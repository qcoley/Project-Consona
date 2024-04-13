import os
import sys
import pygame

from pygame.locals import *


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
    pygame.mixer.pre_init(44100, 16, 2, 4096)
    pygame.init()
    pygame.display.set_caption("Project Consona")
    flags = pygame.RESIZABLE | DOUBLEBUF
    screen = pygame.display.set_mode((1280, 720), flags, 16)
    return screen


def draw_loading_screen(screen):
    loading_screen = pygame.image.load(resource_path('resources/art/screen_loading.png')).convert_alpha()
    screen.blit(loading_screen, (0, 0))
    pygame.display.flip()


def load_graphics():

    loaded_dict = {}

    # non sprite sheets ------------------------------------------------------------------------------------------------
    trading_deck_window = pygame.image.load(resource_path('resources/art/trading_deck_window.png')).convert_alpha()
    trading_card_window = pygame.image.load(resource_path('resources/art/trading_card_window.png')).convert_alpha()
    card_shop_screen = pygame.image.load(resource_path('resources/art/bg_card_shop.png')).convert_alpha()
    all_cats_pet_card = pygame.image.load(resource_path('resources/art/all_cats_pet.png')).convert_alpha()
    dreth_battle_screen = pygame.image.load(resource_path('resources/art/bg_dreth_battle.png')).convert_alpha()
    fishing_journal = pygame.image.load(resource_path('resources/art/fishing_journal.png')).convert_alpha()
    pet_energy_overlay = pygame.image.load(resource_path('resources/art/overlay_pet_energy.png')).convert_alpha()
    pet_window_overlay = pygame.image.load(resource_path('resources/art/overlay_pet_window.png')).convert_alpha()
    overlay_ectrene = pygame.image.load(resource_path('resources/art/overlay_ectrene.png')).convert_alpha()
    overlay_advantages = pygame.image.load(resource_path('resources/art/overlay_type_advantages.png')).convert_alpha()
    overlay_star_waterfall = pygame.image.load(resource_path('resources/art/stardust_waterfall.png')).convert_alpha()
    overlay_bridge_gate = pygame.image.load(resource_path('resources/art/overlay_bridge_gate.png')).convert_alpha()
    apothecary_window = pygame.image.load(resource_path('resources/art/overlay_apothecary_window.png')).convert_alpha()
    weapon_select = pygame.image.load(resource_path('resources/art/overlay_weapon_select.png')).convert_alpha()
    equipment_screen = pygame.image.load(resource_path('resources/art/overlay_equipment_screen.png')).convert_alpha()
    a_char_screen = pygame.image.load(resource_path('resources/art/screen_amuna_character_select.png')).convert_alpha()
    n_char_screen = pygame.image.load(resource_path('resources/art/screen_nuldar_character_select.png')).convert_alpha()
    s_char_screen = pygame.image.load(resource_path('resources/art/screen_sorae_character_select.png')).convert_alpha()
    nascent_grove_screen = pygame.image.load(resource_path('resources/art/bg_nascent_grove.png')).convert_alpha()
    stardust_cove_screen = pygame.image.load(resource_path('resources/art/bg_stardust_post.png')).convert_alpha()
    stardust_post_screen = pygame.image.load(resource_path('resources/art/bg_stardust_inn.png')).convert_alpha()
    star_battle_screen = pygame.image.load(resource_path('resources/art/bg_stardust_battle_screen.png')).convert_alpha()
    seldon_bg_screen = pygame.image.load(resource_path('resources/art/bg_seldon_district.png')).convert_alpha()
    korlok_bg_screen = pygame.image.load(resource_path('resources/art/bg_korlok_district.png')).convert_alpha()
    korlok_re_screen = pygame.image.load(resource_path('resources/art/bg_korlok_district_repaired.png')).convert_alpha()
    korlok_mines_screen = pygame.image.load(resource_path('resources/art/bg_korlok_mines.png')).convert_alpha()
    korlok_battle_screen = pygame.image.load(resource_path('resources/art/bg_korlok_battle_screen.png')).convert_alpha()
    korlok_shop_screen = pygame.image.load(resource_path('resources/art/bg_korlok_shop.png')).convert_alpha()
    korlok_inn_day = pygame.image.load(resource_path('resources/art/bg_korlok_inn.png')).convert_alpha()
    korlok_inn_night = pygame.image.load(resource_path('resources/art/bg_korlok_inn_night.png')).convert_alpha()
    korlok_inn_morning = pygame.image.load(resource_path('resources/art/bg_korlok_inn_morning.png')).convert_alpha()
    korlok_inn_afternoon = pygame.image.load(resource_path('resources/art/bg_korlok_inn_afternoon.png')).convert_alpha()
    korlok_apothecary = pygame.image.load(resource_path('resources/art/bg_korlok_apothecary.png')).convert_alpha()
    fishing_hut_screen = pygame.image.load(resource_path('resources/art/bg_fishing_hut_screen.png')).convert_alpha()
    korlok_forge_bg = pygame.image.load(resource_path('resources/art/bg_korlok_forge.png')).convert_alpha()
    terra_trail_bg = pygame.image.load(resource_path('resources/art/bg_terra_trail.png')).convert_alpha()
    eldream_bg_screen = pygame.image.load(resource_path('resources/art/bg_eldream_district.png')).convert_alpha()
    eldream_inn_day = pygame.image.load(resource_path('resources/art/bg_eldream_inn.png')).convert_alpha()
    eldream_inn_night = pygame.image.load(resource_path('resources/art/bg_eldream_inn_night.png')).convert_alpha()
    eldream_inn_morning = pygame.image.load(resource_path('resources/art/bg_eldream_inn_morning.png')).convert_alpha()
    eldream_inn_afternoon = (pygame.image.load
                             (resource_path('resources/art/bg_eldream_inn_afternoon.png')).convert_alpha())
    eldream_shop_screen = pygame.image.load(resource_path('resources/art/bg_eldream_shop.png')).convert_alpha()
    eldream_menagerie = pygame.image.load(resource_path('resources/art/bg_eldream_menagerie.png')).convert_alpha()
    eldream_interaction = pygame.image.load(resource_path('resources/art/bg_eldream_interaction.png')).convert_alpha()
    eldream_altar_bg = pygame.image.load(resource_path('resources/art/bg_eldream_altar.png')).convert_alpha()
    ectrenos_bg_screen = pygame.image.load(resource_path('resources/art/bg_ectrenos.png')).convert_alpha()
    ectrenos_left_bg_screen = pygame.image.load(resource_path('resources/art/bg_ectrenos_left.png')).convert_alpha()
    ectrenos_right_bg_screen = pygame.image.load(resource_path('resources/art/bg_ectrenos_right.png')).convert_alpha()
    ectrenos_front_bg_screen = pygame.image.load(resource_path('resources/art/bg_ectrenos_front.png')).convert_alpha()
    ectrenos_alcove_screen = pygame.image.load(resource_path('resources/art/bg_ectrenos_alcove.png')).convert_alpha()
    alcove_b = pygame.image.load(resource_path('resources/art/bg_ectrenos_alcove_battle_screen.png')).convert_alpha()
    alcove_fishing = pygame.image.load(resource_path('resources/art/bg_ectrenos_fishing.png')).convert_alpha()
    ectrenos_interaction = pygame.image.load(resource_path('resources/art/bg_ectrenos_interaction.png')).convert_alpha()
    ectrenos_mini_map = pygame.image.load(resource_path('resources/art/overlay_mini_map_ectrenos.png')).convert_alpha()
    ect_mini_l = pygame.image.load(resource_path('resources/art/overlay_mini_map_ectrenos_left.png')).convert_alpha()
    ect_mini_r = pygame.image.load(resource_path('resources/art/overlay_mini_map_ectrenos_right.png')).convert_alpha()
    ect_mini_f = pygame.image.load(resource_path('resources/art/overlay_mini_map_ectrenos_front.png')).convert_alpha()
    marrow_mini_map = pygame.image.load(resource_path('resources/art/overlay_mini_map_marrow.png')).convert_alpha()
    mar_mini_t_l = pygame.image.load(resource_path('resources/art/overlay_mini_map_marrow_tower_l.png')).convert_alpha()
    mar_mini_t_r = pygame.image.load(resource_path('resources/art/overlay_mini_map_marrow_tower_r.png')).convert_alpha()
    mar_mini_r_l = pygame.image.load(resource_path('resources/art/overlay_mini_map_marrow_ramp_l.png')).convert_alpha()
    mar_mini_r_r = pygame.image.load(resource_path('resources/art/overlay_mini_map_marrow_ramp_r.png')).convert_alpha()
    mar_mini_r_e = \
        pygame.image.load(resource_path('resources/art/overlay_mini_map_marrow_ramp_r_end.png')).convert_alpha()
    mar_mini_l_e = \
        pygame.image.load(resource_path('resources/art/overlay_mini_map_marrow_ramp_l_end.png')).convert_alpha()
    marrow_interaction_bg = pygame.image.load(resource_path('resources/art/bg_marrow_interaction.png')).convert_alpha()
    marrow_entrance_bg = pygame.image.load(resource_path('resources/art/bg_marrow_enter.png')).convert_alpha()
    marrow_entrance_bg_open = pygame.image.load(resource_path('resources/art/bg_marrow_enter_open.png')).convert_alpha()
    mar_tower_e_bg = pygame.image.load(resource_path('resources/art/bg_marrow_rampart_tower_east.png')).convert_alpha()
    mar_tower_w_bg = pygame.image.load(resource_path('resources/art/bg_marrow_rampart_tower_west.png')).convert_alpha()
    mar_rampart_e_bg = pygame.image.load(resource_path('resources/art/bg_marrow_rampart_east.png')).convert_alpha()
    mar_rampart_w_bg = pygame.image.load(resource_path('resources/art/bg_marrow_rampart_west.png')).convert_alpha()
    m_ramp_e_end_bg = pygame.image.load(resource_path('resources/art/bg_marrow_rampart_east_end.png')).convert_alpha()
    m_end_block = pygame.image.load(resource_path('resources/art/bg_marrow_rampart_east_end_block.png')).convert_alpha()
    m_ramp_w_end_bg = pygame.image.load(resource_path('resources/art/bg_marrow_rampart_west_end.png')).convert_alpha()
    marrow_district_bg = pygame.image.load(resource_path('resources/art/bg_marrow_district.png')).convert_alpha()
    sub_marrow_bg = pygame.image.load(resource_path('resources/art/bg_sub_marrow.png')).convert_alpha()
    sub_marrow_battle = pygame.image.load(resource_path('resources/art/bg_sub_marrow_battle.png')).convert_alpha()
    castle_one_bg = pygame.image.load(resource_path('resources/art/bg_castle_one.png')).convert_alpha()
    castle_one_rope_bg = pygame.image.load(resource_path('resources/art/bg_castle_one_roped.png')).convert_alpha()
    castle_one_key_bg = pygame.image.load(resource_path('resources/art/bg_castle_one_keyed.png')).convert_alpha()
    castle_two_bg = pygame.image.load(resource_path('resources/art/bg_castle_two.png')).convert_alpha()
    castle_two_rope_bg = pygame.image.load(resource_path('resources/art/bg_castle_two_roped.png')).convert_alpha()
    castle_three_bg = pygame.image.load(resource_path('resources/art/bg_castle_three.png')).convert_alpha()
    castle_three_rope_bg = pygame.image.load(resource_path('resources/art/bg_castle_three_roped.png')).convert_alpha()
    castle_lair_bg = pygame.image.load(resource_path('resources/art/bg_castle_lair.png')).convert_alpha()
    castle_lair_zero_bg = pygame.image.load(resource_path('resources/art/bg_castle_lair_zero.png')).convert_alpha()
    castle_lair_one_bg = pygame.image.load(resource_path('resources/art/bg_castle_lair_one.png')).convert_alpha()
    castle_lair_two_bg = pygame.image.load(resource_path('resources/art/bg_castle_lair_two.png')).convert_alpha()
    caldera_bg = pygame.image.load(resource_path('resources/art/bg_caldera.png')).convert_alpha()
    e_f_interact = pygame.image.load(resource_path('resources/art/bg_ectrenos_interaction_front.png')).convert_alpha()
    fishing_hut_bg = pygame.image.load(resource_path('resources/art/bg_fishing_hut.png')).convert_alpha()
    terra_trail_screen = pygame.image.load(resource_path('resources/art/bg_terra_trail_screen.png')).convert_alpha()
    caves_battle_screen = pygame.image.load(resource_path('resources/art/bg_cave_battle_screen.png')).convert_alpha()
    mines_battle_screen = pygame.image.load(resource_path('resources/art/bg_mines_battle.png')).convert_alpha()
    rohir_river_screen = pygame.image.load(resource_path('resources/art/bg_rohir_river.png')).convert_alpha()
    reservoir_a_screen = pygame.image.load(resource_path('resources/art/bg_reservoir_a.png')).convert_alpha()
    reservoir_b_screen = pygame.image.load(resource_path('resources/art/bg_reservoir_b.png')).convert_alpha()
    reservoir_c_screen = pygame.image.load(resource_path('resources/art/bg_reservoir_c.png')).convert_alpha()
    reservoir_battle = pygame.image.load(resource_path('resources/art/bg_reservoir_battle_screen.png')).convert_alpha()
    seldon_battle_screen = pygame.image.load(resource_path('resources/art/bg_seldon_battle_screen.png')).convert_alpha()
    nascent_screen = pygame.image.load(resource_path('resources/art/bg_nascent_interaction_screen.png')).convert_alpha()
    seldon_shop_screen = pygame.image.load(resource_path('resources/art/bg_seldon_shop.png')).convert_alpha()
    seldon_inn_day = pygame.image.load(resource_path('resources/art/bg_seldon_inn.png')).convert_alpha()
    seldon_inn_night = pygame.image.load(resource_path('resources/art/bg_seldon_inn_night.png')).convert_alpha()
    seldon_inn_morning = pygame.image.load(resource_path('resources/art/bg_seldon_inn_morning.png')).convert_alpha()
    seldon_inn_afternoon = pygame.image.load(resource_path('resources/art/bg_seldon_inn_afternoon.png')).convert_alpha()
    seldon_academia_screen = pygame.image.load(resource_path('resources/art/bg_seldon_academia.png')).convert_alpha()
    seldon_hearth_screen = pygame.image.load(resource_path('resources/art/screen_seldon_hearth.png')).convert_alpha()
    korlok_hearth_screen = pygame.image.load(resource_path('resources/art/screen_korlok_hearth.png')).convert_alpha()
    eldream_hearth_screen = pygame.image.load(resource_path('resources/art/screen_eldream_hearth.png')).convert_alpha()
    marrow_hearth_screen = pygame.image.load(resource_path('resources/art/screen_marrow_hearth.png')).convert_alpha()
    game_over_screen = pygame.image.load(resource_path('resources/art/screen_game_over.png')).convert_alpha()
    start_screen = pygame.image.load(resource_path('resources/art/start_screen.png')).convert_alpha()
    start_screen_logo = pygame.image.load(resource_path('resources/art/start_screen_logo.png')).convert_alpha()
    nera_sleep_screen = pygame.image.load(resource_path('resources/art/screen_nera_sleep.png')).convert_alpha()
    bar_backdrop = pygame.image.load(resource_path('resources/art/overlay_status_bar_backdrop.png')).convert_alpha()
    enemy_status = pygame.image.load(resource_path('resources/art/overlay_enemy_status_backdrop.png')).convert_alpha()
    enemy_bar_backdrop = pygame.image.load(resource_path('resources/art/overlay_enemy_status_bar.png')).convert_alpha()
    buy_inventory = pygame.image.load(resource_path('resources/art/overlay_buy_inventory.png')).convert_alpha()
    pine_tree = pygame.image.load(resource_path('resources/art/sprite_pine_tree.png')).convert_alpha()
    rohir_gate = pygame.image.load(resource_path('resources/art/overlay_rohir_gate.png')).convert_alpha()
    lets_go_button = pygame.image.load(resource_path('resources/art/button_lets_go.png')).convert_alpha()
    learn_button = pygame.image.load(resource_path('resources/art/overlay_learn.png')).convert_alpha()
    skill_learn_button = pygame.image.load(resource_path('resources/art/overlay_skill_learn.png')).convert_alpha()
    nascent_gate_popup = pygame.image.load(resource_path('resources/art/popup_nascent_gate.png')).convert_alpha()
    level_up_win = pygame.image.load(resource_path('resources/art/popup_level_up.png')).convert_alpha()
    close_button = pygame.image.load(resource_path('resources/art/button_close.png')).convert_alpha()
    knowledge_window = pygame.image.load(resource_path('resources/art/overlay_knowledge.png')).convert_alpha()
    skill_bar = pygame.image.load(resource_path('resources/art/overlay_skill_bar.png')).convert_alpha()
    start_button = pygame.image.load(resource_path('resources/art/button_start.png')).convert_alpha()
    npc_name_plate = pygame.image.load(resource_path('resources/art/overlay_npc_name_plate.png')).convert_alpha()
    char_select_overlay = pygame.image.load(resource_path('resources/art/overlay_character_select.png')).convert_alpha()
    role_selection_overlay = pygame.image.load(resource_path('resources/art/overlay_role_select.png')).convert_alpha()
    location_overlay = pygame.image.load(resource_path('resources/art/overlay_location.png')).convert_alpha()
    popup_loot = pygame.image.load(resource_path('resources/art/popup_enemy_defeat.png')).convert_alpha()
    stardust_entrance = pygame.image.load(resource_path('resources/art/overlay_stardust_entrance.png')).convert_alpha()
    upgrade_overlay = pygame.image.load(resource_path('resources/art/overlay_upgrade_select.png')).convert_alpha()
    cat_pet_button_overlay = pygame.image.load(resource_path('resources/art/overlay_cat_pet.png')).convert_alpha()
    book_high = pygame.image.load(resource_path('resources/art/book_button_highlight.png')).convert_alpha()
    save_hearth_high = pygame.image.load(resource_path('resources/art/buttons_small_high.png')).convert_alpha()
    lets_go_high = pygame.image.load(resource_path('resources/art/button_lets_go_highlight.png')).convert_alpha()
    water_player = pygame.image.load(resource_path('resources/art/overlay_water_player.png')).convert_alpha()
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
    reservoir_passage = pygame.image.load(resource_path('resources/art/overlay_reservoir_passage.png')).convert_alpha()
    reservoir_exit = pygame.image.load(resource_path('resources/art/overlay_reservoir_exit.png')).convert_alpha()
    reservoir_enter = pygame.image.load(resource_path('resources/art/overlay_reservoir_enter.png')).convert_alpha()
    mines_entrance = pygame.image.load(resource_path('resources/art/overlay_mines_entrance.png')).convert_alpha()
    mines_wall = pygame.image.load(resource_path('resources/art/overlay_mines_wall.png')).convert_alpha()
    mines_light = pygame.image.load(resource_path('resources/art/overlay_mines_light.png')).convert_alpha()
    terra_mountains = pygame.image.load(resource_path('resources/art/'
                                                      'overlay_terra_trail_mountains.png')).convert_alpha()
    terra_cave = pygame.image.load(resource_path('resources/art/overlay_trail_cave.png')).convert_alpha()
    sprite_chinzilla = pygame.image.load(resource_path('resources/art/sprite_chinzilla.png')).convert_alpha()
    overlay_eldream_river = pygame.image.load(resource_path('resources/art/overlay_eldream_river.png')).convert_alpha()
    overlay_chroma_bridge = pygame.image.load(resource_path('resources/art/overlay_chroma_bridge.png')).convert_alpha()
    chroma_small = pygame.image.load(resource_path('resources/art/overlay_chroma_bridge_small.png')).convert_alpha()
    chroma_forge = pygame.image.load(resource_path('resources/art/overlay_chroma_bridge_forge.png')).convert_alpha()
    stardust_top = pygame.image.load(resource_path('resources/art/overlay_stardust_top.png')).convert_alpha()
    alcove_star = pygame.image.load(resource_path('resources/art/overlay_alcove_star.png')).convert_alpha()
    tree_tops = pygame.image.load(resource_path('resources/art/overlay_tree_tops.png')).convert_alpha()
    a_building_tops = pygame.image.load(resource_path('resources/art/overlay_amuna_building_tops.png')).convert_alpha()
    n_building_tops = pygame.image.load(resource_path('resources/art/overlay_nuldar_building_tops.png')).convert_alpha()
    level_up_vis = pygame.image.load(resource_path('resources/art/overlay_level_up.png')).convert_alpha()
    quest_accepted = pygame.image.load(resource_path('resources/art/overlay_quest_accepted.png')).convert_alpha()
    task_accepted = pygame.image.load(resource_path('resources/art/overlay_task_accepted.png')).convert_alpha()
    kart_overworld = pygame.image.load(resource_path('resources/art/sprite_kart_overworld_full.png')).convert_alpha()
    kart_big_full = pygame.image.load(resource_path('resources/art/sprite_kart_full.png')).convert_alpha()
    mirror_overlay = pygame.image.load(resource_path('resources/art/overlay_mirror_image.png')).convert_alpha()
    over_mar_ramps_west = pygame.image.load(resource_path('resources/art/overlay_marrow_ramp_west.png')).convert_alpha()
    over_mar_ramps_east = pygame.image.load(resource_path('resources/art/overlay_marrow_ramp_east.png')).convert_alpha()
    overlay_chroma_ramps = pygame.image.load(resource_path('resources/art/overlay_chroma_ramps.png')).convert_alpha()
    popup_wide = pygame.image.load(resource_path('resources/art/popup_interaction_wide.png')).convert_alpha()
    ramparts_battle = pygame.image.load(resource_path('resources/art/bg_marrow_rampart_battle.png')).convert_alpha()
    tower_battle = pygame.image.load(resource_path('resources/art/bg_marrow_tower_battle.png')).convert_alpha()
    overlay_enemy_vanish = pygame.image.load(resource_path('resources/art/overlay_enemy_vanish.png')).convert_alpha()
    overlay_smelting = pygame.image.load(resource_path('resources/art/overlay_smelting.png')).convert_alpha()
    overlay_enchanting = pygame.image.load(resource_path('resources/art/overlay_enchanting.png')).convert_alpha()
    overlay_flower_counts = pygame.image.load(resource_path('resources/art/overlay_flower_counts.png')).convert_alpha()
    overlay_fish_counts = pygame.image.load(resource_path('resources/art/overlay_fish_counts.png')).convert_alpha()
    apothis_star = pygame.image.load(resource_path('resources/art/apothis_gift_star_overlay.png')).convert_alpha()
    overlay_stardust_star = pygame.image.load(resource_path('resources/art/overlay_stardust_star.png')).convert_alpha()

    m_switch = pygame.image.load(resource_path('resources/art/overlay_marrow_switch.png')).convert_alpha()
    m_switch_b = pygame.image.load(resource_path('resources/art/overlay_marrow_switch_blue.png')).convert_alpha()
    m_switch_r = pygame.image.load(resource_path('resources/art/overlay_marrow_switch_red.png')).convert_alpha()
    m_switch_p = pygame.image.load(resource_path('resources/art/overlay_marrow_switch_purple.png')).convert_alpha()
    m_switch_c = pygame.image.load(resource_path('resources/art/overlay_marrow_switch_complete.png')).convert_alpha()
    m_switch_box = pygame.image.load(resource_path('resources/art/marrow_switch_box.png')).convert_alpha()
    chest_small = pygame.image.load(resource_path('resources/art/sprite_dungeon_chest_small.png')).convert_alpha()
    overlay_prism = pygame.image.load(resource_path('resources/art/overlay_prism_activate.png')).convert_alpha()

    apothis_scene_1 = pygame.image.load(resource_path('resources/art/cutscene_apothis_1.png')).convert_alpha()
    apothis_scene_2 = pygame.image.load(resource_path('resources/art/cutscene_apothis_2.png')).convert_alpha()
    apothis_scene_3 = pygame.image.load(resource_path('resources/art/cutscene_apothis_3.png')).convert_alpha()
    apothis_scene_4 = pygame.image.load(resource_path('resources/art/cutscene_apothis_4.png')).convert_alpha()
    apothis_scene_5 = pygame.image.load(resource_path('resources/art/cutscene_apothis_5.png')).convert_alpha()
    apothis_scene_6 = pygame.image.load(resource_path('resources/art/cutscene_apothis_6.png')).convert_alpha()

    apothis_scene_1_n = pygame.image.load(resource_path('resources/art/cutscene_apothis_1_night.png')).convert_alpha()
    apothis_scene_2_n = pygame.image.load(resource_path('resources/art/cutscene_apothis_2_night.png')).convert_alpha()
    apothis_scene_3_n = pygame.image.load(resource_path('resources/art/cutscene_apothis_3_night.png')).convert_alpha()
    apothis_scene_4_n = pygame.image.load(resource_path('resources/art/cutscene_apothis_4_night.png')).convert_alpha()
    apothis_scene_5_n = pygame.image.load(resource_path('resources/art/cutscene_apothis_5_night.png')).convert_alpha()
    apothis_scene_6_n = pygame.image.load(resource_path('resources/art/cutscene_apothis_6_night.png')).convert_alpha()

    dreth_scene_0 = pygame.image.load(resource_path('resources/art/cutscene_apothis_dreth_0.png')).convert_alpha()
    dreth_scene_1 = pygame.image.load(resource_path('resources/art/cutscene_apothis_dreth_1.png')).convert_alpha()
    dreth_scene_2 = pygame.image.load(resource_path('resources/art/cutscene_apothis_dreth_2.png')).convert_alpha()
    dreth_scene_3 = pygame.image.load(resource_path('resources/art/cutscene_apothis_dreth_3.png')).convert_alpha()
    dreth_scene_4 = pygame.image.load(resource_path('resources/art/cutscene_apothis_dreth_4.png')).convert_alpha()
    dreth_scene_5 = pygame.image.load(resource_path('resources/art/cutscene_apothis_dreth_5.png')).convert_alpha()
    dreth_scene_6 = pygame.image.load(resource_path('resources/art/cutscene_apothis_dreth_6.png')).convert_alpha()
    dreth_scene_7 = pygame.image.load(resource_path('resources/art/cutscene_apothis_dreth_7.png')).convert_alpha()
    dreth_scene_8 = pygame.image.load(resource_path('resources/art/cutscene_apothis_dreth_8.png')).convert_alpha()

    final_scene_1 = pygame.image.load(resource_path('resources/art/cutscene_final_1.png')).convert_alpha()
    final_scene_2 = pygame.image.load(resource_path('resources/art/cutscene_final_2.png')).convert_alpha()
    final_scene_3 = pygame.image.load(resource_path('resources/art/cutscene_final_3.png')).convert_alpha()
    final_scene_4 = pygame.image.load(resource_path('resources/art/cutscene_final_4.png')).convert_alpha()
    final_scene_5 = pygame.image.load(resource_path('resources/art/cutscene_final_5.png')).convert_alpha()
    final_scene_6 = pygame.image.load(resource_path('resources/art/cutscene_final_6.png')).convert_alpha()
    final_scene_7 = pygame.image.load(resource_path('resources/art/cutscene_final_7.png')).convert_alpha()
    final_scene_8 = pygame.image.load(resource_path('resources/art/cutscene_final_8.png')).convert_alpha()
    final_scene_9 = pygame.image.load(resource_path('resources/art/cutscene_final_9.png')).convert_alpha()
    final_scene_10 = pygame.image.load(resource_path('resources/art/cutscene_final_10.png')).convert_alpha()
    final_scene_11 = pygame.image.load(resource_path('resources/art/cutscene_final_11.png')).convert_alpha()
    final_scene_12 = pygame.image.load(resource_path('resources/art/cutscene_final_12.png')).convert_alpha()
    final_scene_13 = pygame.image.load(resource_path('resources/art/cutscene_final_13.png')).convert_alpha()
    final_scene_14 = pygame.image.load(resource_path('resources/art/cutscene_final_14.png')).convert_alpha()

    credit_scene_1 = pygame.image.load(resource_path('resources/art/screen_credits_marrow.png')).convert_alpha()
    credit_scene_2 = pygame.image.load(resource_path('resources/art/screen_credits_seldon.png')).convert_alpha()
    credit_scene_3 = pygame.image.load(resource_path('resources/art/screen_credits_korlok.png')).convert_alpha()
    credit_scene_4 = pygame.image.load(resource_path('resources/art/screen_credits_eldream.png')).convert_alpha()
    credit_scene_5 = pygame.image.load(resource_path('resources/art/screen_credits_thanks.png')).convert_alpha()

    effect_dawn = pygame.image.load(resource_path('resources/art/effect_dawn.png')).convert_alpha()
    effect_e_morning = pygame.image.load(resource_path('resources/art/effect_early_morning.png')).convert_alpha()
    effect_morning = pygame.image.load(resource_path('resources/art/effect_morning.png')).convert_alpha()
    effect_e_afternoon = pygame.image.load(resource_path('resources/art/effect_early_afternoon.png')).convert_alpha()
    effect_afternoon = pygame.image.load(resource_path('resources/art/effect_afternoon.png')).convert_alpha()
    effect_dusk = pygame.image.load(resource_path('resources/art/effect_dusk.png')).convert_alpha()
    effect_night = pygame.image.load(resource_path('resources/art/effect_night.png')).convert_alpha()

    night_sleep_overlay = pygame.image.load(resource_path('resources/art/night_sleep_overlay.png')).convert_alpha()

    color_keys = [bar_backdrop, enemy_status, enemy_bar_backdrop, buy_inventory, pine_tree,
                  rohir_gate, lets_go_button, learn_button, skill_learn_button, nascent_gate_popup, level_up_win,
                  close_button, knowledge_window, skill_bar, start_button, npc_name_plate, char_select_overlay,
                  role_selection_overlay, location_overlay, popup_loot, stardust_entrance, book_high,
                  upgrade_overlay, cat_pet_button_overlay, save_hearth_high, lets_go_high, dungeon_entrance,
                  world_map_button, world_map_button_high, nede_big, dungeon_wall_1, dungeon_wall_2, dungeon_gate,
                  reservoir_passage, reservoir_exit, reservoir_enter, mines_entrance,
                  mines_wall, mines_light, terra_mountains, terra_cave, weapon_select,
                  overlay_eldream_river, overlay_advantages, overlay_ectrene, pet_energy_overlay, overlay_chroma_bridge,
                  chroma_small, stardust_top, alcove_star, tree_tops, a_building_tops, level_up_vis, n_building_tops,
                  kart_overworld, kart_big_full, mirror_overlay, start_screen_logo, overlay_star_waterfall,
                  overlay_bridge_gate, over_mar_ramps_east, over_mar_ramps_west, overlay_chroma_ramps, m_switch,
                  m_switch_b, m_switch_r, m_switch_p, m_switch_c, m_switch_box, popup_wide,
                  overlay_enemy_vanish, chroma_forge, overlay_smelting, overlay_enchanting, chest_small, overlay_prism,
                  apothis_star, overlay_stardust_star, night_sleep_overlay]

    for image in color_keys:
        image.set_colorkey((255, 255, 255))

    loaded_dict["pet_window_overlay"] = pet_window_overlay
    loaded_dict["night_sleep_overlay"] = night_sleep_overlay
    loaded_dict["effect_dawn"] = effect_dawn
    loaded_dict["effect_early_morning"] = effect_e_morning
    loaded_dict["effect_morning"] = effect_morning
    loaded_dict["effect_early_afternoon"] = effect_e_afternoon
    loaded_dict["effect_afternoon"] = effect_afternoon
    loaded_dict["effect_dusk"] = effect_dusk
    loaded_dict["effect_night"] = effect_night
    loaded_dict["trading_deck"] = trading_deck_window
    loaded_dict["trading_window"] = trading_card_window
    loaded_dict["card_shop_bg"] = card_shop_screen
    loaded_dict["all_cats_pet_card"] = all_cats_pet_card
    loaded_dict["apothis_star"] = apothis_star
    loaded_dict["dreth_battle_screen"] = dreth_battle_screen
    loaded_dict["castle_lair_bg"] = castle_lair_bg
    loaded_dict["castle_lair_zero_bg"] = castle_lair_zero_bg
    loaded_dict["castle_lair_one_bg"] = castle_lair_one_bg
    loaded_dict["castle_lair_two_bg"] = castle_lair_two_bg
    loaded_dict["caldera_bg"] = caldera_bg
    loaded_dict["castle_two_bg"] = castle_two_bg
    loaded_dict["castle_two_roped_bg"] = castle_two_rope_bg
    loaded_dict["castle_three_bg"] = castle_three_bg
    loaded_dict["castle_three_roped_bg"] = castle_three_rope_bg
    loaded_dict["castle_one_bg"] = castle_one_bg
    loaded_dict["castle_one_roped_bg"] = castle_one_rope_bg
    loaded_dict["castle_one_keyed_bg"] = castle_one_key_bg
    loaded_dict["overlay_prism"] = overlay_prism
    loaded_dict["sub_marrow_battle_screen"] = sub_marrow_battle
    loaded_dict["chest_small"] = chest_small
    loaded_dict["flower_counts"] = overlay_flower_counts
    loaded_dict["fish_counts"] = overlay_fish_counts
    loaded_dict["fishing_journal"] = fishing_journal
    loaded_dict["marrow_mini_map"] = marrow_mini_map
    loaded_dict["marrow_mini_map_tower_left"] = mar_mini_t_l
    loaded_dict["marrow_mini_map_tower_right"] = mar_mini_t_r
    loaded_dict["marrow_mini_map_ramps_left"] = mar_mini_r_l
    loaded_dict["marrow_mini_map_ramps_right"] = mar_mini_r_r
    loaded_dict["marrow_mini_map_ramps_right_end"] = mar_mini_r_e
    loaded_dict["marrow_mini_map_ramps_left_end"] = mar_mini_l_e
    loaded_dict["ectrenos_mini_map_left"] = ect_mini_l
    loaded_dict["ectrenos_mini_map_right"] = ect_mini_r
    loaded_dict["ectrenos_mini_map_front"] = ect_mini_f
    loaded_dict["ectrenos_mini_map"] = ectrenos_mini_map
    loaded_dict["overlay_smelting"] = overlay_smelting
    loaded_dict["overlay_enchanting"] = overlay_enchanting
    loaded_dict["quest_accepted"] = quest_accepted
    loaded_dict["task_accepted"] = task_accepted
    loaded_dict["level_up_vis"] = level_up_vis
    loaded_dict["amuna_building_top"] = a_building_tops
    loaded_dict["nuldar_building_top"] = n_building_tops
    loaded_dict["tree_top"] = tree_tops
    loaded_dict["alcove_star"] = alcove_star
    loaded_dict["ectrenos_front_interaction"] = e_f_interact
    loaded_dict["ectrenos_interaction"] = ectrenos_interaction
    loaded_dict["eldream_interaction"] = eldream_interaction
    loaded_dict["stardust_top"] = stardust_top
    loaded_dict["chroma_bridge_small"] = chroma_small
    loaded_dict["chroma_bridge"] = overlay_chroma_bridge
    loaded_dict["chroma_forge"] = chroma_forge
    loaded_dict["pet_energy"] = pet_energy_overlay
    loaded_dict["eldream_menagerie"] = eldream_menagerie
    loaded_dict["overlay_ectrene"] = overlay_ectrene
    loaded_dict["overlay_stardust_waterfall"] = overlay_star_waterfall
    loaded_dict["overlay_bridge_gate"] = overlay_bridge_gate
    loaded_dict["overlay_chroma_ramps"] = overlay_chroma_ramps
    loaded_dict["ectrenos_bg"] = ectrenos_bg_screen
    loaded_dict["ectrenos_left_bg"] = ectrenos_left_bg_screen
    loaded_dict["ectrenos_right_bg"] = ectrenos_right_bg_screen
    loaded_dict["ectrenos_front_bg"] = ectrenos_front_bg_screen
    loaded_dict["ectrenos_alcove_bg"] = ectrenos_alcove_screen
    loaded_dict["type advantages"] = overlay_advantages
    loaded_dict["fishing_hut_bg"] = fishing_hut_bg
    loaded_dict["fishing_hut_screen"] = fishing_hut_screen
    loaded_dict["fishing_alcove_bg"] = alcove_fishing
    loaded_dict["eldream_river"] = overlay_eldream_river
    loaded_dict["apothecary_window"] = apothecary_window
    loaded_dict["weapon_select"] = weapon_select
    loaded_dict["chinzilla"] = sprite_chinzilla
    loaded_dict["caves_battle_screen"] = caves_battle_screen
    loaded_dict["equipment_screen"] = equipment_screen
    loaded_dict["a_char_screen"] = a_char_screen
    loaded_dict["n_char_screen"] = n_char_screen
    loaded_dict["s_char_screen"] = s_char_screen
    loaded_dict["nascent_grove_screen"] = nascent_grove_screen
    loaded_dict["stardust_cove_screen"] = stardust_cove_screen
    loaded_dict["stardust_post_screen"] = stardust_post_screen
    loaded_dict["star_battle_screen"] = star_battle_screen
    loaded_dict["seldon_bg_screen"] = seldon_bg_screen
    loaded_dict["korlok_bg_screen"] = korlok_bg_screen
    loaded_dict["korlok_repaired_screen"] = korlok_re_screen
    loaded_dict["korlok_forge_bg"] = korlok_forge_bg
    loaded_dict["eldream_bg_screen"] = eldream_bg_screen
    loaded_dict["eldream_altar_bg"] = eldream_altar_bg
    loaded_dict["marrow_interaction_bg"] = marrow_interaction_bg
    loaded_dict["marrow_entrance_bg"] = marrow_entrance_bg
    loaded_dict["marrow_entrance_bg_open"] = marrow_entrance_bg_open
    loaded_dict["marrow_tower_east_bg"] = mar_tower_e_bg
    loaded_dict["marrow_tower_west_bg"] = mar_tower_w_bg
    loaded_dict["marrow_rampart_east_bg"] = mar_rampart_e_bg
    loaded_dict["marrow_rampart_west_bg"] = mar_rampart_w_bg
    loaded_dict["marrow_rampart_east_end_bg"] = m_ramp_e_end_bg
    loaded_dict["marrow_rampart_west_end_bg"] = m_ramp_w_end_bg
    loaded_dict["marrow_rampart_west_end_bg_block"] = m_end_block
    loaded_dict["marrow_district_bg"] = marrow_district_bg
    loaded_dict["sub_marrow_bg"] = sub_marrow_bg
    loaded_dict["overlay_marrow_ramps_east"] = over_mar_ramps_east
    loaded_dict["overlay_marrow_ramps_west"] = over_mar_ramps_west
    loaded_dict["rohir_river_screen"] = rohir_river_screen
    loaded_dict["reservoir_a_screen"] = reservoir_a_screen
    loaded_dict["reservoir_b_screen"] = reservoir_b_screen
    loaded_dict["reservoir_c_screen"] = reservoir_c_screen
    loaded_dict["reservoir_battle_screen"] = reservoir_battle
    loaded_dict["seldon_battle_screen"] = seldon_battle_screen
    loaded_dict["nascent_interaction_screen"] = nascent_screen
    loaded_dict["korlok_battle_screen"] = korlok_battle_screen
    loaded_dict["mines_battle_screen"] = mines_battle_screen
    loaded_dict["alcove_battle_screen"] = alcove_b
    loaded_dict["seldon_shop_screen"] = seldon_shop_screen
    loaded_dict["korlok_shop_screen"] = korlok_shop_screen
    loaded_dict["eldream_shop_screen"] = eldream_shop_screen
    loaded_dict["seldon_inn_day"] = seldon_inn_day
    loaded_dict["seldon_inn_night"] = seldon_inn_night
    loaded_dict["seldon_inn_morning"] = seldon_inn_morning
    loaded_dict["seldon_inn_afternoon"] = seldon_inn_afternoon
    loaded_dict["korlok_inn_day"] = korlok_inn_day
    loaded_dict["korlok_inn_night"] = korlok_inn_night
    loaded_dict["korlok_inn_morning"] = korlok_inn_morning
    loaded_dict["korlok_inn_afternoon"] = korlok_inn_afternoon
    loaded_dict["eldream_inn_day"] = eldream_inn_day
    loaded_dict["eldream_inn_night"] = eldream_inn_night
    loaded_dict["eldream_inn_morning"] = eldream_inn_morning
    loaded_dict["eldream_inn_afternoon"] = eldream_inn_afternoon
    loaded_dict["terra_trail_bg"] = terra_trail_bg
    loaded_dict["seldon_academia_screen"] = seldon_academia_screen
    loaded_dict["seldon_hearth_screen"] = seldon_hearth_screen
    loaded_dict["eldream_hearth_screen"] = eldream_hearth_screen
    loaded_dict["marrow_hearth_screen"] = marrow_hearth_screen
    loaded_dict["game_over_screen"] = game_over_screen
    loaded_dict["start_screen"] = start_screen
    loaded_dict["start_screen_logo"] = start_screen_logo
    loaded_dict["nera_sleep_screen"] = nera_sleep_screen
    loaded_dict["bar_backdrop"] = bar_backdrop
    loaded_dict["enemy_status"] = enemy_status
    loaded_dict["enemy_bar_backdrop"] = enemy_bar_backdrop
    loaded_dict["buy_inventory"] = buy_inventory
    loaded_dict["pine_tree"] = pine_tree
    loaded_dict["rohir_gate"] = rohir_gate
    loaded_dict["lets_go_button"] = lets_go_button
    loaded_dict["learn_button"] = learn_button
    loaded_dict["skill_learn_button"] = skill_learn_button
    loaded_dict["nascent_gate_popup"] = nascent_gate_popup
    loaded_dict["level_up_win"] = level_up_win
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
    loaded_dict["apothis_1_night"] = apothis_scene_1_n
    loaded_dict["apothis_2_night"] = apothis_scene_2_n
    loaded_dict["apothis_3_night"] = apothis_scene_3_n
    loaded_dict["apothis_4_night"] = apothis_scene_4_n
    loaded_dict["apothis_5_night"] = apothis_scene_5_n
    loaded_dict["apothis_6_night"] = apothis_scene_6_n
    loaded_dict["dreth_0"] = dreth_scene_0
    loaded_dict["dreth_1"] = dreth_scene_1
    loaded_dict["dreth_2"] = dreth_scene_2
    loaded_dict["dreth_3"] = dreth_scene_3
    loaded_dict["dreth_4"] = dreth_scene_4
    loaded_dict["dreth_5"] = dreth_scene_5
    loaded_dict["dreth_6"] = dreth_scene_6
    loaded_dict["dreth_7"] = dreth_scene_7
    loaded_dict["dreth_8"] = dreth_scene_8
    loaded_dict["final_1"] = final_scene_1
    loaded_dict["final_2"] = final_scene_2
    loaded_dict["final_3"] = final_scene_3
    loaded_dict["final_4"] = final_scene_4
    loaded_dict["final_5"] = final_scene_5
    loaded_dict["final_6"] = final_scene_6
    loaded_dict["final_7"] = final_scene_7
    loaded_dict["final_8"] = final_scene_8
    loaded_dict["final_9"] = final_scene_9
    loaded_dict["final_10"] = final_scene_10
    loaded_dict["final_11"] = final_scene_11
    loaded_dict["final_12"] = final_scene_12
    loaded_dict["final_13"] = final_scene_13
    loaded_dict["final_14"] = final_scene_14
    loaded_dict["credits_1"] = credit_scene_1
    loaded_dict["credits_2"] = credit_scene_2
    loaded_dict["credits_3"] = credit_scene_3
    loaded_dict["credits_4"] = credit_scene_4
    loaded_dict["credits_5"] = credit_scene_5
    loaded_dict["water_player"] = water_player
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
    loaded_dict["reservoir_passage"] = reservoir_passage
    loaded_dict["reservoir_exit"] = reservoir_exit
    loaded_dict["reservoir_enter"] = reservoir_enter
    loaded_dict["korlok_hearth_screen"] = korlok_hearth_screen
    loaded_dict["mines_entrance"] = mines_entrance
    loaded_dict["korlok_mines"] = korlok_mines_screen
    loaded_dict["mines_wall"] = mines_wall
    loaded_dict["mines_light"] = mines_light
    loaded_dict["korlok_apothecary"] = korlok_apothecary
    loaded_dict["terra_mountains"] = terra_mountains
    loaded_dict["terra_cave"] = terra_cave
    loaded_dict["terra_trail_screen"] = terra_trail_screen
    loaded_dict["kart_overworld"] = kart_overworld
    loaded_dict["kart_full"] = kart_big_full
    loaded_dict["mirror_overlay"] = mirror_overlay
    loaded_dict["marrow_switch"] = m_switch
    loaded_dict["marrow_switch_blue"] = m_switch_b
    loaded_dict["marrow_switch_red"] = m_switch_r
    loaded_dict["marrow_switch_purple"] = m_switch_p
    loaded_dict["marrow_switch_complete"] = m_switch_c
    loaded_dict["marrow_switch_box"] = m_switch_box
    loaded_dict["popup_wide"] = popup_wide
    loaded_dict["marrow_ramparts_battle"] = ramparts_battle
    loaded_dict["marrow_tower_battle"] = tower_battle
    loaded_dict["overlay_enemy_vanish"] = overlay_enemy_vanish
    loaded_dict["overlay_stardust_star"] = overlay_stardust_star

    # sprite sheets ----------------------------------------------------------------------------------------------------
    # korlok interaction snowfall --------------------------------------------------------------------------------------
    popup_level_roles_url = resource_path('resources/art/popup_level_roles.png')
    popup_level_roles_sheet = sprite_sheet((270, 110), popup_level_roles_url)
    loaded_dict["mage_level_up"] = popup_level_roles_sheet[0]
    loaded_dict["fighter_level_up"] = popup_level_roles_sheet[1]
    loaded_dict["scout_level_up"] = popup_level_roles_sheet[2]
    # korlok interaction snowfall --------------------------------------------------------------------------------------
    korlok_interaction_snowfall_url = resource_path('resources/art/korlok_interaction_snowfall.png')
    korlok_interaction_snowfall_sheet = sprite_sheet((292, 172), korlok_interaction_snowfall_url)
    loaded_dict["korlok_snowfall_1"] = korlok_interaction_snowfall_sheet[0]
    loaded_dict["korlok_snowfall_2"] = korlok_interaction_snowfall_sheet[1]
    loaded_dict["korlok_snowfall_3"] = korlok_interaction_snowfall_sheet[2]
    # npc interaction quest stars --------------------------------------------------------------------------------------
    npc_interaction_stars_url = resource_path('resources/art/overlay_npc_interaction_stars.png')
    npc_interaction_stars_sheet = sprite_sheet((200, 200), npc_interaction_stars_url)
    loaded_dict["interaction_start_star"] = npc_interaction_stars_sheet[0]
    loaded_dict["interaction_progress_star"] = npc_interaction_stars_sheet[1]
    loaded_dict["interaction_complete_star"] = npc_interaction_stars_sheet[2]
    # condition overlays -----------------------------------------------------------------------------------------------
    overlay_conditions_url = resource_path('resources/art/overlay_conditions.png')
    overlay_conditions_sheet = sprite_sheet((25, 25), overlay_conditions_url)
    loaded_dict["overlay_burned"] = overlay_conditions_sheet[0]
    loaded_dict["overlay_poisoned"] = overlay_conditions_sheet[1]
    loaded_dict["overlay_bleeding"] = overlay_conditions_sheet[2]
    loaded_dict["overlay_crushed"] = overlay_conditions_sheet[3]
    # condition description overlays -----------------------------------------------------------------------------------
    overlay_condition_descriptions_url = resource_path('resources/art/overlay_condition_descriptions.png')
    overlay_condition_descriptions_sheet = sprite_sheet((100, 75), overlay_condition_descriptions_url)
    loaded_dict["overlay_burned_description"] = overlay_condition_descriptions_sheet[0]
    loaded_dict["overlay_poisoned_description"] = overlay_condition_descriptions_sheet[1]
    loaded_dict["overlay_bleeding_description"] = overlay_condition_descriptions_sheet[2]
    loaded_dict["overlay_crushed_description"] = overlay_condition_descriptions_sheet[3]
    # korlok_mountains -------------------------------------------------------------------------------------------------
    korlok_mountains_url = resource_path('resources/art/overlay_korlok_mountains.png')
    korlok_mountains_sheet = sprite_sheet((483, 136), korlok_mountains_url)
    loaded_dict["korlok_mountains"] = korlok_mountains_sheet[0]
    loaded_dict["korlok_mountains_1"] = korlok_mountains_sheet[1]
    loaded_dict["korlok_mountains_2"] = korlok_mountains_sheet[2]
    # message_box ------------------------------------------------------------------------------------------------------
    message_box_url = resource_path('resources/art/overlay_message_box.png')
    message_box_sheet = sprite_sheet((320, 110), message_box_url)
    loaded_dict["message_box_day"] = message_box_sheet[0]
    loaded_dict["message_box_dusk"] = message_box_sheet[1]
    loaded_dict["message_box_dawn"] = message_box_sheet[2]
    loaded_dict["message_box_night"] = message_box_sheet[3]
    # recycle crate overlay --------------------------------------------------------------------------------------------
    recycle_crate_overlay_url = resource_path('resources/art/overlay_recycle_crate.png')
    recycle_crate_overlay_sheet = sprite_sheet((200, 200), recycle_crate_overlay_url)
    loaded_dict["recycle_crate_overlay"] = recycle_crate_overlay_sheet[0]
    loaded_dict["recycle_crate_overlay_full"] = recycle_crate_overlay_sheet[1]
    # recycle crate ---------------------------------------------------------------------------------------------------
    recycle_crate_url = resource_path('resources/art/sprites_recycle_crates.png')
    recycle_crate_sheet = sprite_sheet((75, 75), recycle_crate_url)
    loaded_dict["recycle_crate"] = recycle_crate_sheet[0]
    loaded_dict["recycle_crate_full"] = recycle_crate_sheet[1]
    loaded_dict["construct_part"] = recycle_crate_sheet[2]
    loaded_dict["construct_part_high"] = recycle_crate_sheet[3]
    # quest district buttons -------------------------------------------------------------------------------------------
    quest_district_buttons_url = resource_path('resources/art/buttons_quest_district.png')
    quest_district_buttons_sheet = sprite_sheet((69, 32), quest_district_buttons_url)
    loaded_dict["seldon_district_button"] = quest_district_buttons_sheet[0]
    loaded_dict["korlok_district_button"] = quest_district_buttons_sheet[1]
    loaded_dict["eldream_district_button"] = quest_district_buttons_sheet[2]
    loaded_dict["marrow_district_button"] = quest_district_buttons_sheet[3]
    loaded_dict["district_button_highlight"] = quest_district_buttons_sheet[4]
    loaded_dict["district_button_select"] = quest_district_buttons_sheet[5]
    # muchador crate ---------------------------------------------------------------------------------------------------
    muchador_crate_url = resource_path('resources/art/overlay_muchador_crate.png')
    muchador_crate_sheet = sprite_sheet((125, 125), muchador_crate_url)
    loaded_dict["muchador_crate"] = muchador_crate_sheet[0]
    loaded_dict["muchador_crate_top"] = muchador_crate_sheet[1]
    # extra inventory buttons ------------------------------------------------------------------------------------------
    extra_buttons_url = resource_path('resources/art/overlay_extra_inventory_buttons.png')
    extra_buttons_sheet = sprite_sheet((50, 50), extra_buttons_url)
    loaded_dict["kasper_button"] = extra_buttons_sheet[0]
    loaded_dict["torok_button"] = extra_buttons_sheet[1]
    loaded_dict["iriana_button"] = extra_buttons_sheet[2]
    loaded_dict["nera's_grace"] = extra_buttons_sheet[3]
    loaded_dict["aren's_strength"] = extra_buttons_sheet[4]
    loaded_dict["wisdom's_spirit"] = extra_buttons_sheet[5]
    loaded_dict["extra_inventory_high"] = extra_buttons_sheet[6]
    # arrow skill overlays ---------------------------------------------------------------------------------------------
    skill_tier_three_url = resource_path('resources/art/overlay_skills_tier_three.png')
    skill_tier_three_sheet = sprite_sheet((700, 700), skill_tier_three_url)
    loaded_dict["skill_arrow"] = skill_tier_three_sheet[0]
    loaded_dict["skill_arrow_advantage"] = skill_tier_three_sheet[1]
    loaded_dict["millennium_fire"] = skill_tier_three_sheet[2]
    loaded_dict["epsilon's_edge"] = skill_tier_three_sheet[3]
    loaded_dict["transpose_1"] = skill_tier_three_sheet[4]
    loaded_dict["transpose_2"] = skill_tier_three_sheet[5]
    loaded_dict["transpose_3"] = skill_tier_three_sheet[6]
    # card trade button ------------------------------------------------------------------------------------------------
    card_trade_button_url = resource_path('resources/art/button_trade.png')
    card_trade_button_sheet = sprite_sheet((111, 30), card_trade_button_url)
    loaded_dict["trading_button"] = card_trade_button_sheet[0]
    loaded_dict["trading_button_high"] = card_trade_button_sheet[1]
    # marrow cat -------------------------------------------------------------------------------------------------------
    marrow_cat_url = resource_path('resources/art/sprite_cat_marrow.png')
    marrow_cat_sheet = sprite_sheet((100, 100), marrow_cat_url)
    loaded_dict["marrow_cat"] = marrow_cat_sheet[0]
    loaded_dict["marrow_cat_pet"] = marrow_cat_sheet[1]
    # dreth sprites ----------------------------------------------------------------------------------------------------
    dreths_url = resource_path('resources/art/sprites_dreth.png')
    dreths_sheet = sprite_sheet((500, 500), dreths_url)
    loaded_dict["sprite_dreth"] = dreths_sheet[0]
    loaded_dict["dreth_battle"] = dreths_sheet[1]
    loaded_dict["dreth_attack"] = dreths_sheet[2]
    loaded_dict["dreth_shatter"] = dreths_sheet[3]
    loaded_dict["dreth_battle_2"] = dreths_sheet[4]
    loaded_dict["dreth_attack_2"] = dreths_sheet[5]
    loaded_dict["dreth_shatter_2"] = dreths_sheet[6]
    # mirages ----------------------------------------------------------------------------------------------------------
    mirages_url = resource_path('resources/art/sprites_mirages.png')
    mirages_sheet = sprite_sheet((50, 75), mirages_url)
    loaded_dict["mirage_female"] = mirages_sheet[0]
    loaded_dict["mirage_male"] = mirages_sheet[1]
    # dreth taunt popups -----------------------------------------------------------------------------------------------
    dreth_taunts_url = resource_path('resources/art/dreth_taunts.png')
    dreth_taunts_sheet = sprite_sheet((400, 200), dreth_taunts_url)
    loaded_dict["dreth_taunt_1"] = dreth_taunts_sheet[0]
    loaded_dict["dreth_taunt_2"] = dreth_taunts_sheet[1]
    loaded_dict["dreth_taunt_3"] = dreth_taunts_sheet[2]
    loaded_dict["dreth_taunt_4"] = dreth_taunts_sheet[3]
    # marrow castle chandelier -----------------------------------------------------------------------------------------
    chandelier_url = resource_path('resources/art/overlay_chandelier.png')
    chandelier_sheet = sprite_sheet((1027, 200), chandelier_url)
    loaded_dict["chandelier_full"] = chandelier_sheet[0]
    loaded_dict["chandelier_right"] = chandelier_sheet[1]
    loaded_dict["chandelier_left"] = chandelier_sheet[2]
    loaded_dict["chandelier_broken"] = chandelier_sheet[3]
    # marrow castle bridge ---------------------------------------------------------------------------------------------
    castle_bridge_url = resource_path('resources/art/overlay_marrow_castle_bridge.png')
    castle_bridge_sheet = sprite_sheet((150, 150), castle_bridge_url)
    loaded_dict["castle_bridge_unfinished"] = castle_bridge_sheet[0]
    loaded_dict["castle_bridge_finished"] = castle_bridge_sheet[1]
    # fishing popups ---------------------------------------------------------------------------------------------------
    fish_popups_url = resource_path('resources/art/popup_fishing_fish.png')
    fish_popups_sheet = sprite_sheet((250, 150), fish_popups_url)
    loaded_dict["basic_fish_popup"] = fish_popups_sheet[0]
    loaded_dict["better_fish_popup"] = fish_popups_sheet[1]
    loaded_dict["best_fish_popup"] = fish_popups_sheet[2]
    loaded_dict["very_best_fish_popup"] = fish_popups_sheet[3]
    # seldon fireworks -------------------------------------------------------------------------------------------------
    seldon_fireworks_url = resource_path('resources/art/overlay_fireworks_seldon.png')
    seldon_fireworks_sheet = sprite_sheet((200, 300), seldon_fireworks_url)
    loaded_dict["seldon_fireworks_1"] = seldon_fireworks_sheet[0]
    loaded_dict["seldon_fireworks_2"] = seldon_fireworks_sheet[1]
    loaded_dict["seldon_fireworks_3"] = seldon_fireworks_sheet[2]
    loaded_dict["seldon_fireworks_4"] = seldon_fireworks_sheet[3]
    # korlok fireworks -------------------------------------------------------------------------------------------------
    korlok_fireworks_url = resource_path('resources/art/overlay_fireworks_korlok.png')
    korlok_fireworks_sheet = sprite_sheet((200, 300), korlok_fireworks_url)
    loaded_dict["korlok_fireworks_1"] = korlok_fireworks_sheet[0]
    loaded_dict["korlok_fireworks_2"] = korlok_fireworks_sheet[1]
    loaded_dict["korlok_fireworks_3"] = korlok_fireworks_sheet[2]
    loaded_dict["korlok_fireworks_4"] = korlok_fireworks_sheet[3]
    # eldream fireworks ------------------------------------------------------------------------------------------------
    eldream_fireworks_url = resource_path('resources/art/overlay_fireworks_eldream.png')
    eldream_fireworks_sheet = sprite_sheet((200, 300), eldream_fireworks_url)
    loaded_dict["eldream_fireworks_1"] = eldream_fireworks_sheet[0]
    loaded_dict["eldream_fireworks_2"] = eldream_fireworks_sheet[1]
    loaded_dict["eldream_fireworks_3"] = eldream_fireworks_sheet[2]
    loaded_dict["eldream_fireworks_4"] = eldream_fireworks_sheet[3]
    # create character screen character race selections ----------------------------------------------------------------
    character_selections_url = resource_path('resources/art/overlay_character_selections.png')
    character_selections_sheet = sprite_sheet((250, 350), character_selections_url)
    loaded_dict["amuna_male_character_img"] = character_selections_sheet[0]
    loaded_dict["amuna_female_character_img"] = character_selections_sheet[1]
    loaded_dict["nuldar_male_character_img"] = character_selections_sheet[2]
    loaded_dict["nuldar_female_character_img"] = character_selections_sheet[3]
    loaded_dict["sorae_a_character_img"] = character_selections_sheet[4]
    loaded_dict["sorae_b_character_img"] = character_selections_sheet[5]
    # player character cutscene overlays -------------------------------------------------------------------------------
    player_cutscene_url = resource_path('resources/art/overlay_player_cutscene.png')
    player_cutscene_sheet = sprite_sheet((90, 160), player_cutscene_url)
    loaded_dict["amuna_cutscene"] = player_cutscene_sheet[0]
    loaded_dict["nuldar_cutscene"] = player_cutscene_sheet[1]
    loaded_dict["sorae_cutscene"] = player_cutscene_sheet[2]
    loaded_dict["amuna_cutscene_female"] = player_cutscene_sheet[3]
    loaded_dict["nuldar_cutscene_female"] = player_cutscene_sheet[4]
    loaded_dict["sorae_cutscene_beta"] = player_cutscene_sheet[5]
    # player character night cutscene overlays -------------------------------------------------------------------------
    player_cutscene_night_url = resource_path('resources/art/overlay_player_cutscene_night.png')
    player_cutscene_night_sheet = sprite_sheet((90, 160), player_cutscene_night_url)
    loaded_dict["amuna_cutscene_night"] = player_cutscene_night_sheet[0]
    loaded_dict["nuldar_cutscene_night"] = player_cutscene_night_sheet[1]
    loaded_dict["sorae_cutscene_night"] = player_cutscene_night_sheet[2]
    loaded_dict["amuna_cutscene_female_night"] = player_cutscene_night_sheet[3]
    loaded_dict["nuldar_cutscene_female_night"] = player_cutscene_night_sheet[4]
    loaded_dict["sorae_cutscene_beta_night"] = player_cutscene_night_sheet[5]
    # player character cutscene overlays 2 -----------------------------------------------------------------------------
    player_cutscene_2_url = resource_path('resources/art/overlay_player_cutscene_2.png')
    player_cutscene_2_sheet = sprite_sheet((500, 668), player_cutscene_2_url)
    loaded_dict["amuna_cutscene_2"] = player_cutscene_2_sheet[0]
    loaded_dict["nuldar_cutscene_2"] = player_cutscene_2_sheet[1]
    loaded_dict["sorae_cutscene_2"] = player_cutscene_2_sheet[2]
    loaded_dict["amuna_cutscene_2_female"] = player_cutscene_2_sheet[3]
    loaded_dict["nuldar_cutscene_2_female"] = player_cutscene_2_sheet[4]
    loaded_dict["sorae_cutscene_2_beta"] = player_cutscene_2_sheet[5]
    # player character cutscene overlays 2 night -----------------------------------------------------------------------
    player_cutscene_2_night_url = resource_path('resources/art/overlay_player_cutscene_2_night.png')
    player_cutscene_2_night_sheet = sprite_sheet((500, 668), player_cutscene_2_night_url)
    loaded_dict["amuna_cutscene_2_night"] = player_cutscene_2_night_sheet[0]
    loaded_dict["nuldar_cutscene_2_night"] = player_cutscene_2_night_sheet[1]
    loaded_dict["sorae_cutscene_2_night"] = player_cutscene_2_night_sheet[2]
    loaded_dict["amuna_cutscene_2_female_night"] = player_cutscene_2_night_sheet[3]
    loaded_dict["nuldar_cutscene_2_female_night"] = player_cutscene_2_night_sheet[4]
    loaded_dict["sorae_cutscene_2_beta_night"] = player_cutscene_2_night_sheet[5]
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
    # male -------------------------------------------------------------------------------------------------------------
    player_no_role_amuna_male_down_url = resource_path('resources/art/player_no_role_amuna_down_male.png')
    player_no_role_amuna_male_down_sheet = sprite_sheet((50, 75), player_no_role_amuna_male_down_url)
    loaded_dict["player_no_role_amuna_male_down_1"] = player_no_role_amuna_male_down_sheet[0]
    loaded_dict["player_no_role_amuna_male_down_2"] = player_no_role_amuna_male_down_sheet[1]
    loaded_dict["player_no_role_amuna_male_down_3"] = player_no_role_amuna_male_down_sheet[2]
    loaded_dict["player_no_role_amuna_male_down_4"] = player_no_role_amuna_male_down_sheet[3]
    player_no_role_amuna_male_up_url = resource_path('resources/art/player_no_role_amuna_up_male.png')
    player_no_role_amuna_male_up_sheet = sprite_sheet((50, 75), player_no_role_amuna_male_up_url)
    loaded_dict["player_no_role_amuna_male_up_1"] = player_no_role_amuna_male_up_sheet[0]
    loaded_dict["player_no_role_amuna_male_up_2"] = player_no_role_amuna_male_up_sheet[1]
    loaded_dict["player_no_role_amuna_male_up_3"] = player_no_role_amuna_male_up_sheet[2]
    loaded_dict["player_no_role_amuna_male_up_4"] = player_no_role_amuna_male_up_sheet[3]
    player_no_role_amuna_male_left_url = resource_path('resources/art/player_no_role_amuna_left_male.png')
    player_no_role_amuna_male_left_sheet = sprite_sheet((50, 75), player_no_role_amuna_male_left_url)
    loaded_dict["player_no_role_amuna_male_left_1"] = player_no_role_amuna_male_left_sheet[0]
    loaded_dict["player_no_role_amuna_male_left_2"] = player_no_role_amuna_male_left_sheet[1]
    loaded_dict["player_no_role_amuna_male_left_3"] = player_no_role_amuna_male_left_sheet[2]
    loaded_dict["player_no_role_amuna_male_left_4"] = player_no_role_amuna_male_left_sheet[3]
    player_no_role_amuna_male_right_url = resource_path('resources/art/player_no_role_amuna_right_male.png')
    player_no_role_amuna_male_right_sheet = sprite_sheet((50, 75), player_no_role_amuna_male_right_url)
    loaded_dict["player_no_role_amuna_male_right_1"] = player_no_role_amuna_male_right_sheet[0]
    loaded_dict["player_no_role_amuna_male_right_2"] = player_no_role_amuna_male_right_sheet[1]
    loaded_dict["player_no_role_amuna_male_right_3"] = player_no_role_amuna_male_right_sheet[2]
    loaded_dict["player_no_role_amuna_male_right_4"] = player_no_role_amuna_male_right_sheet[3]
    # female -----------------------------------------------------------------------------------------------------------
    player_no_role_amuna_female_down_url = resource_path('resources/art/player_no_role_amuna_down_female.png')
    player_no_role_amuna_female_down_sheet = sprite_sheet((50, 75), player_no_role_amuna_female_down_url)
    loaded_dict["player_no_role_amuna_female_down_1"] = player_no_role_amuna_female_down_sheet[0]
    loaded_dict["player_no_role_amuna_female_down_2"] = player_no_role_amuna_female_down_sheet[1]
    loaded_dict["player_no_role_amuna_female_down_3"] = player_no_role_amuna_female_down_sheet[2]
    loaded_dict["player_no_role_amuna_female_down_4"] = player_no_role_amuna_female_down_sheet[3]
    player_no_role_amuna_female_up_url = resource_path('resources/art/player_no_role_amuna_up_female.png')
    player_no_role_amuna_female_up_sheet = sprite_sheet((50, 75), player_no_role_amuna_female_up_url)
    loaded_dict["player_no_role_amuna_female_up_1"] = player_no_role_amuna_female_up_sheet[0]
    loaded_dict["player_no_role_amuna_female_up_2"] = player_no_role_amuna_female_up_sheet[1]
    loaded_dict["player_no_role_amuna_female_up_3"] = player_no_role_amuna_female_up_sheet[2]
    loaded_dict["player_no_role_amuna_female_up_4"] = player_no_role_amuna_female_up_sheet[3]
    player_no_role_amuna_female_left_url = resource_path('resources/art/player_no_role_amuna_left_female.png')
    player_no_role_amuna_female_left_sheet = sprite_sheet((50, 75), player_no_role_amuna_female_left_url)
    loaded_dict["player_no_role_amuna_female_left_1"] = player_no_role_amuna_female_left_sheet[0]
    loaded_dict["player_no_role_amuna_female_left_2"] = player_no_role_amuna_female_left_sheet[1]
    loaded_dict["player_no_role_amuna_female_left_3"] = player_no_role_amuna_female_left_sheet[2]
    loaded_dict["player_no_role_amuna_female_left_4"] = player_no_role_amuna_female_left_sheet[3]
    player_no_role_amuna_female_right_url = resource_path('resources/art/player_no_role_amuna_right_female.png')
    player_no_role_amuna_female_right_sheet = sprite_sheet((50, 75), player_no_role_amuna_female_right_url)
    loaded_dict["player_no_role_amuna_female_right_1"] = player_no_role_amuna_female_right_sheet[0]
    loaded_dict["player_no_role_amuna_female_right_2"] = player_no_role_amuna_female_right_sheet[1]
    loaded_dict["player_no_role_amuna_female_right_3"] = player_no_role_amuna_female_right_sheet[2]
    loaded_dict["player_no_role_amuna_female_right_4"] = player_no_role_amuna_female_right_sheet[3]
    # player no role sorae race ----------------------------------------------------------------------------------------
    # alpha ------------------------------------------------------------------------------------------------------------
    player_no_role_sorae_a_down_url = resource_path('resources/art/player_no_role_sorae_down_a.png')
    player_no_role_sorae_a_down_sheet = sprite_sheet((50, 75), player_no_role_sorae_a_down_url)
    loaded_dict["player_no_role_sorae_a_down_1"] = player_no_role_sorae_a_down_sheet[0]
    loaded_dict["player_no_role_sorae_a_down_2"] = player_no_role_sorae_a_down_sheet[1]
    loaded_dict["player_no_role_sorae_a_down_3"] = player_no_role_sorae_a_down_sheet[2]
    loaded_dict["player_no_role_sorae_a_down_4"] = player_no_role_sorae_a_down_sheet[3]
    player_no_role_sorae_a_up_url = resource_path('resources/art/player_no_role_sorae_up_a.png')
    player_no_role_sorae_a_up_sheet = sprite_sheet((50, 75), player_no_role_sorae_a_up_url)
    loaded_dict["player_no_role_sorae_a_up_1"] = player_no_role_sorae_a_up_sheet[0]
    loaded_dict["player_no_role_sorae_a_up_2"] = player_no_role_sorae_a_up_sheet[1]
    loaded_dict["player_no_role_sorae_a_up_3"] = player_no_role_sorae_a_up_sheet[2]
    loaded_dict["player_no_role_sorae_a_up_4"] = player_no_role_sorae_a_up_sheet[3]
    player_no_role_sorae_a_left_url = resource_path('resources/art/player_no_role_sorae_left_a.png')
    player_no_role_sorae_a_left_sheet = sprite_sheet((50, 75), player_no_role_sorae_a_left_url)
    loaded_dict["player_no_role_sorae_a_left_1"] = player_no_role_sorae_a_left_sheet[0]
    loaded_dict["player_no_role_sorae_a_left_2"] = player_no_role_sorae_a_left_sheet[1]
    loaded_dict["player_no_role_sorae_a_left_3"] = player_no_role_sorae_a_left_sheet[2]
    loaded_dict["player_no_role_sorae_a_left_4"] = player_no_role_sorae_a_left_sheet[3]
    player_no_role_sorae_a_right_url = resource_path('resources/art/player_no_role_sorae_right_a.png')
    player_no_role_sorae_a_right_sheet = sprite_sheet((50, 75), player_no_role_sorae_a_right_url)
    loaded_dict["player_no_role_sorae_a_right_1"] = player_no_role_sorae_a_right_sheet[0]
    loaded_dict["player_no_role_sorae_a_right_2"] = player_no_role_sorae_a_right_sheet[1]
    loaded_dict["player_no_role_sorae_a_right_3"] = player_no_role_sorae_a_right_sheet[2]
    loaded_dict["player_no_role_sorae_a_right_4"] = player_no_role_sorae_a_right_sheet[3]
    # beta -------------------------------------------------------------------------------------------------------------
    player_no_role_sorae_b_down_url = resource_path('resources/art/player_no_role_sorae_down_b.png')
    player_no_role_sorae_b_down_sheet = sprite_sheet((50, 75), player_no_role_sorae_b_down_url)
    loaded_dict["player_no_role_sorae_b_down_1"] = player_no_role_sorae_b_down_sheet[0]
    loaded_dict["player_no_role_sorae_b_down_2"] = player_no_role_sorae_b_down_sheet[1]
    loaded_dict["player_no_role_sorae_b_down_3"] = player_no_role_sorae_b_down_sheet[2]
    loaded_dict["player_no_role_sorae_b_down_4"] = player_no_role_sorae_b_down_sheet[3]
    player_no_role_sorae_b_up_url = resource_path('resources/art/player_no_role_sorae_up_b.png')
    player_no_role_sorae_b_up_sheet = sprite_sheet((50, 75), player_no_role_sorae_b_up_url)
    loaded_dict["player_no_role_sorae_b_up_1"] = player_no_role_sorae_b_up_sheet[0]
    loaded_dict["player_no_role_sorae_b_up_2"] = player_no_role_sorae_b_up_sheet[1]
    loaded_dict["player_no_role_sorae_b_up_3"] = player_no_role_sorae_b_up_sheet[2]
    loaded_dict["player_no_role_sorae_b_up_4"] = player_no_role_sorae_b_up_sheet[3]
    player_no_role_sorae_b_left_url = resource_path('resources/art/player_no_role_sorae_left_b.png')
    player_no_role_sorae_b_left_sheet = sprite_sheet((50, 75), player_no_role_sorae_b_left_url)
    loaded_dict["player_no_role_sorae_b_left_1"] = player_no_role_sorae_b_left_sheet[0]
    loaded_dict["player_no_role_sorae_b_left_2"] = player_no_role_sorae_b_left_sheet[1]
    loaded_dict["player_no_role_sorae_b_left_3"] = player_no_role_sorae_b_left_sheet[2]
    loaded_dict["player_no_role_sorae_b_left_4"] = player_no_role_sorae_b_left_sheet[3]
    player_no_role_sorae_b_right_url = resource_path('resources/art/player_no_role_sorae_right_b.png')
    player_no_role_sorae_b_right_sheet = sprite_sheet((50, 75), player_no_role_sorae_b_right_url)
    loaded_dict["player_no_role_sorae_b_right_1"] = player_no_role_sorae_b_right_sheet[0]
    loaded_dict["player_no_role_sorae_b_right_2"] = player_no_role_sorae_b_right_sheet[1]
    loaded_dict["player_no_role_sorae_b_right_3"] = player_no_role_sorae_b_right_sheet[2]
    loaded_dict["player_no_role_sorae_b_right_4"] = player_no_role_sorae_b_right_sheet[3]
    # player no role nuldar race ---------------------------------------------------------------------------------------
    # male -------------------------------------------------------------------------------------------------------------
    player_no_role_nuldar_male_down_url = resource_path('resources/art/player_no_role_nuldar_down_male.png')
    player_no_role_nuldar_male_down_sheet = sprite_sheet((50, 75), player_no_role_nuldar_male_down_url)
    loaded_dict["player_no_role_nuldar_male_down_1"] = player_no_role_nuldar_male_down_sheet[0]
    loaded_dict["player_no_role_nuldar_male_down_2"] = player_no_role_nuldar_male_down_sheet[1]
    loaded_dict["player_no_role_nuldar_male_down_3"] = player_no_role_nuldar_male_down_sheet[2]
    loaded_dict["player_no_role_nuldar_male_down_4"] = player_no_role_nuldar_male_down_sheet[3]
    player_no_role_nuldar_male_up_url = resource_path('resources/art/player_no_role_nuldar_up_male.png')
    player_no_role_nuldar_male_up_sheet = sprite_sheet((50, 75), player_no_role_nuldar_male_up_url)
    loaded_dict["player_no_role_nuldar_male_up_1"] = player_no_role_nuldar_male_up_sheet[0]
    loaded_dict["player_no_role_nuldar_male_up_2"] = player_no_role_nuldar_male_up_sheet[1]
    loaded_dict["player_no_role_nuldar_male_up_3"] = player_no_role_nuldar_male_up_sheet[2]
    loaded_dict["player_no_role_nuldar_male_up_4"] = player_no_role_nuldar_male_up_sheet[3]
    player_no_role_nuldar_male_left_url = resource_path('resources/art/player_no_role_nuldar_left_male.png')
    player_no_role_nuldar_male_left_sheet = sprite_sheet((50, 75), player_no_role_nuldar_male_left_url)
    loaded_dict["player_no_role_nuldar_male_left_1"] = player_no_role_nuldar_male_left_sheet[0]
    loaded_dict["player_no_role_nuldar_male_left_2"] = player_no_role_nuldar_male_left_sheet[1]
    loaded_dict["player_no_role_nuldar_male_left_3"] = player_no_role_nuldar_male_left_sheet[2]
    loaded_dict["player_no_role_nuldar_male_left_4"] = player_no_role_nuldar_male_left_sheet[3]
    player_no_role_nuldar_male_right_url = resource_path('resources/art/player_no_role_nuldar_right_male.png')
    player_no_role_nuldar_male_right_sheet = sprite_sheet((50, 75), player_no_role_nuldar_male_right_url)
    loaded_dict["player_no_role_nuldar_male_right_1"] = player_no_role_nuldar_male_right_sheet[0]
    loaded_dict["player_no_role_nuldar_male_right_2"] = player_no_role_nuldar_male_right_sheet[1]
    loaded_dict["player_no_role_nuldar_male_right_3"] = player_no_role_nuldar_male_right_sheet[2]
    loaded_dict["player_no_role_nuldar_male_right_4"] = player_no_role_nuldar_male_right_sheet[3]
    # female -----------------------------------------------------------------------------------------------------------
    player_no_role_nuldar_male_down_url = resource_path('resources/art/player_no_role_nuldar_down_female.png')
    player_no_role_nuldar_male_down_sheet = sprite_sheet((50, 75), player_no_role_nuldar_male_down_url)
    loaded_dict["player_no_role_nuldar_female_down_1"] = player_no_role_nuldar_male_down_sheet[0]
    loaded_dict["player_no_role_nuldar_female_down_2"] = player_no_role_nuldar_male_down_sheet[1]
    loaded_dict["player_no_role_nuldar_female_down_3"] = player_no_role_nuldar_male_down_sheet[2]
    loaded_dict["player_no_role_nuldar_female_down_4"] = player_no_role_nuldar_male_down_sheet[3]
    player_no_role_nuldar_male_up_url = resource_path('resources/art/player_no_role_nuldar_up_female.png')
    player_no_role_nuldar_male_up_sheet = sprite_sheet((50, 75), player_no_role_nuldar_male_up_url)
    loaded_dict["player_no_role_nuldar_female_up_1"] = player_no_role_nuldar_male_up_sheet[0]
    loaded_dict["player_no_role_nuldar_female_up_2"] = player_no_role_nuldar_male_up_sheet[1]
    loaded_dict["player_no_role_nuldar_female_up_3"] = player_no_role_nuldar_male_up_sheet[2]
    loaded_dict["player_no_role_nuldar_female_up_4"] = player_no_role_nuldar_male_up_sheet[3]
    player_no_role_nuldar_male_left_url = resource_path('resources/art/player_no_role_nuldar_left_female.png')
    player_no_role_nuldar_male_left_sheet = sprite_sheet((50, 75), player_no_role_nuldar_male_left_url)
    loaded_dict["player_no_role_nuldar_female_left_1"] = player_no_role_nuldar_male_left_sheet[0]
    loaded_dict["player_no_role_nuldar_female_left_2"] = player_no_role_nuldar_male_left_sheet[1]
    loaded_dict["player_no_role_nuldar_female_left_3"] = player_no_role_nuldar_male_left_sheet[2]
    loaded_dict["player_no_role_nuldar_female_left_4"] = player_no_role_nuldar_male_left_sheet[3]
    player_no_role_nuldar_male_right_url = resource_path('resources/art/player_no_role_nuldar_right_female.png')
    player_no_role_nuldar_male_right_sheet = sprite_sheet((50, 75), player_no_role_nuldar_male_right_url)
    loaded_dict["player_no_role_nuldar_female_right_1"] = player_no_role_nuldar_male_right_sheet[0]
    loaded_dict["player_no_role_nuldar_female_right_2"] = player_no_role_nuldar_male_right_sheet[1]
    loaded_dict["player_no_role_nuldar_female_right_3"] = player_no_role_nuldar_male_right_sheet[2]
    loaded_dict["player_no_role_nuldar_female_right_4"] = player_no_role_nuldar_male_right_sheet[3]

    # player mage amuna race -------------------------------------------------------------------------------------------
    # male -------------------------------------------------------------------------------------------------------------
    player_mage_amuna_down_url = resource_path('resources/art/player_mage_amuna_down_male.png')
    player_mage_amuna_down_sheet = sprite_sheet((50, 75), player_mage_amuna_down_url)
    loaded_dict["player_mage_amuna_male_down_1"] = player_mage_amuna_down_sheet[0]
    loaded_dict["player_mage_amuna_male_down_2"] = player_mage_amuna_down_sheet[1]
    loaded_dict["player_mage_amuna_male_down_3"] = player_mage_amuna_down_sheet[2]
    loaded_dict["player_mage_amuna_male_down_4"] = player_mage_amuna_down_sheet[3]
    # basic
    player_mage_amuna_down_basic_url = resource_path('resources/art/player_mage_amuna_down_male_basic.png')
    player_mage_amuna_down_basic_sheet = sprite_sheet((50, 75), player_mage_amuna_down_basic_url)
    loaded_dict["player_mage_amuna_male_down_1_basic"] = player_mage_amuna_down_basic_sheet[0]
    loaded_dict["player_mage_amuna_male_down_2_basic"] = player_mage_amuna_down_basic_sheet[1]
    loaded_dict["player_mage_amuna_male_down_3_basic"] = player_mage_amuna_down_basic_sheet[2]
    loaded_dict["player_mage_amuna_male_down_4_basic"] = player_mage_amuna_down_basic_sheet[3]
    # forged
    player_mage_amuna_down_forged_url = resource_path('resources/art/player_mage_amuna_down_male_forged.png')
    player_mage_amuna_down_forged_sheet = sprite_sheet((50, 75), player_mage_amuna_down_forged_url)
    loaded_dict["player_mage_amuna_male_down_1_forged"] = player_mage_amuna_down_forged_sheet[0]
    loaded_dict["player_mage_amuna_male_down_2_forged"] = player_mage_amuna_down_forged_sheet[1]
    loaded_dict["player_mage_amuna_male_down_3_forged"] = player_mage_amuna_down_forged_sheet[2]
    loaded_dict["player_mage_amuna_male_down_4_forged"] = player_mage_amuna_down_forged_sheet[3]
    # mythic
    player_mage_amuna_down_mythic_url = resource_path('resources/art/player_mage_amuna_down_male_mythic.png')
    player_mage_amuna_down_mythic_sheet = sprite_sheet((50, 75), player_mage_amuna_down_mythic_url)
    loaded_dict["player_mage_amuna_male_down_1_mythic"] = player_mage_amuna_down_mythic_sheet[0]
    loaded_dict["player_mage_amuna_male_down_2_mythic"] = player_mage_amuna_down_mythic_sheet[1]
    loaded_dict["player_mage_amuna_male_down_3_mythic"] = player_mage_amuna_down_mythic_sheet[2]
    loaded_dict["player_mage_amuna_male_down_4_mythic"] = player_mage_amuna_down_mythic_sheet[3]
    # legend
    player_mage_amuna_down_legend_url = resource_path('resources/art/player_mage_amuna_down_male_legend.png')
    player_mage_amuna_down_legend_sheet = sprite_sheet((50, 75), player_mage_amuna_down_legend_url)
    loaded_dict["player_mage_amuna_male_down_1_legend"] = player_mage_amuna_down_legend_sheet[0]
    loaded_dict["player_mage_amuna_male_down_2_legend"] = player_mage_amuna_down_legend_sheet[1]
    loaded_dict["player_mage_amuna_male_down_3_legend"] = player_mage_amuna_down_legend_sheet[2]
    loaded_dict["player_mage_amuna_male_down_4_legend"] = player_mage_amuna_down_legend_sheet[3]
    player_mage_amuna_up_url = resource_path('resources/art/player_mage_amuna_up_male.png')
    player_mage_amuna_up_sheet = sprite_sheet((50, 75), player_mage_amuna_up_url)
    loaded_dict["player_mage_amuna_male_up_1"] = player_mage_amuna_up_sheet[0]
    loaded_dict["player_mage_amuna_male_up_2"] = player_mage_amuna_up_sheet[1]
    loaded_dict["player_mage_amuna_male_up_3"] = player_mage_amuna_up_sheet[2]
    loaded_dict["player_mage_amuna_male_up_4"] = player_mage_amuna_up_sheet[3]
    # basic
    player_mage_amuna_up_basic_url = resource_path('resources/art/player_mage_amuna_up_male_basic.png')
    player_mage_amuna_up_basic_sheet = sprite_sheet((50, 75), player_mage_amuna_up_basic_url)
    loaded_dict["player_mage_amuna_male_up_1_basic"] = player_mage_amuna_up_basic_sheet[0]
    loaded_dict["player_mage_amuna_male_up_2_basic"] = player_mage_amuna_up_basic_sheet[1]
    loaded_dict["player_mage_amuna_male_up_3_basic"] = player_mage_amuna_up_basic_sheet[2]
    loaded_dict["player_mage_amuna_male_up_4_basic"] = player_mage_amuna_up_basic_sheet[3]
    # forged
    player_mage_amuna_up_forged_url = resource_path('resources/art/player_mage_amuna_up_male_forged.png')
    player_mage_amuna_up_forged_sheet = sprite_sheet((50, 75), player_mage_amuna_up_forged_url)
    loaded_dict["player_mage_amuna_male_up_1_forged"] = player_mage_amuna_up_forged_sheet[0]
    loaded_dict["player_mage_amuna_male_up_2_forged"] = player_mage_amuna_up_forged_sheet[1]
    loaded_dict["player_mage_amuna_male_up_3_forged"] = player_mage_amuna_up_forged_sheet[2]
    loaded_dict["player_mage_amuna_male_up_4_forged"] = player_mage_amuna_up_forged_sheet[3]
    # mythic
    player_mage_amuna_up_mythic_url = resource_path('resources/art/player_mage_amuna_up_male_mythic.png')
    player_mage_amuna_up_mythic_sheet = sprite_sheet((50, 75), player_mage_amuna_up_mythic_url)
    loaded_dict["player_mage_amuna_male_up_1_mythic"] = player_mage_amuna_up_mythic_sheet[0]
    loaded_dict["player_mage_amuna_male_up_2_mythic"] = player_mage_amuna_up_mythic_sheet[1]
    loaded_dict["player_mage_amuna_male_up_3_mythic"] = player_mage_amuna_up_mythic_sheet[2]
    loaded_dict["player_mage_amuna_male_up_4_mythic"] = player_mage_amuna_up_mythic_sheet[3]
    # legend
    player_mage_amuna_up_legend_url = resource_path('resources/art/player_mage_amuna_up_male_legend.png')
    player_mage_amuna_up_legend_sheet = sprite_sheet((50, 75), player_mage_amuna_up_legend_url)
    loaded_dict["player_mage_amuna_male_up_1_legend"] = player_mage_amuna_up_legend_sheet[0]
    loaded_dict["player_mage_amuna_male_up_2_legend"] = player_mage_amuna_up_legend_sheet[1]
    loaded_dict["player_mage_amuna_male_up_3_legend"] = player_mage_amuna_up_legend_sheet[2]
    loaded_dict["player_mage_amuna_male_up_4_legend"] = player_mage_amuna_up_legend_sheet[3]
    player_mage_amuna_left_url = resource_path('resources/art/player_mage_amuna_left_male.png')
    player_mage_amuna_left_sheet = sprite_sheet((50, 75), player_mage_amuna_left_url)
    loaded_dict["player_mage_amuna_male_left_1"] = player_mage_amuna_left_sheet[0]
    loaded_dict["player_mage_amuna_male_left_2"] = player_mage_amuna_left_sheet[1]
    loaded_dict["player_mage_amuna_male_left_3"] = player_mage_amuna_left_sheet[2]
    loaded_dict["player_mage_amuna_male_left_4"] = player_mage_amuna_left_sheet[3]
    # basic
    player_mage_amuna_left_basic_url = resource_path('resources/art/player_mage_amuna_left_male_basic.png')
    player_mage_amuna_left_basic_sheet = sprite_sheet((50, 75), player_mage_amuna_left_basic_url)
    loaded_dict["player_mage_amuna_male_left_1_basic"] = player_mage_amuna_left_basic_sheet[0]
    loaded_dict["player_mage_amuna_male_left_2_basic"] = player_mage_amuna_left_basic_sheet[1]
    loaded_dict["player_mage_amuna_male_left_3_basic"] = player_mage_amuna_left_basic_sheet[2]
    loaded_dict["player_mage_amuna_male_left_4_basic"] = player_mage_amuna_left_basic_sheet[3]
    # forged
    player_mage_amuna_left_forged_url = resource_path('resources/art/player_mage_amuna_left_male_forged.png')
    player_mage_amuna_left_forged_sheet = sprite_sheet((50, 75), player_mage_amuna_left_forged_url)
    loaded_dict["player_mage_amuna_male_left_1_forged"] = player_mage_amuna_left_forged_sheet[0]
    loaded_dict["player_mage_amuna_male_left_2_forged"] = player_mage_amuna_left_forged_sheet[1]
    loaded_dict["player_mage_amuna_male_left_3_forged"] = player_mage_amuna_left_forged_sheet[2]
    loaded_dict["player_mage_amuna_male_left_4_forged"] = player_mage_amuna_left_forged_sheet[3]
    # mythic
    player_mage_amuna_left_mythic_url = resource_path('resources/art/player_mage_amuna_left_male_mythic.png')
    player_mage_amuna_left_mythic_sheet = sprite_sheet((50, 75), player_mage_amuna_left_mythic_url)
    loaded_dict["player_mage_amuna_male_left_1_mythic"] = player_mage_amuna_left_mythic_sheet[0]
    loaded_dict["player_mage_amuna_male_left_2_mythic"] = player_mage_amuna_left_mythic_sheet[1]
    loaded_dict["player_mage_amuna_male_left_3_mythic"] = player_mage_amuna_left_mythic_sheet[2]
    loaded_dict["player_mage_amuna_male_left_4_mythic"] = player_mage_amuna_left_mythic_sheet[3]
    # legend
    player_mage_amuna_left_legend_url = resource_path('resources/art/player_mage_amuna_left_male_legend.png')
    player_mage_amuna_left_legend_sheet = sprite_sheet((50, 75), player_mage_amuna_left_legend_url)
    loaded_dict["player_mage_amuna_male_left_1_legend"] = player_mage_amuna_left_legend_sheet[0]
    loaded_dict["player_mage_amuna_male_left_2_legend"] = player_mage_amuna_left_legend_sheet[1]
    loaded_dict["player_mage_amuna_male_left_3_legend"] = player_mage_amuna_left_legend_sheet[2]
    loaded_dict["player_mage_amuna_male_left_4_legend"] = player_mage_amuna_left_legend_sheet[3]
    player_mage_amuna_right_url = resource_path('resources/art/player_mage_amuna_right_male.png')
    player_mage_amuna_right_sheet = sprite_sheet((50, 75), player_mage_amuna_right_url)
    loaded_dict["player_mage_amuna_male_right_1"] = player_mage_amuna_right_sheet[0]
    loaded_dict["player_mage_amuna_male_right_2"] = player_mage_amuna_right_sheet[1]
    loaded_dict["player_mage_amuna_male_right_3"] = player_mage_amuna_right_sheet[2]
    loaded_dict["player_mage_amuna_male_right_4"] = player_mage_amuna_right_sheet[3]
    # basic
    player_mage_amuna_right_basic_url = resource_path('resources/art/player_mage_amuna_right_male_basic.png')
    player_mage_amuna_right_basic_sheet = sprite_sheet((50, 75), player_mage_amuna_right_basic_url)
    loaded_dict["player_mage_amuna_male_right_1_basic"] = player_mage_amuna_right_basic_sheet[0]
    loaded_dict["player_mage_amuna_male_right_2_basic"] = player_mage_amuna_right_basic_sheet[1]
    loaded_dict["player_mage_amuna_male_right_3_basic"] = player_mage_amuna_right_basic_sheet[2]
    loaded_dict["player_mage_amuna_male_right_4_basic"] = player_mage_amuna_right_basic_sheet[3]
    # forged
    player_mage_amuna_right_forged_url = resource_path('resources/art/player_mage_amuna_right_male_forged.png')
    player_mage_amuna_right_forged_sheet = sprite_sheet((50, 75), player_mage_amuna_right_forged_url)
    loaded_dict["player_mage_amuna_male_right_1_forged"] = player_mage_amuna_right_forged_sheet[0]
    loaded_dict["player_mage_amuna_male_right_2_forged"] = player_mage_amuna_right_forged_sheet[1]
    loaded_dict["player_mage_amuna_male_right_3_forged"] = player_mage_amuna_right_forged_sheet[2]
    loaded_dict["player_mage_amuna_male_right_4_forged"] = player_mage_amuna_right_forged_sheet[3]
    # mythic
    player_mage_amuna_right_mythic_url = resource_path('resources/art/player_mage_amuna_right_male_mythic.png')
    player_mage_amuna_right_mythic_sheet = sprite_sheet((50, 75), player_mage_amuna_right_mythic_url)
    loaded_dict["player_mage_amuna_male_right_1_mythic"] = player_mage_amuna_right_mythic_sheet[0]
    loaded_dict["player_mage_amuna_male_right_2_mythic"] = player_mage_amuna_right_mythic_sheet[1]
    loaded_dict["player_mage_amuna_male_right_3_mythic"] = player_mage_amuna_right_mythic_sheet[2]
    loaded_dict["player_mage_amuna_male_right_4_mythic"] = player_mage_amuna_right_mythic_sheet[3]
    # legend
    player_mage_amuna_right_legend_url = resource_path('resources/art/player_mage_amuna_right_male_legend.png')
    player_mage_amuna_right_legend_sheet = sprite_sheet((50, 75), player_mage_amuna_right_legend_url)
    loaded_dict["player_mage_amuna_male_right_1_legend"] = player_mage_amuna_right_legend_sheet[0]
    loaded_dict["player_mage_amuna_male_right_2_legend"] = player_mage_amuna_right_legend_sheet[1]
    loaded_dict["player_mage_amuna_male_right_3_legend"] = player_mage_amuna_right_legend_sheet[2]
    loaded_dict["player_mage_amuna_male_right_4_legend"] = player_mage_amuna_right_legend_sheet[3]
    # female -----------------------------------------------------------------------------------------------------------
    player_mage_amuna_female_down_url = resource_path('resources/art/player_mage_amuna_down_female.png')
    player_mage_amuna_female_down_sheet = sprite_sheet((50, 75), player_mage_amuna_female_down_url)
    loaded_dict["player_mage_amuna_female_down_1"] = player_mage_amuna_female_down_sheet[0]
    loaded_dict["player_mage_amuna_female_down_2"] = player_mage_amuna_female_down_sheet[1]
    loaded_dict["player_mage_amuna_female_down_3"] = player_mage_amuna_female_down_sheet[2]
    loaded_dict["player_mage_amuna_female_down_4"] = player_mage_amuna_female_down_sheet[3]
    # basic
    player_mage_amuna_female_down_basic_url = resource_path('resources/art/player_mage_amuna_down_female_basic.png')
    player_mage_amuna_female_down_basic_sheet = sprite_sheet((50, 75), player_mage_amuna_female_down_basic_url)
    loaded_dict["player_mage_amuna_female_down_1_basic"] = player_mage_amuna_female_down_basic_sheet[0]
    loaded_dict["player_mage_amuna_female_down_2_basic"] = player_mage_amuna_female_down_basic_sheet[1]
    loaded_dict["player_mage_amuna_female_down_3_basic"] = player_mage_amuna_female_down_basic_sheet[2]
    loaded_dict["player_mage_amuna_female_down_4_basic"] = player_mage_amuna_female_down_basic_sheet[3]
    # forged
    player_mage_amuna_female_down_forged_url = resource_path('resources/art/player_mage_amuna_down_female_forged.png')
    player_mage_amuna_female_down_forged_sheet = sprite_sheet((50, 75), player_mage_amuna_female_down_forged_url)
    loaded_dict["player_mage_amuna_female_down_1_forged"] = player_mage_amuna_female_down_forged_sheet[0]
    loaded_dict["player_mage_amuna_female_down_2_forged"] = player_mage_amuna_female_down_forged_sheet[1]
    loaded_dict["player_mage_amuna_female_down_3_forged"] = player_mage_amuna_female_down_forged_sheet[2]
    loaded_dict["player_mage_amuna_female_down_4_forged"] = player_mage_amuna_female_down_forged_sheet[3]
    # mythic
    player_mage_amuna_female_down_mythic_url = resource_path('resources/art/player_mage_amuna_down_female_mythic.png')
    player_mage_amuna_female_down_mythic_sheet = sprite_sheet((50, 75), player_mage_amuna_female_down_mythic_url)
    loaded_dict["player_mage_amuna_female_down_1_mythic"] = player_mage_amuna_female_down_mythic_sheet[0]
    loaded_dict["player_mage_amuna_female_down_2_mythic"] = player_mage_amuna_female_down_mythic_sheet[1]
    loaded_dict["player_mage_amuna_female_down_3_mythic"] = player_mage_amuna_female_down_mythic_sheet[2]
    loaded_dict["player_mage_amuna_female_down_4_mythic"] = player_mage_amuna_female_down_mythic_sheet[3]
    # legend
    player_mage_amuna_female_down_legend_url = resource_path('resources/art/player_mage_amuna_down_female_legend.png')
    player_mage_amuna_female_down_legend_sheet = sprite_sheet((50, 75), player_mage_amuna_female_down_legend_url)
    loaded_dict["player_mage_amuna_female_down_1_legend"] = player_mage_amuna_female_down_legend_sheet[0]
    loaded_dict["player_mage_amuna_female_down_2_legend"] = player_mage_amuna_female_down_legend_sheet[1]
    loaded_dict["player_mage_amuna_female_down_3_legend"] = player_mage_amuna_female_down_legend_sheet[2]
    loaded_dict["player_mage_amuna_female_down_4_legend"] = player_mage_amuna_female_down_legend_sheet[3]
    player_mage_amuna_female_up_url = resource_path('resources/art/player_mage_amuna_up_female.png')
    player_mage_amuna_female_up_sheet = sprite_sheet((50, 75), player_mage_amuna_female_up_url)
    loaded_dict["player_mage_amuna_female_up_1"] = player_mage_amuna_female_up_sheet[0]
    loaded_dict["player_mage_amuna_female_up_2"] = player_mage_amuna_female_up_sheet[1]
    loaded_dict["player_mage_amuna_female_up_3"] = player_mage_amuna_female_up_sheet[2]
    loaded_dict["player_mage_amuna_female_up_4"] = player_mage_amuna_female_up_sheet[3]
    # basic
    player_mage_amuna_female_up_basic_url = resource_path('resources/art/player_mage_amuna_up_female_basic.png')
    player_mage_amuna_female_up_basic_sheet = sprite_sheet((50, 75), player_mage_amuna_female_up_basic_url)
    loaded_dict["player_mage_amuna_female_up_1_basic"] = player_mage_amuna_female_up_basic_sheet[0]
    loaded_dict["player_mage_amuna_female_up_2_basic"] = player_mage_amuna_female_up_basic_sheet[1]
    loaded_dict["player_mage_amuna_female_up_3_basic"] = player_mage_amuna_female_up_basic_sheet[2]
    loaded_dict["player_mage_amuna_female_up_4_basic"] = player_mage_amuna_female_up_basic_sheet[3]
    # forged
    player_mage_amuna_female_up_forged_url = resource_path('resources/art/player_mage_amuna_up_female_forged.png')
    player_mage_amuna_female_up_forged_sheet = sprite_sheet((50, 75), player_mage_amuna_female_up_forged_url)
    loaded_dict["player_mage_amuna_female_up_1_forged"] = player_mage_amuna_female_up_forged_sheet[0]
    loaded_dict["player_mage_amuna_female_up_2_forged"] = player_mage_amuna_female_up_forged_sheet[1]
    loaded_dict["player_mage_amuna_female_up_3_forged"] = player_mage_amuna_female_up_forged_sheet[2]
    loaded_dict["player_mage_amuna_female_up_4_forged"] = player_mage_amuna_female_up_forged_sheet[3]
    # mythic
    player_mage_amuna_female_up_mythic_url = resource_path('resources/art/player_mage_amuna_up_female_mythic.png')
    player_mage_amuna_female_up_mythic_sheet = sprite_sheet((50, 75), player_mage_amuna_female_up_mythic_url)
    loaded_dict["player_mage_amuna_female_up_1_mythic"] = player_mage_amuna_female_up_mythic_sheet[0]
    loaded_dict["player_mage_amuna_female_up_2_mythic"] = player_mage_amuna_female_up_mythic_sheet[1]
    loaded_dict["player_mage_amuna_female_up_3_mythic"] = player_mage_amuna_female_up_mythic_sheet[2]
    loaded_dict["player_mage_amuna_female_up_4_mythic"] = player_mage_amuna_female_up_mythic_sheet[3]
    # legend
    player_mage_amuna_female_up_legend_url = resource_path('resources/art/player_mage_amuna_up_female_legend.png')
    player_mage_amuna_female_up_legend_sheet = sprite_sheet((50, 75), player_mage_amuna_female_up_legend_url)
    loaded_dict["player_mage_amuna_female_up_1_legend"] = player_mage_amuna_female_up_legend_sheet[0]
    loaded_dict["player_mage_amuna_female_up_2_legend"] = player_mage_amuna_female_up_legend_sheet[1]
    loaded_dict["player_mage_amuna_female_up_3_legend"] = player_mage_amuna_female_up_legend_sheet[2]
    loaded_dict["player_mage_amuna_female_up_4_legend"] = player_mage_amuna_female_up_legend_sheet[3]
    player_mage_amuna_female_left_url = resource_path('resources/art/player_mage_amuna_left_female.png')
    player_mage_amuna_female_left_sheet = sprite_sheet((50, 75), player_mage_amuna_female_left_url)
    loaded_dict["player_mage_amuna_female_left_1"] = player_mage_amuna_female_left_sheet[0]
    loaded_dict["player_mage_amuna_female_left_2"] = player_mage_amuna_female_left_sheet[1]
    loaded_dict["player_mage_amuna_female_left_3"] = player_mage_amuna_female_left_sheet[2]
    loaded_dict["player_mage_amuna_female_left_4"] = player_mage_amuna_female_left_sheet[3]
    # basic
    player_mage_amuna_female_left_basic_url = resource_path('resources/art/player_mage_amuna_left_female_basic.png')
    player_mage_amuna_female_left_basic_sheet = sprite_sheet((50, 75), player_mage_amuna_female_left_basic_url)
    loaded_dict["player_mage_amuna_female_left_1_basic"] = player_mage_amuna_female_left_basic_sheet[0]
    loaded_dict["player_mage_amuna_female_left_2_basic"] = player_mage_amuna_female_left_basic_sheet[1]
    loaded_dict["player_mage_amuna_female_left_3_basic"] = player_mage_amuna_female_left_basic_sheet[2]
    loaded_dict["player_mage_amuna_female_left_4_basic"] = player_mage_amuna_female_left_basic_sheet[3]
    # forged
    player_mage_amuna_female_left_forged_url = resource_path('resources/art/player_mage_amuna_left_female_forged.png')
    player_mage_amuna_female_left_forged_sheet = sprite_sheet((50, 75), player_mage_amuna_female_left_forged_url)
    loaded_dict["player_mage_amuna_female_left_1_forged"] = player_mage_amuna_female_left_forged_sheet[0]
    loaded_dict["player_mage_amuna_female_left_2_forged"] = player_mage_amuna_female_left_forged_sheet[1]
    loaded_dict["player_mage_amuna_female_left_3_forged"] = player_mage_amuna_female_left_forged_sheet[2]
    loaded_dict["player_mage_amuna_female_left_4_forged"] = player_mage_amuna_female_left_forged_sheet[3]
    # mythic
    player_mage_amuna_female_left_mythic_url = resource_path('resources/art/player_mage_amuna_left_female_mythic.png')
    player_mage_amuna_female_left_mythic_sheet = sprite_sheet((50, 75), player_mage_amuna_female_left_mythic_url)
    loaded_dict["player_mage_amuna_female_left_1_mythic"] = player_mage_amuna_female_left_mythic_sheet[0]
    loaded_dict["player_mage_amuna_female_left_2_mythic"] = player_mage_amuna_female_left_mythic_sheet[1]
    loaded_dict["player_mage_amuna_female_left_3_mythic"] = player_mage_amuna_female_left_mythic_sheet[2]
    loaded_dict["player_mage_amuna_female_left_4_mythic"] = player_mage_amuna_female_left_mythic_sheet[3]
    # legend
    player_mage_amuna_female_left_legend_url = resource_path('resources/art/player_mage_amuna_left_female_legend.png')
    player_mage_amuna_female_left_legend_sheet = sprite_sheet((50, 75), player_mage_amuna_female_left_legend_url)
    loaded_dict["player_mage_amuna_female_left_1_legend"] = player_mage_amuna_female_left_legend_sheet[0]
    loaded_dict["player_mage_amuna_female_left_2_legend"] = player_mage_amuna_female_left_legend_sheet[1]
    loaded_dict["player_mage_amuna_female_left_3_legend"] = player_mage_amuna_female_left_legend_sheet[2]
    loaded_dict["player_mage_amuna_female_left_4_legend"] = player_mage_amuna_female_left_legend_sheet[3]
    player_mage_amuna_female_right_url = resource_path('resources/art/player_mage_amuna_right_female.png')
    player_mage_amuna_female_right_sheet = sprite_sheet((50, 75), player_mage_amuna_female_right_url)
    loaded_dict["player_mage_amuna_female_right_1"] = player_mage_amuna_female_right_sheet[0]
    loaded_dict["player_mage_amuna_female_right_2"] = player_mage_amuna_female_right_sheet[1]
    loaded_dict["player_mage_amuna_female_right_3"] = player_mage_amuna_female_right_sheet[2]
    loaded_dict["player_mage_amuna_female_right_4"] = player_mage_amuna_female_right_sheet[3]
    # basic
    player_mage_amuna_female_right_basic_url = resource_path('resources/art/player_mage_amuna_right_female_basic.png')
    player_mage_amuna_female_right_basic_sheet = sprite_sheet((50, 75), player_mage_amuna_female_right_basic_url)
    loaded_dict["player_mage_amuna_female_right_1_basic"] = player_mage_amuna_female_right_basic_sheet[0]
    loaded_dict["player_mage_amuna_female_right_2_basic"] = player_mage_amuna_female_right_basic_sheet[1]
    loaded_dict["player_mage_amuna_female_right_3_basic"] = player_mage_amuna_female_right_basic_sheet[2]
    loaded_dict["player_mage_amuna_female_right_4_basic"] = player_mage_amuna_female_right_basic_sheet[3]
    # forged
    player_mage_amuna_female_right_forged_url = resource_path('resources/art/player_mage_amuna_right_female_forged.png')
    player_mage_amuna_female_right_forged_sheet = sprite_sheet((50, 75), player_mage_amuna_female_right_forged_url)
    loaded_dict["player_mage_amuna_female_right_1_forged"] = player_mage_amuna_female_right_forged_sheet[0]
    loaded_dict["player_mage_amuna_female_right_2_forged"] = player_mage_amuna_female_right_forged_sheet[1]
    loaded_dict["player_mage_amuna_female_right_3_forged"] = player_mage_amuna_female_right_forged_sheet[2]
    loaded_dict["player_mage_amuna_female_right_4_forged"] = player_mage_amuna_female_right_forged_sheet[3]
    # mythic
    player_mage_amuna_female_right_mythic_url = resource_path('resources/art/player_mage_amuna_right_female_mythic.png')
    player_mage_amuna_female_right_mythic_sheet = sprite_sheet((50, 75), player_mage_amuna_female_right_mythic_url)
    loaded_dict["player_mage_amuna_female_right_1_mythic"] = player_mage_amuna_female_right_mythic_sheet[0]
    loaded_dict["player_mage_amuna_female_right_2_mythic"] = player_mage_amuna_female_right_mythic_sheet[1]
    loaded_dict["player_mage_amuna_female_right_3_mythic"] = player_mage_amuna_female_right_mythic_sheet[2]
    loaded_dict["player_mage_amuna_female_right_4_mythic"] = player_mage_amuna_female_right_mythic_sheet[3]
    # legend
    player_mage_amuna_female_right_legend_url = resource_path('resources/art/player_mage_amuna_right_female_legend.png')
    player_mage_amuna_female_right_legend_sheet = sprite_sheet((50, 75), player_mage_amuna_female_right_legend_url)
    loaded_dict["player_mage_amuna_female_right_1_legend"] = player_mage_amuna_female_right_legend_sheet[0]
    loaded_dict["player_mage_amuna_female_right_2_legend"] = player_mage_amuna_female_right_legend_sheet[1]
    loaded_dict["player_mage_amuna_female_right_3_legend"] = player_mage_amuna_female_right_legend_sheet[2]
    loaded_dict["player_mage_amuna_female_right_4_legend"] = player_mage_amuna_female_right_legend_sheet[3]

    # player mage nuldar race ------------------------------------------------------------------------------------------
    # male -------------------------------------------------------------------------------------------------------------
    player_mage_nuldar_down_url = resource_path('resources/art/player_mage_nuldar_down_male.png')
    player_mage_nuldar_down_sheet = sprite_sheet((50, 75), player_mage_nuldar_down_url)
    loaded_dict["player_mage_nuldar_male_down_1"] = player_mage_nuldar_down_sheet[0]
    loaded_dict["player_mage_nuldar_male_down_2"] = player_mage_nuldar_down_sheet[1]
    loaded_dict["player_mage_nuldar_male_down_3"] = player_mage_nuldar_down_sheet[2]
    loaded_dict["player_mage_nuldar_male_down_4"] = player_mage_nuldar_down_sheet[3]
    # basic
    player_mage_nuldar_down_basic_url = resource_path('resources/art/player_mage_nuldar_down_male_basic.png')
    player_mage_nuldar_down_basic_sheet = sprite_sheet((50, 75), player_mage_nuldar_down_basic_url)
    loaded_dict["player_mage_nuldar_male_down_1_basic"] = player_mage_nuldar_down_basic_sheet[0]
    loaded_dict["player_mage_nuldar_male_down_2_basic"] = player_mage_nuldar_down_basic_sheet[1]
    loaded_dict["player_mage_nuldar_male_down_3_basic"] = player_mage_nuldar_down_basic_sheet[2]
    loaded_dict["player_mage_nuldar_male_down_4_basic"] = player_mage_nuldar_down_basic_sheet[3]
    # forged
    player_mage_nuldar_down_forged_url = resource_path('resources/art/player_mage_nuldar_down_male_forged.png')
    player_mage_nuldar_down_forged_sheet = sprite_sheet((50, 75), player_mage_nuldar_down_forged_url)
    loaded_dict["player_mage_nuldar_male_down_1_forged"] = player_mage_nuldar_down_forged_sheet[0]
    loaded_dict["player_mage_nuldar_male_down_2_forged"] = player_mage_nuldar_down_forged_sheet[1]
    loaded_dict["player_mage_nuldar_male_down_3_forged"] = player_mage_nuldar_down_forged_sheet[2]
    loaded_dict["player_mage_nuldar_male_down_4_forged"] = player_mage_nuldar_down_forged_sheet[3]
    # mythic
    player_mage_nuldar_down_mythic_url = resource_path('resources/art/player_mage_nuldar_down_male_mythic.png')
    player_mage_nuldar_down_mythic_sheet = sprite_sheet((50, 75), player_mage_nuldar_down_mythic_url)
    loaded_dict["player_mage_nuldar_male_down_1_mythic"] = player_mage_nuldar_down_mythic_sheet[0]
    loaded_dict["player_mage_nuldar_male_down_2_mythic"] = player_mage_nuldar_down_mythic_sheet[1]
    loaded_dict["player_mage_nuldar_male_down_3_mythic"] = player_mage_nuldar_down_mythic_sheet[2]
    loaded_dict["player_mage_nuldar_male_down_4_mythic"] = player_mage_nuldar_down_mythic_sheet[3]
    # legend
    player_mage_nuldar_down_legend_url = resource_path('resources/art/player_mage_nuldar_down_male_legend.png')
    player_mage_nuldar_down_legend_sheet = sprite_sheet((50, 75), player_mage_nuldar_down_legend_url)
    loaded_dict["player_mage_nuldar_male_down_1_legend"] = player_mage_nuldar_down_legend_sheet[0]
    loaded_dict["player_mage_nuldar_male_down_2_legend"] = player_mage_nuldar_down_legend_sheet[1]
    loaded_dict["player_mage_nuldar_male_down_3_legend"] = player_mage_nuldar_down_legend_sheet[2]
    loaded_dict["player_mage_nuldar_male_down_4_legend"] = player_mage_nuldar_down_legend_sheet[3]
    player_mage_nuldar_up_url = resource_path('resources/art/player_mage_nuldar_up_male.png')
    player_mage_nuldar_up_sheet = sprite_sheet((50, 75), player_mage_nuldar_up_url)
    loaded_dict["player_mage_nuldar_male_up_1"] = player_mage_nuldar_up_sheet[0]
    loaded_dict["player_mage_nuldar_male_up_2"] = player_mage_nuldar_up_sheet[1]
    loaded_dict["player_mage_nuldar_male_up_3"] = player_mage_nuldar_up_sheet[2]
    loaded_dict["player_mage_nuldar_male_up_4"] = player_mage_nuldar_up_sheet[3]
    # basic
    player_mage_nuldar_up_basic_url = resource_path('resources/art/player_mage_nuldar_up_male_basic.png')
    player_mage_nuldar_up_basic_sheet = sprite_sheet((50, 75), player_mage_nuldar_up_basic_url)
    loaded_dict["player_mage_nuldar_male_up_1_basic"] = player_mage_nuldar_up_basic_sheet[0]
    loaded_dict["player_mage_nuldar_male_up_2_basic"] = player_mage_nuldar_up_basic_sheet[1]
    loaded_dict["player_mage_nuldar_male_up_3_basic"] = player_mage_nuldar_up_basic_sheet[2]
    loaded_dict["player_mage_nuldar_male_up_4_basic"] = player_mage_nuldar_up_basic_sheet[3]
    # forged
    player_mage_nuldar_up_forged_url = resource_path('resources/art/player_mage_nuldar_up_male_forged.png')
    player_mage_nuldar_up_forged_sheet = sprite_sheet((50, 75), player_mage_nuldar_up_forged_url)
    loaded_dict["player_mage_nuldar_male_up_1_forged"] = player_mage_nuldar_up_forged_sheet[0]
    loaded_dict["player_mage_nuldar_male_up_2_forged"] = player_mage_nuldar_up_forged_sheet[1]
    loaded_dict["player_mage_nuldar_male_up_3_forged"] = player_mage_nuldar_up_forged_sheet[2]
    loaded_dict["player_mage_nuldar_male_up_4_forged"] = player_mage_nuldar_up_forged_sheet[3]
    # mythic
    player_mage_nuldar_up_mythic_url = resource_path('resources/art/player_mage_nuldar_up_male_mythic.png')
    player_mage_nuldar_up_mythic_sheet = sprite_sheet((50, 75), player_mage_nuldar_up_mythic_url)
    loaded_dict["player_mage_nuldar_male_up_1_mythic"] = player_mage_nuldar_up_mythic_sheet[0]
    loaded_dict["player_mage_nuldar_male_up_2_mythic"] = player_mage_nuldar_up_mythic_sheet[1]
    loaded_dict["player_mage_nuldar_male_up_3_mythic"] = player_mage_nuldar_up_mythic_sheet[2]
    loaded_dict["player_mage_nuldar_male_up_4_mythic"] = player_mage_nuldar_up_mythic_sheet[3]
    # legend
    player_mage_nuldar_up_legend_url = resource_path('resources/art/player_mage_nuldar_up_male_legend.png')
    player_mage_nuldar_up_legend_sheet = sprite_sheet((50, 75), player_mage_nuldar_up_legend_url)
    loaded_dict["player_mage_nuldar_male_up_1_legend"] = player_mage_nuldar_up_legend_sheet[0]
    loaded_dict["player_mage_nuldar_male_up_2_legend"] = player_mage_nuldar_up_legend_sheet[1]
    loaded_dict["player_mage_nuldar_male_up_3_legend"] = player_mage_nuldar_up_legend_sheet[2]
    loaded_dict["player_mage_nuldar_male_up_4_legend"] = player_mage_nuldar_up_legend_sheet[3]
    player_mage_nuldar_left_url = resource_path('resources/art/player_mage_nuldar_left_male.png')
    player_mage_nuldar_left_sheet = sprite_sheet((50, 75), player_mage_nuldar_left_url)
    loaded_dict["player_mage_nuldar_male_left_1"] = player_mage_nuldar_left_sheet[0]
    loaded_dict["player_mage_nuldar_male_left_2"] = player_mage_nuldar_left_sheet[1]
    loaded_dict["player_mage_nuldar_male_left_3"] = player_mage_nuldar_left_sheet[2]
    loaded_dict["player_mage_nuldar_male_left_4"] = player_mage_nuldar_left_sheet[3]
    # basic
    player_mage_nuldar_left_basic_url = resource_path('resources/art/player_mage_nuldar_left_male_basic.png')
    player_mage_nuldar_left_basic_sheet = sprite_sheet((50, 75), player_mage_nuldar_left_basic_url)
    loaded_dict["player_mage_nuldar_male_left_1_basic"] = player_mage_nuldar_left_basic_sheet[0]
    loaded_dict["player_mage_nuldar_male_left_2_basic"] = player_mage_nuldar_left_basic_sheet[1]
    loaded_dict["player_mage_nuldar_male_left_3_basic"] = player_mage_nuldar_left_basic_sheet[2]
    loaded_dict["player_mage_nuldar_male_left_4_basic"] = player_mage_nuldar_left_basic_sheet[3]
    # forged
    player_mage_nuldar_left_forged_url = resource_path('resources/art/player_mage_nuldar_left_male_forged.png')
    player_mage_nuldar_left_forged_sheet = sprite_sheet((50, 75), player_mage_nuldar_left_forged_url)
    loaded_dict["player_mage_nuldar_male_left_1_forged"] = player_mage_nuldar_left_forged_sheet[0]
    loaded_dict["player_mage_nuldar_male_left_2_forged"] = player_mage_nuldar_left_forged_sheet[1]
    loaded_dict["player_mage_nuldar_male_left_3_forged"] = player_mage_nuldar_left_forged_sheet[2]
    loaded_dict["player_mage_nuldar_male_left_4_forged"] = player_mage_nuldar_left_forged_sheet[3]
    # mythic
    player_mage_nuldar_left_mythic_url = resource_path('resources/art/player_mage_nuldar_left_male_mythic.png')
    player_mage_nuldar_left_mythic_sheet = sprite_sheet((50, 75), player_mage_nuldar_left_mythic_url)
    loaded_dict["player_mage_nuldar_male_left_1_mythic"] = player_mage_nuldar_left_mythic_sheet[0]
    loaded_dict["player_mage_nuldar_male_left_2_mythic"] = player_mage_nuldar_left_mythic_sheet[1]
    loaded_dict["player_mage_nuldar_male_left_3_mythic"] = player_mage_nuldar_left_mythic_sheet[2]
    loaded_dict["player_mage_nuldar_male_left_4_mythic"] = player_mage_nuldar_left_mythic_sheet[3]
    # legend
    player_mage_nuldar_left_legend_url = resource_path('resources/art/player_mage_nuldar_left_male_legend.png')
    player_mage_nuldar_left_legend_sheet = sprite_sheet((50, 75), player_mage_nuldar_left_legend_url)
    loaded_dict["player_mage_nuldar_male_left_1_legend"] = player_mage_nuldar_left_legend_sheet[0]
    loaded_dict["player_mage_nuldar_male_left_2_legend"] = player_mage_nuldar_left_legend_sheet[1]
    loaded_dict["player_mage_nuldar_male_left_3_legend"] = player_mage_nuldar_left_legend_sheet[2]
    loaded_dict["player_mage_nuldar_male_left_4_legend"] = player_mage_nuldar_left_legend_sheet[3]
    player_mage_nuldar_right_url = resource_path('resources/art/player_mage_nuldar_right_male.png')
    player_mage_nuldar_right_sheet = sprite_sheet((50, 75), player_mage_nuldar_right_url)
    loaded_dict["player_mage_nuldar_male_right_1"] = player_mage_nuldar_right_sheet[0]
    loaded_dict["player_mage_nuldar_male_right_2"] = player_mage_nuldar_right_sheet[1]
    loaded_dict["player_mage_nuldar_male_right_3"] = player_mage_nuldar_right_sheet[2]
    loaded_dict["player_mage_nuldar_male_right_4"] = player_mage_nuldar_right_sheet[3]
    # basic
    player_mage_nuldar_right_basic_url = resource_path('resources/art/player_mage_nuldar_right_male_basic.png')
    player_mage_nuldar_right_basic_sheet = sprite_sheet((50, 75), player_mage_nuldar_right_basic_url)
    loaded_dict["player_mage_nuldar_male_right_1_basic"] = player_mage_nuldar_right_basic_sheet[0]
    loaded_dict["player_mage_nuldar_male_right_2_basic"] = player_mage_nuldar_right_basic_sheet[1]
    loaded_dict["player_mage_nuldar_male_right_3_basic"] = player_mage_nuldar_right_basic_sheet[2]
    loaded_dict["player_mage_nuldar_male_right_4_basic"] = player_mage_nuldar_right_basic_sheet[3]
    # forged
    player_mage_nuldar_right_forged_url = resource_path('resources/art/player_mage_nuldar_right_male_forged.png')
    player_mage_nuldar_right_forged_sheet = sprite_sheet((50, 75), player_mage_nuldar_right_forged_url)
    loaded_dict["player_mage_nuldar_male_right_1_forged"] = player_mage_nuldar_right_forged_sheet[0]
    loaded_dict["player_mage_nuldar_male_right_2_forged"] = player_mage_nuldar_right_forged_sheet[1]
    loaded_dict["player_mage_nuldar_male_right_3_forged"] = player_mage_nuldar_right_forged_sheet[2]
    loaded_dict["player_mage_nuldar_male_right_4_forged"] = player_mage_nuldar_right_forged_sheet[3]
    # mythic
    player_mage_nuldar_right_mythic_url = resource_path('resources/art/player_mage_nuldar_right_male_mythic.png')
    player_mage_nuldar_right_mythic_sheet = sprite_sheet((50, 75), player_mage_nuldar_right_mythic_url)
    loaded_dict["player_mage_nuldar_male_right_1_mythic"] = player_mage_nuldar_right_mythic_sheet[0]
    loaded_dict["player_mage_nuldar_male_right_2_mythic"] = player_mage_nuldar_right_mythic_sheet[1]
    loaded_dict["player_mage_nuldar_male_right_3_mythic"] = player_mage_nuldar_right_mythic_sheet[2]
    loaded_dict["player_mage_nuldar_male_right_4_mythic"] = player_mage_nuldar_right_mythic_sheet[3]
    # legend
    player_mage_nuldar_right_legend_url = resource_path('resources/art/player_mage_nuldar_right_male_legend.png')
    player_mage_nuldar_right_legend_sheet = sprite_sheet((50, 75), player_mage_nuldar_right_legend_url)
    loaded_dict["player_mage_nuldar_male_right_1_legend"] = player_mage_nuldar_right_legend_sheet[0]
    loaded_dict["player_mage_nuldar_male_right_2_legend"] = player_mage_nuldar_right_legend_sheet[1]
    loaded_dict["player_mage_nuldar_male_right_3_legend"] = player_mage_nuldar_right_legend_sheet[2]
    loaded_dict["player_mage_nuldar_male_right_4_legend"] = player_mage_nuldar_right_legend_sheet[3]
    # female -----------------------------------------------------------------------------------------------------------
    player_mage_nuldar_female_down_url = resource_path('resources/art/player_mage_nuldar_down_female.png')
    player_mage_nuldar_female_down_sheet = sprite_sheet((50, 75), player_mage_nuldar_female_down_url)
    loaded_dict["player_mage_nuldar_female_down_1"] = player_mage_nuldar_female_down_sheet[0]
    loaded_dict["player_mage_nuldar_female_down_2"] = player_mage_nuldar_female_down_sheet[1]
    loaded_dict["player_mage_nuldar_female_down_3"] = player_mage_nuldar_female_down_sheet[2]
    loaded_dict["player_mage_nuldar_female_down_4"] = player_mage_nuldar_female_down_sheet[3]
    # basic
    player_mage_nuldar_female_down_basic_url = resource_path('resources/art/player_mage_nuldar_down_female_basic.png')
    player_mage_nuldar_female_down_basic_sheet = sprite_sheet((50, 75), player_mage_nuldar_female_down_basic_url)
    loaded_dict["player_mage_nuldar_female_down_1_basic"] = player_mage_nuldar_female_down_basic_sheet[0]
    loaded_dict["player_mage_nuldar_female_down_2_basic"] = player_mage_nuldar_female_down_basic_sheet[1]
    loaded_dict["player_mage_nuldar_female_down_3_basic"] = player_mage_nuldar_female_down_basic_sheet[2]
    loaded_dict["player_mage_nuldar_female_down_4_basic"] = player_mage_nuldar_female_down_basic_sheet[3]
    # forged
    player_mage_nuldar_female_down_forged_url = resource_path('resources/art/player_mage_nuldar_down_female_forged.png')
    player_mage_nuldar_female_down_forged_sheet = sprite_sheet((50, 75), player_mage_nuldar_female_down_forged_url)
    loaded_dict["player_mage_nuldar_female_down_1_forged"] = player_mage_nuldar_female_down_forged_sheet[0]
    loaded_dict["player_mage_nuldar_female_down_2_forged"] = player_mage_nuldar_female_down_forged_sheet[1]
    loaded_dict["player_mage_nuldar_female_down_3_forged"] = player_mage_nuldar_female_down_forged_sheet[2]
    loaded_dict["player_mage_nuldar_female_down_4_forged"] = player_mage_nuldar_female_down_forged_sheet[3]
    # mythic
    player_mage_nuldar_female_down_mythic_url = resource_path('resources/art/player_mage_nuldar_down_female_mythic.png')
    player_mage_nuldar_female_down_mythic_sheet = sprite_sheet((50, 75), player_mage_nuldar_female_down_mythic_url)
    loaded_dict["player_mage_nuldar_female_down_1_mythic"] = player_mage_nuldar_female_down_mythic_sheet[0]
    loaded_dict["player_mage_nuldar_female_down_2_mythic"] = player_mage_nuldar_female_down_mythic_sheet[1]
    loaded_dict["player_mage_nuldar_female_down_3_mythic"] = player_mage_nuldar_female_down_mythic_sheet[2]
    loaded_dict["player_mage_nuldar_female_down_4_mythic"] = player_mage_nuldar_female_down_mythic_sheet[3]
    # legend
    player_mage_nuldar_female_down_legend_url = resource_path('resources/art/player_mage_nuldar_down_female_legend.png')
    player_mage_nuldar_female_down_legend_sheet = sprite_sheet((50, 75), player_mage_nuldar_female_down_legend_url)
    loaded_dict["player_mage_nuldar_female_down_1_legend"] = player_mage_nuldar_female_down_legend_sheet[0]
    loaded_dict["player_mage_nuldar_female_down_2_legend"] = player_mage_nuldar_female_down_legend_sheet[1]
    loaded_dict["player_mage_nuldar_female_down_3_legend"] = player_mage_nuldar_female_down_legend_sheet[2]
    loaded_dict["player_mage_nuldar_female_down_4_legend"] = player_mage_nuldar_female_down_legend_sheet[3]
    player_mage_nuldar_female_up_url = resource_path('resources/art/player_mage_nuldar_up_female.png')
    player_mage_nuldar_female_up_sheet = sprite_sheet((50, 75), player_mage_nuldar_female_up_url)
    loaded_dict["player_mage_nuldar_female_up_1"] = player_mage_nuldar_female_up_sheet[0]
    loaded_dict["player_mage_nuldar_female_up_2"] = player_mage_nuldar_female_up_sheet[1]
    loaded_dict["player_mage_nuldar_female_up_3"] = player_mage_nuldar_female_up_sheet[2]
    loaded_dict["player_mage_nuldar_female_up_4"] = player_mage_nuldar_female_up_sheet[3]
    # basic
    player_mage_nuldar_female_up_basic_url = resource_path('resources/art/player_mage_nuldar_up_female_basic.png')
    player_mage_nuldar_female_up_basic_sheet = sprite_sheet((50, 75), player_mage_nuldar_female_up_basic_url)
    loaded_dict["player_mage_nuldar_female_up_1_basic"] = player_mage_nuldar_female_up_basic_sheet[0]
    loaded_dict["player_mage_nuldar_female_up_2_basic"] = player_mage_nuldar_female_up_basic_sheet[1]
    loaded_dict["player_mage_nuldar_female_up_3_basic"] = player_mage_nuldar_female_up_basic_sheet[2]
    loaded_dict["player_mage_nuldar_female_up_4_basic"] = player_mage_nuldar_female_up_basic_sheet[3]
    # forged
    player_mage_nuldar_female_up_forged_url = resource_path('resources/art/player_mage_nuldar_up_female_forged.png')
    player_mage_nuldar_female_up_forged_sheet = sprite_sheet((50, 75), player_mage_nuldar_female_up_forged_url)
    loaded_dict["player_mage_nuldar_female_up_1_forged"] = player_mage_nuldar_female_up_forged_sheet[0]
    loaded_dict["player_mage_nuldar_female_up_2_forged"] = player_mage_nuldar_female_up_forged_sheet[1]
    loaded_dict["player_mage_nuldar_female_up_3_forged"] = player_mage_nuldar_female_up_forged_sheet[2]
    loaded_dict["player_mage_nuldar_female_up_4_forged"] = player_mage_nuldar_female_up_forged_sheet[3]
    # mythic
    player_mage_nuldar_female_up_mythic_url = resource_path('resources/art/player_mage_nuldar_up_female_mythic.png')
    player_mage_nuldar_female_up_mythic_sheet = sprite_sheet((50, 75), player_mage_nuldar_female_up_mythic_url)
    loaded_dict["player_mage_nuldar_female_up_1_mythic"] = player_mage_nuldar_female_up_mythic_sheet[0]
    loaded_dict["player_mage_nuldar_female_up_2_mythic"] = player_mage_nuldar_female_up_mythic_sheet[1]
    loaded_dict["player_mage_nuldar_female_up_3_mythic"] = player_mage_nuldar_female_up_mythic_sheet[2]
    loaded_dict["player_mage_nuldar_female_up_4_mythic"] = player_mage_nuldar_female_up_mythic_sheet[3]
    # legend
    player_mage_nuldar_female_up_legend_url = resource_path('resources/art/player_mage_nuldar_up_female_legend.png')
    player_mage_nuldar_female_up_legend_sheet = sprite_sheet((50, 75), player_mage_nuldar_female_up_legend_url)
    loaded_dict["player_mage_nuldar_female_up_1_legend"] = player_mage_nuldar_female_up_legend_sheet[0]
    loaded_dict["player_mage_nuldar_female_up_2_legend"] = player_mage_nuldar_female_up_legend_sheet[1]
    loaded_dict["player_mage_nuldar_female_up_3_legend"] = player_mage_nuldar_female_up_legend_sheet[2]
    loaded_dict["player_mage_nuldar_female_up_4_legend"] = player_mage_nuldar_female_up_legend_sheet[3]
    player_mage_nuldar_female_left_url = resource_path('resources/art/player_mage_nuldar_left_female.png')
    player_mage_nuldar_female_left_sheet = sprite_sheet((50, 75), player_mage_nuldar_female_left_url)
    loaded_dict["player_mage_nuldar_female_left_1"] = player_mage_nuldar_female_left_sheet[0]
    loaded_dict["player_mage_nuldar_female_left_2"] = player_mage_nuldar_female_left_sheet[1]
    loaded_dict["player_mage_nuldar_female_left_3"] = player_mage_nuldar_female_left_sheet[2]
    loaded_dict["player_mage_nuldar_female_left_4"] = player_mage_nuldar_female_left_sheet[3]
    # basic
    player_mage_nuldar_female_left_basic_url = resource_path('resources/art/player_mage_nuldar_left_female_basic.png')
    player_mage_nuldar_female_left_basic_sheet = sprite_sheet((50, 75), player_mage_nuldar_female_left_basic_url)
    loaded_dict["player_mage_nuldar_female_left_1_basic"] = player_mage_nuldar_female_left_basic_sheet[0]
    loaded_dict["player_mage_nuldar_female_left_2_basic"] = player_mage_nuldar_female_left_basic_sheet[1]
    loaded_dict["player_mage_nuldar_female_left_3_basic"] = player_mage_nuldar_female_left_basic_sheet[2]
    loaded_dict["player_mage_nuldar_female_left_4_basic"] = player_mage_nuldar_female_left_basic_sheet[3]
    # forged
    player_mage_nuldar_female_left_forged_url = resource_path('resources/art/player_mage_nuldar_left_female_forged.png')
    player_mage_nuldar_female_left_forged_sheet = sprite_sheet((50, 75), player_mage_nuldar_female_left_forged_url)
    loaded_dict["player_mage_nuldar_female_left_1_forged"] = player_mage_nuldar_female_left_forged_sheet[0]
    loaded_dict["player_mage_nuldar_female_left_2_forged"] = player_mage_nuldar_female_left_forged_sheet[1]
    loaded_dict["player_mage_nuldar_female_left_3_forged"] = player_mage_nuldar_female_left_forged_sheet[2]
    loaded_dict["player_mage_nuldar_female_left_4_forged"] = player_mage_nuldar_female_left_forged_sheet[3]
    # mythic
    player_mage_nuldar_female_left_mythic_url = resource_path('resources/art/player_mage_nuldar_left_female_mythic.png')
    player_mage_nuldar_female_left_mythic_sheet = sprite_sheet((50, 75), player_mage_nuldar_female_left_mythic_url)
    loaded_dict["player_mage_nuldar_female_left_1_mythic"] = player_mage_nuldar_female_left_mythic_sheet[0]
    loaded_dict["player_mage_nuldar_female_left_2_mythic"] = player_mage_nuldar_female_left_mythic_sheet[1]
    loaded_dict["player_mage_nuldar_female_left_3_mythic"] = player_mage_nuldar_female_left_mythic_sheet[2]
    loaded_dict["player_mage_nuldar_female_left_4_mythic"] = player_mage_nuldar_female_left_mythic_sheet[3]
    # legend
    player_mage_nuldar_female_left_legend_url = resource_path('resources/art/player_mage_nuldar_left_female_legend.png')
    player_mage_nuldar_female_left_legend_sheet = sprite_sheet((50, 75), player_mage_nuldar_female_left_legend_url)
    loaded_dict["player_mage_nuldar_female_left_1_legend"] = player_mage_nuldar_female_left_legend_sheet[0]
    loaded_dict["player_mage_nuldar_female_left_2_legend"] = player_mage_nuldar_female_left_legend_sheet[1]
    loaded_dict["player_mage_nuldar_female_left_3_legend"] = player_mage_nuldar_female_left_legend_sheet[2]
    loaded_dict["player_mage_nuldar_female_left_4_legend"] = player_mage_nuldar_female_left_legend_sheet[3]
    player_mage_nuldar_female_right_url = resource_path('resources/art/player_mage_nuldar_right_female.png')
    player_mage_nuldar_female_right_sheet = sprite_sheet((50, 75), player_mage_nuldar_female_right_url)
    loaded_dict["player_mage_nuldar_female_right_1"] = player_mage_nuldar_female_right_sheet[0]
    loaded_dict["player_mage_nuldar_female_right_2"] = player_mage_nuldar_female_right_sheet[1]
    loaded_dict["player_mage_nuldar_female_right_3"] = player_mage_nuldar_female_right_sheet[2]
    loaded_dict["player_mage_nuldar_female_right_4"] = player_mage_nuldar_female_right_sheet[3]
    # basic
    player_mage_nuldar_female_right_basic_url = resource_path('resources/art/player_mage_nuldar_right_female_basic.png')
    player_mage_nuldar_female_right_basic_sheet = sprite_sheet((50, 75), player_mage_nuldar_female_right_basic_url)
    loaded_dict["player_mage_nuldar_female_right_1_basic"] = player_mage_nuldar_female_right_basic_sheet[0]
    loaded_dict["player_mage_nuldar_female_right_2_basic"] = player_mage_nuldar_female_right_basic_sheet[1]
    loaded_dict["player_mage_nuldar_female_right_3_basic"] = player_mage_nuldar_female_right_basic_sheet[2]
    loaded_dict["player_mage_nuldar_female_right_4_basic"] = player_mage_nuldar_female_right_basic_sheet[3]
    # forged
    player_mage_nuldar_female_right_forged_url = resource_path('resources/art/player_mage_nuldar_right_'
                                                               'female_forged.png')
    player_mage_nuldar_female_right_forged_sheet = sprite_sheet((50, 75), player_mage_nuldar_female_right_forged_url)
    loaded_dict["player_mage_nuldar_female_right_1_forged"] = player_mage_nuldar_female_right_forged_sheet[0]
    loaded_dict["player_mage_nuldar_female_right_2_forged"] = player_mage_nuldar_female_right_forged_sheet[1]
    loaded_dict["player_mage_nuldar_female_right_3_forged"] = player_mage_nuldar_female_right_forged_sheet[2]
    loaded_dict["player_mage_nuldar_female_right_4_forged"] = player_mage_nuldar_female_right_forged_sheet[3]
    # mythic
    player_mage_nuldar_female_right_mythic_url = resource_path('resources/art/player_mage_nuldar_right_'
                                                               'female_mythic.png')
    player_mage_nuldar_female_right_mythic_sheet = sprite_sheet((50, 75), player_mage_nuldar_female_right_mythic_url)
    loaded_dict["player_mage_nuldar_female_right_1_mythic"] = player_mage_nuldar_female_right_mythic_sheet[0]
    loaded_dict["player_mage_nuldar_female_right_2_mythic"] = player_mage_nuldar_female_right_mythic_sheet[1]
    loaded_dict["player_mage_nuldar_female_right_3_mythic"] = player_mage_nuldar_female_right_mythic_sheet[2]
    loaded_dict["player_mage_nuldar_female_right_4_mythic"] = player_mage_nuldar_female_right_mythic_sheet[3]
    # legend
    player_mage_nuldar_female_right_legend_url = resource_path('resources/art/player_mage_nuldar_right_'
                                                               'female_legend.png')
    player_mage_nuldar_female_right_legend_sheet = sprite_sheet((50, 75), player_mage_nuldar_female_right_legend_url)
    loaded_dict["player_mage_nuldar_female_right_1_legend"] = player_mage_nuldar_female_right_legend_sheet[0]
    loaded_dict["player_mage_nuldar_female_right_2_legend"] = player_mage_nuldar_female_right_legend_sheet[1]
    loaded_dict["player_mage_nuldar_female_right_3_legend"] = player_mage_nuldar_female_right_legend_sheet[2]
    loaded_dict["player_mage_nuldar_female_right_4_legend"] = player_mage_nuldar_female_right_legend_sheet[3]

    # player mage sorae race -------------------------------------------------------------------------------------------
    # alpha ------------------------------------------------------------------------------------------------------------
    player_mage_sorae_down_url = resource_path('resources/art/player_mage_sorae_down_a.png')
    player_mage_sorae_down_sheet = sprite_sheet((50, 75), player_mage_sorae_down_url)
    loaded_dict["player_mage_sorae_a_down_1"] = player_mage_sorae_down_sheet[0]
    loaded_dict["player_mage_sorae_a_down_2"] = player_mage_sorae_down_sheet[1]
    loaded_dict["player_mage_sorae_a_down_3"] = player_mage_sorae_down_sheet[2]
    loaded_dict["player_mage_sorae_a_down_4"] = player_mage_sorae_down_sheet[3]
    # basic
    player_mage_sorae_down_basic_url = resource_path('resources/art/player_mage_sorae_down_a_basic.png')
    player_mage_sorae_down_basic_sheet = sprite_sheet((50, 75), player_mage_sorae_down_basic_url)
    loaded_dict["player_mage_sorae_a_down_1_basic"] = player_mage_sorae_down_basic_sheet[0]
    loaded_dict["player_mage_sorae_a_down_2_basic"] = player_mage_sorae_down_basic_sheet[1]
    loaded_dict["player_mage_sorae_a_down_3_basic"] = player_mage_sorae_down_basic_sheet[2]
    loaded_dict["player_mage_sorae_a_down_4_basic"] = player_mage_sorae_down_basic_sheet[3]
    # forged
    player_mage_sorae_down_forged_url = resource_path('resources/art/player_mage_sorae_down_a_forged.png')
    player_mage_sorae_down_forged_sheet = sprite_sheet((50, 75), player_mage_sorae_down_forged_url)
    loaded_dict["player_mage_sorae_a_down_1_forged"] = player_mage_sorae_down_forged_sheet[0]
    loaded_dict["player_mage_sorae_a_down_2_forged"] = player_mage_sorae_down_forged_sheet[1]
    loaded_dict["player_mage_sorae_a_down_3_forged"] = player_mage_sorae_down_forged_sheet[2]
    loaded_dict["player_mage_sorae_a_down_4_forged"] = player_mage_sorae_down_forged_sheet[3]
    # mythic
    player_mage_sorae_down_mythic_url = resource_path('resources/art/player_mage_sorae_down_a_mythic.png')
    player_mage_sorae_down_mythic_sheet = sprite_sheet((50, 75), player_mage_sorae_down_mythic_url)
    loaded_dict["player_mage_sorae_a_down_1_mythic"] = player_mage_sorae_down_mythic_sheet[0]
    loaded_dict["player_mage_sorae_a_down_2_mythic"] = player_mage_sorae_down_mythic_sheet[1]
    loaded_dict["player_mage_sorae_a_down_3_mythic"] = player_mage_sorae_down_mythic_sheet[2]
    loaded_dict["player_mage_sorae_a_down_4_mythic"] = player_mage_sorae_down_mythic_sheet[3]
    # legend
    player_mage_sorae_down_legend_url = resource_path('resources/art/player_mage_sorae_down_a_legend.png')
    player_mage_sorae_down_legend_sheet = sprite_sheet((50, 75), player_mage_sorae_down_legend_url)
    loaded_dict["player_mage_sorae_a_down_1_legend"] = player_mage_sorae_down_legend_sheet[0]
    loaded_dict["player_mage_sorae_a_down_2_legend"] = player_mage_sorae_down_legend_sheet[1]
    loaded_dict["player_mage_sorae_a_down_3_legend"] = player_mage_sorae_down_legend_sheet[2]
    loaded_dict["player_mage_sorae_a_down_4_legend"] = player_mage_sorae_down_legend_sheet[3]
    player_mage_sorae_up_url = resource_path('resources/art/player_mage_sorae_up_a.png')
    player_mage_sorae_up_sheet = sprite_sheet((50, 75), player_mage_sorae_up_url)
    loaded_dict["player_mage_sorae_a_up_1"] = player_mage_sorae_up_sheet[0]
    loaded_dict["player_mage_sorae_a_up_2"] = player_mage_sorae_up_sheet[1]
    loaded_dict["player_mage_sorae_a_up_3"] = player_mage_sorae_up_sheet[2]
    loaded_dict["player_mage_sorae_a_up_4"] = player_mage_sorae_up_sheet[3]
    # basic
    player_mage_sorae_up_basic_url = resource_path('resources/art/player_mage_sorae_up_a_basic.png')
    player_mage_sorae_up_basic_sheet = sprite_sheet((50, 75), player_mage_sorae_up_basic_url)
    loaded_dict["player_mage_sorae_a_up_1_basic"] = player_mage_sorae_up_basic_sheet[0]
    loaded_dict["player_mage_sorae_a_up_2_basic"] = player_mage_sorae_up_basic_sheet[1]
    loaded_dict["player_mage_sorae_a_up_3_basic"] = player_mage_sorae_up_basic_sheet[2]
    loaded_dict["player_mage_sorae_a_up_4_basic"] = player_mage_sorae_up_basic_sheet[3]
    # forged
    player_mage_sorae_up_forged_url = resource_path('resources/art/player_mage_sorae_up_a_forged.png')
    player_mage_sorae_up_forged_sheet = sprite_sheet((50, 75), player_mage_sorae_up_forged_url)
    loaded_dict["player_mage_sorae_a_up_1_forged"] = player_mage_sorae_up_forged_sheet[0]
    loaded_dict["player_mage_sorae_a_up_2_forged"] = player_mage_sorae_up_forged_sheet[1]
    loaded_dict["player_mage_sorae_a_up_3_forged"] = player_mage_sorae_up_forged_sheet[2]
    loaded_dict["player_mage_sorae_a_up_4_forged"] = player_mage_sorae_up_forged_sheet[3]
    # mythic
    player_mage_sorae_up_mythic_url = resource_path('resources/art/player_mage_sorae_up_a_mythic.png')
    player_mage_sorae_up_mythic_sheet = sprite_sheet((50, 75), player_mage_sorae_up_mythic_url)
    loaded_dict["player_mage_sorae_a_up_1_mythic"] = player_mage_sorae_up_mythic_sheet[0]
    loaded_dict["player_mage_sorae_a_up_2_mythic"] = player_mage_sorae_up_mythic_sheet[1]
    loaded_dict["player_mage_sorae_a_up_3_mythic"] = player_mage_sorae_up_mythic_sheet[2]
    loaded_dict["player_mage_sorae_a_up_4_mythic"] = player_mage_sorae_up_mythic_sheet[3]
    # legend
    player_mage_sorae_up_legend_url = resource_path('resources/art/player_mage_sorae_up_a_legend.png')
    player_mage_sorae_up_legend_sheet = sprite_sheet((50, 75), player_mage_sorae_up_legend_url)
    loaded_dict["player_mage_sorae_a_up_1_legend"] = player_mage_sorae_up_legend_sheet[0]
    loaded_dict["player_mage_sorae_a_up_2_legend"] = player_mage_sorae_up_legend_sheet[1]
    loaded_dict["player_mage_sorae_a_up_3_legend"] = player_mage_sorae_up_legend_sheet[2]
    loaded_dict["player_mage_sorae_a_up_4_legend"] = player_mage_sorae_up_legend_sheet[3]
    player_mage_sorae_left_url = resource_path('resources/art/player_mage_sorae_left_a.png')
    player_mage_sorae_left_sheet = sprite_sheet((50, 75), player_mage_sorae_left_url)
    loaded_dict["player_mage_sorae_a_left_1"] = player_mage_sorae_left_sheet[0]
    loaded_dict["player_mage_sorae_a_left_2"] = player_mage_sorae_left_sheet[1]
    loaded_dict["player_mage_sorae_a_left_3"] = player_mage_sorae_left_sheet[2]
    loaded_dict["player_mage_sorae_a_left_4"] = player_mage_sorae_left_sheet[3]
    # basic
    player_mage_sorae_left_basic_url = resource_path('resources/art/player_mage_sorae_left_a_basic.png')
    player_mage_sorae_left_basic_sheet = sprite_sheet((50, 75), player_mage_sorae_left_basic_url)
    loaded_dict["player_mage_sorae_a_left_1_basic"] = player_mage_sorae_left_basic_sheet[0]
    loaded_dict["player_mage_sorae_a_left_2_basic"] = player_mage_sorae_left_basic_sheet[1]
    loaded_dict["player_mage_sorae_a_left_3_basic"] = player_mage_sorae_left_basic_sheet[2]
    loaded_dict["player_mage_sorae_a_left_4_basic"] = player_mage_sorae_left_basic_sheet[3]
    # forged
    player_mage_sorae_left_forged_url = resource_path('resources/art/player_mage_sorae_left_a_forged.png')
    player_mage_sorae_left_forged_sheet = sprite_sheet((50, 75), player_mage_sorae_left_forged_url)
    loaded_dict["player_mage_sorae_a_left_1_forged"] = player_mage_sorae_left_forged_sheet[0]
    loaded_dict["player_mage_sorae_a_left_2_forged"] = player_mage_sorae_left_forged_sheet[1]
    loaded_dict["player_mage_sorae_a_left_3_forged"] = player_mage_sorae_left_forged_sheet[2]
    loaded_dict["player_mage_sorae_a_left_4_forged"] = player_mage_sorae_left_forged_sheet[3]
    # mythic
    player_mage_sorae_left_mythic_url = resource_path('resources/art/player_mage_sorae_left_a_mythic.png')
    player_mage_sorae_left_mythic_sheet = sprite_sheet((50, 75), player_mage_sorae_left_mythic_url)
    loaded_dict["player_mage_sorae_a_left_1_mythic"] = player_mage_sorae_left_mythic_sheet[0]
    loaded_dict["player_mage_sorae_a_left_2_mythic"] = player_mage_sorae_left_mythic_sheet[1]
    loaded_dict["player_mage_sorae_a_left_3_mythic"] = player_mage_sorae_left_mythic_sheet[2]
    loaded_dict["player_mage_sorae_a_left_4_mythic"] = player_mage_sorae_left_mythic_sheet[3]
    # legend
    player_mage_sorae_left_legend_url = resource_path('resources/art/player_mage_sorae_left_a_legend.png')
    player_mage_sorae_left_legend_sheet = sprite_sheet((50, 75), player_mage_sorae_left_legend_url)
    loaded_dict["player_mage_sorae_a_left_1_legend"] = player_mage_sorae_left_legend_sheet[0]
    loaded_dict["player_mage_sorae_a_left_2_legend"] = player_mage_sorae_left_legend_sheet[1]
    loaded_dict["player_mage_sorae_a_left_3_legend"] = player_mage_sorae_left_legend_sheet[2]
    loaded_dict["player_mage_sorae_a_left_4_legend"] = player_mage_sorae_left_legend_sheet[3]
    player_mage_sorae_right_url = resource_path('resources/art/player_mage_sorae_right_a.png')
    player_mage_sorae_right_sheet = sprite_sheet((50, 75), player_mage_sorae_right_url)
    loaded_dict["player_mage_sorae_a_right_1"] = player_mage_sorae_right_sheet[0]
    loaded_dict["player_mage_sorae_a_right_2"] = player_mage_sorae_right_sheet[1]
    loaded_dict["player_mage_sorae_a_right_3"] = player_mage_sorae_right_sheet[2]
    loaded_dict["player_mage_sorae_a_right_4"] = player_mage_sorae_right_sheet[3]
    # basic
    player_mage_sorae_right_basic_url = resource_path('resources/art/player_mage_sorae_right_a_basic.png')
    player_mage_sorae_right_basic_sheet = sprite_sheet((50, 75), player_mage_sorae_right_basic_url)
    loaded_dict["player_mage_sorae_a_right_1_basic"] = player_mage_sorae_right_basic_sheet[0]
    loaded_dict["player_mage_sorae_a_right_2_basic"] = player_mage_sorae_right_basic_sheet[1]
    loaded_dict["player_mage_sorae_a_right_3_basic"] = player_mage_sorae_right_basic_sheet[2]
    loaded_dict["player_mage_sorae_a_right_4_basic"] = player_mage_sorae_right_basic_sheet[3]
    # forged
    player_mage_sorae_right_forged_url = resource_path('resources/art/player_mage_sorae_right_a_forged.png')
    player_mage_sorae_right_forged_sheet = sprite_sheet((50, 75), player_mage_sorae_right_forged_url)
    loaded_dict["player_mage_sorae_a_right_1_forged"] = player_mage_sorae_right_forged_sheet[0]
    loaded_dict["player_mage_sorae_a_right_2_forged"] = player_mage_sorae_right_forged_sheet[1]
    loaded_dict["player_mage_sorae_a_right_3_forged"] = player_mage_sorae_right_forged_sheet[2]
    loaded_dict["player_mage_sorae_a_right_4_forged"] = player_mage_sorae_right_forged_sheet[3]
    # mythic
    player_mage_sorae_right_mythic_url = resource_path('resources/art/player_mage_sorae_right_a_mythic.png')
    player_mage_sorae_right_mythic_sheet = sprite_sheet((50, 75), player_mage_sorae_right_mythic_url)
    loaded_dict["player_mage_sorae_a_right_1_mythic"] = player_mage_sorae_right_mythic_sheet[0]
    loaded_dict["player_mage_sorae_a_right_2_mythic"] = player_mage_sorae_right_mythic_sheet[1]
    loaded_dict["player_mage_sorae_a_right_3_mythic"] = player_mage_sorae_right_mythic_sheet[2]
    loaded_dict["player_mage_sorae_a_right_4_mythic"] = player_mage_sorae_right_mythic_sheet[3]
    # legend
    player_mage_sorae_right_legend_url = resource_path('resources/art/player_mage_sorae_right_a_legend.png')
    player_mage_sorae_right_legend_sheet = sprite_sheet((50, 75), player_mage_sorae_right_legend_url)
    loaded_dict["player_mage_sorae_a_right_1_legend"] = player_mage_sorae_right_legend_sheet[0]
    loaded_dict["player_mage_sorae_a_right_2_legend"] = player_mage_sorae_right_legend_sheet[1]
    loaded_dict["player_mage_sorae_a_right_3_legend"] = player_mage_sorae_right_legend_sheet[2]
    loaded_dict["player_mage_sorae_a_right_4_legend"] = player_mage_sorae_right_legend_sheet[3]
    # beta -------------------------------------------------------------------------------------------------------------
    player_mage_sorae_b_down_url = resource_path('resources/art/player_mage_sorae_down_b.png')
    player_mage_sorae_b_down_sheet = sprite_sheet((50, 75), player_mage_sorae_b_down_url)
    loaded_dict["player_mage_sorae_b_down_1"] = player_mage_sorae_b_down_sheet[0]
    loaded_dict["player_mage_sorae_b_down_2"] = player_mage_sorae_b_down_sheet[1]
    loaded_dict["player_mage_sorae_b_down_3"] = player_mage_sorae_b_down_sheet[2]
    loaded_dict["player_mage_sorae_b_down_4"] = player_mage_sorae_b_down_sheet[3]
    # basic
    player_mage_sorae_b_down_basic_url = resource_path('resources/art/player_mage_sorae_down_b_basic.png')
    player_mage_sorae_b_down_basic_sheet = sprite_sheet((50, 75), player_mage_sorae_b_down_basic_url)
    loaded_dict["player_mage_sorae_b_down_1_basic"] = player_mage_sorae_b_down_basic_sheet[0]
    loaded_dict["player_mage_sorae_b_down_2_basic"] = player_mage_sorae_b_down_basic_sheet[1]
    loaded_dict["player_mage_sorae_b_down_3_basic"] = player_mage_sorae_b_down_basic_sheet[2]
    loaded_dict["player_mage_sorae_b_down_4_basic"] = player_mage_sorae_b_down_basic_sheet[3]
    # forged
    player_mage_sorae_b_down_forged_url = resource_path('resources/art/player_mage_sorae_down_b_forged.png')
    player_mage_sorae_b_down_forged_sheet = sprite_sheet((50, 75), player_mage_sorae_b_down_forged_url)
    loaded_dict["player_mage_sorae_b_down_1_forged"] = player_mage_sorae_b_down_forged_sheet[0]
    loaded_dict["player_mage_sorae_b_down_2_forged"] = player_mage_sorae_b_down_forged_sheet[1]
    loaded_dict["player_mage_sorae_b_down_3_forged"] = player_mage_sorae_b_down_forged_sheet[2]
    loaded_dict["player_mage_sorae_b_down_4_forged"] = player_mage_sorae_b_down_forged_sheet[3]
    # mythic
    player_mage_sorae_b_down_mythic_url = resource_path('resources/art/player_mage_sorae_down_b_mythic.png')
    player_mage_sorae_b_down_mythic_sheet = sprite_sheet((50, 75), player_mage_sorae_b_down_mythic_url)
    loaded_dict["player_mage_sorae_b_down_1_mythic"] = player_mage_sorae_b_down_mythic_sheet[0]
    loaded_dict["player_mage_sorae_b_down_2_mythic"] = player_mage_sorae_b_down_mythic_sheet[1]
    loaded_dict["player_mage_sorae_b_down_3_mythic"] = player_mage_sorae_b_down_mythic_sheet[2]
    loaded_dict["player_mage_sorae_b_down_4_mythic"] = player_mage_sorae_b_down_mythic_sheet[3]
    # legend
    player_mage_sorae_b_down_legend_url = resource_path('resources/art/player_mage_sorae_down_b_legend.png')
    player_mage_sorae_b_down_legend_sheet = sprite_sheet((50, 75), player_mage_sorae_b_down_legend_url)
    loaded_dict["player_mage_sorae_b_down_1_legend"] = player_mage_sorae_b_down_legend_sheet[0]
    loaded_dict["player_mage_sorae_b_down_2_legend"] = player_mage_sorae_b_down_legend_sheet[1]
    loaded_dict["player_mage_sorae_b_down_3_legend"] = player_mage_sorae_b_down_legend_sheet[2]
    loaded_dict["player_mage_sorae_b_down_4_legend"] = player_mage_sorae_b_down_legend_sheet[3]
    player_mage_sorae_b_up_url = resource_path('resources/art/player_mage_sorae_up_b.png')
    player_mage_sorae_b_up_sheet = sprite_sheet((50, 75), player_mage_sorae_b_up_url)
    loaded_dict["player_mage_sorae_b_up_1"] = player_mage_sorae_b_up_sheet[0]
    loaded_dict["player_mage_sorae_b_up_2"] = player_mage_sorae_b_up_sheet[1]
    loaded_dict["player_mage_sorae_b_up_3"] = player_mage_sorae_b_up_sheet[2]
    loaded_dict["player_mage_sorae_b_up_4"] = player_mage_sorae_b_up_sheet[3]
    # basic
    player_mage_sorae_b_up_basic_url = resource_path('resources/art/player_mage_sorae_up_b_basic.png')
    player_mage_sorae_b_up_basic_sheet = sprite_sheet((50, 75), player_mage_sorae_b_up_basic_url)
    loaded_dict["player_mage_sorae_b_up_1_basic"] = player_mage_sorae_b_up_basic_sheet[0]
    loaded_dict["player_mage_sorae_b_up_2_basic"] = player_mage_sorae_b_up_basic_sheet[1]
    loaded_dict["player_mage_sorae_b_up_3_basic"] = player_mage_sorae_b_up_basic_sheet[2]
    loaded_dict["player_mage_sorae_b_up_4_basic"] = player_mage_sorae_b_up_basic_sheet[3]
    # forged
    player_mage_sorae_b_up_forged_url = resource_path('resources/art/player_mage_sorae_up_b_forged.png')
    player_mage_sorae_b_up_forged_sheet = sprite_sheet((50, 75), player_mage_sorae_b_up_forged_url)
    loaded_dict["player_mage_sorae_b_up_1_forged"] = player_mage_sorae_b_up_forged_sheet[0]
    loaded_dict["player_mage_sorae_b_up_2_forged"] = player_mage_sorae_b_up_forged_sheet[1]
    loaded_dict["player_mage_sorae_b_up_3_forged"] = player_mage_sorae_b_up_forged_sheet[2]
    loaded_dict["player_mage_sorae_b_up_4_forged"] = player_mage_sorae_b_up_forged_sheet[3]
    # mythic
    player_mage_sorae_b_up_mythic_url = resource_path('resources/art/player_mage_sorae_up_b_mythic.png')
    player_mage_sorae_b_up_mythic_sheet = sprite_sheet((50, 75), player_mage_sorae_b_up_mythic_url)
    loaded_dict["player_mage_sorae_b_up_1_mythic"] = player_mage_sorae_b_up_mythic_sheet[0]
    loaded_dict["player_mage_sorae_b_up_2_mythic"] = player_mage_sorae_b_up_mythic_sheet[1]
    loaded_dict["player_mage_sorae_b_up_3_mythic"] = player_mage_sorae_b_up_mythic_sheet[2]
    loaded_dict["player_mage_sorae_b_up_4_mythic"] = player_mage_sorae_b_up_mythic_sheet[3]
    # legend
    player_mage_sorae_b_up_legend_url = resource_path('resources/art/player_mage_sorae_up_b_legend.png')
    player_mage_sorae_b_up_legend_sheet = sprite_sheet((50, 75), player_mage_sorae_b_up_legend_url)
    loaded_dict["player_mage_sorae_b_up_1_legend"] = player_mage_sorae_b_up_legend_sheet[0]
    loaded_dict["player_mage_sorae_b_up_2_legend"] = player_mage_sorae_b_up_legend_sheet[1]
    loaded_dict["player_mage_sorae_b_up_3_legend"] = player_mage_sorae_b_up_legend_sheet[2]
    loaded_dict["player_mage_sorae_b_up_4_legend"] = player_mage_sorae_b_up_legend_sheet[3]
    player_mage_sorae_b_left_url = resource_path('resources/art/player_mage_sorae_left_b.png')
    player_mage_sorae_b_left_sheet = sprite_sheet((50, 75), player_mage_sorae_b_left_url)
    loaded_dict["player_mage_sorae_b_left_1"] = player_mage_sorae_b_left_sheet[0]
    loaded_dict["player_mage_sorae_b_left_2"] = player_mage_sorae_b_left_sheet[1]
    loaded_dict["player_mage_sorae_b_left_3"] = player_mage_sorae_b_left_sheet[2]
    loaded_dict["player_mage_sorae_b_left_4"] = player_mage_sorae_b_left_sheet[3]
    # basic
    player_mage_sorae_b_left_basic_url = resource_path('resources/art/player_mage_sorae_left_b_basic.png')
    player_mage_sorae_b_left_basic_sheet = sprite_sheet((50, 75), player_mage_sorae_b_left_basic_url)
    loaded_dict["player_mage_sorae_b_left_1_basic"] = player_mage_sorae_b_left_basic_sheet[0]
    loaded_dict["player_mage_sorae_b_left_2_basic"] = player_mage_sorae_b_left_basic_sheet[1]
    loaded_dict["player_mage_sorae_b_left_3_basic"] = player_mage_sorae_b_left_basic_sheet[2]
    loaded_dict["player_mage_sorae_b_left_4_basic"] = player_mage_sorae_b_left_basic_sheet[3]
    # forged
    player_mage_sorae_b_left_forged_url = resource_path('resources/art/player_mage_sorae_left_b_forged.png')
    player_mage_sorae_b_left_forged_sheet = sprite_sheet((50, 75), player_mage_sorae_b_left_forged_url)
    loaded_dict["player_mage_sorae_b_left_1_forged"] = player_mage_sorae_b_left_forged_sheet[0]
    loaded_dict["player_mage_sorae_b_left_2_forged"] = player_mage_sorae_b_left_forged_sheet[1]
    loaded_dict["player_mage_sorae_b_left_3_forged"] = player_mage_sorae_b_left_forged_sheet[2]
    loaded_dict["player_mage_sorae_b_left_4_forged"] = player_mage_sorae_b_left_forged_sheet[3]
    # mythic
    player_mage_sorae_b_left_mythic_url = resource_path('resources/art/player_mage_sorae_left_b_mythic.png')
    player_mage_sorae_b_left_mythic_sheet = sprite_sheet((50, 75), player_mage_sorae_b_left_mythic_url)
    loaded_dict["player_mage_sorae_b_left_1_mythic"] = player_mage_sorae_b_left_mythic_sheet[0]
    loaded_dict["player_mage_sorae_b_left_2_mythic"] = player_mage_sorae_b_left_mythic_sheet[1]
    loaded_dict["player_mage_sorae_b_left_3_mythic"] = player_mage_sorae_b_left_mythic_sheet[2]
    loaded_dict["player_mage_sorae_b_left_4_mythic"] = player_mage_sorae_b_left_mythic_sheet[3]
    # legend
    player_mage_sorae_b_left_legend_url = resource_path('resources/art/player_mage_sorae_left_b_legend.png')
    player_mage_sorae_b_left_legend_sheet = sprite_sheet((50, 75), player_mage_sorae_b_left_legend_url)
    loaded_dict["player_mage_sorae_b_left_1_legend"] = player_mage_sorae_b_left_legend_sheet[0]
    loaded_dict["player_mage_sorae_b_left_2_legend"] = player_mage_sorae_b_left_legend_sheet[1]
    loaded_dict["player_mage_sorae_b_left_3_legend"] = player_mage_sorae_b_left_legend_sheet[2]
    loaded_dict["player_mage_sorae_b_left_4_legend"] = player_mage_sorae_b_left_legend_sheet[3]
    player_mage_sorae_b_right_url = resource_path('resources/art/player_mage_sorae_right_b.png')
    player_mage_sorae_b_right_sheet = sprite_sheet((50, 75), player_mage_sorae_b_right_url)
    loaded_dict["player_mage_sorae_b_right_1"] = player_mage_sorae_b_right_sheet[0]
    loaded_dict["player_mage_sorae_b_right_2"] = player_mage_sorae_b_right_sheet[1]
    loaded_dict["player_mage_sorae_b_right_3"] = player_mage_sorae_b_right_sheet[2]
    loaded_dict["player_mage_sorae_b_right_4"] = player_mage_sorae_b_right_sheet[3]
    # basic
    player_mage_sorae_b_right_basic_url = resource_path('resources/art/player_mage_sorae_right_b_basic.png')
    player_mage_sorae_b_right_basic_sheet = sprite_sheet((50, 75), player_mage_sorae_b_right_basic_url)
    loaded_dict["player_mage_sorae_b_right_1_basic"] = player_mage_sorae_b_right_basic_sheet[0]
    loaded_dict["player_mage_sorae_b_right_2_basic"] = player_mage_sorae_b_right_basic_sheet[1]
    loaded_dict["player_mage_sorae_b_right_3_basic"] = player_mage_sorae_b_right_basic_sheet[2]
    loaded_dict["player_mage_sorae_b_right_4_basic"] = player_mage_sorae_b_right_basic_sheet[3]
    # forged
    player_mage_sorae_b_right_forged_url = resource_path('resources/art/player_mage_sorae_right_b_forged.png')
    player_mage_sorae_b_right_forged_sheet = sprite_sheet((50, 75), player_mage_sorae_b_right_forged_url)
    loaded_dict["player_mage_sorae_b_right_1_forged"] = player_mage_sorae_b_right_forged_sheet[0]
    loaded_dict["player_mage_sorae_b_right_2_forged"] = player_mage_sorae_b_right_forged_sheet[1]
    loaded_dict["player_mage_sorae_b_right_3_forged"] = player_mage_sorae_b_right_forged_sheet[2]
    loaded_dict["player_mage_sorae_b_right_4_forged"] = player_mage_sorae_b_right_forged_sheet[3]
    # mythic
    player_mage_sorae_b_right_mythic_url = resource_path('resources/art/player_mage_sorae_right_b_mythic.png')
    player_mage_sorae_b_right_mythic_sheet = sprite_sheet((50, 75), player_mage_sorae_b_right_mythic_url)
    loaded_dict["player_mage_sorae_b_right_1_mythic"] = player_mage_sorae_b_right_mythic_sheet[0]
    loaded_dict["player_mage_sorae_b_right_2_mythic"] = player_mage_sorae_b_right_mythic_sheet[1]
    loaded_dict["player_mage_sorae_b_right_3_mythic"] = player_mage_sorae_b_right_mythic_sheet[2]
    loaded_dict["player_mage_sorae_b_right_4_mythic"] = player_mage_sorae_b_right_mythic_sheet[3]
    # legend
    player_mage_sorae_b_right_legend_url = resource_path('resources/art/player_mage_sorae_right_b_legend.png')
    player_mage_sorae_b_right_legend_sheet = sprite_sheet((50, 75), player_mage_sorae_b_right_legend_url)
    loaded_dict["player_mage_sorae_b_right_1_legend"] = player_mage_sorae_b_right_legend_sheet[0]
    loaded_dict["player_mage_sorae_b_right_2_legend"] = player_mage_sorae_b_right_legend_sheet[1]
    loaded_dict["player_mage_sorae_b_right_3_legend"] = player_mage_sorae_b_right_legend_sheet[2]
    loaded_dict["player_mage_sorae_b_right_4_legend"] = player_mage_sorae_b_right_legend_sheet[3]

    # player fighter amuna race ----------------------------------------------------------------------------------------
    # male -------------------------------------------------------------------------------------------------------------
    player_fighter_amuna_down_url = resource_path('resources/art/player_fighter_amuna_down_male.png')
    player_fighter_amuna_down_sheet = sprite_sheet((50, 75), player_fighter_amuna_down_url)
    loaded_dict["player_fighter_amuna_male_down_1"] = player_fighter_amuna_down_sheet[0]
    loaded_dict["player_fighter_amuna_male_down_2"] = player_fighter_amuna_down_sheet[1]
    loaded_dict["player_fighter_amuna_male_down_3"] = player_fighter_amuna_down_sheet[2]
    loaded_dict["player_fighter_amuna_male_down_4"] = player_fighter_amuna_down_sheet[3]
    # basic
    player_fighter_amuna_down_basic_url = resource_path('resources/art/player_fighter_amuna_down_male_basic.png')
    player_fighter_amuna_down_basic_sheet = sprite_sheet((50, 75), player_fighter_amuna_down_basic_url)
    loaded_dict["player_fighter_amuna_male_down_1_basic"] = player_fighter_amuna_down_basic_sheet[0]
    loaded_dict["player_fighter_amuna_male_down_2_basic"] = player_fighter_amuna_down_basic_sheet[1]
    loaded_dict["player_fighter_amuna_male_down_3_basic"] = player_fighter_amuna_down_basic_sheet[2]
    loaded_dict["player_fighter_amuna_male_down_4_basic"] = player_fighter_amuna_down_basic_sheet[3]
    # forged
    player_fighter_amuna_down_forged_url = resource_path('resources/art/player_fighter_amuna_down_male_forged.png')
    player_fighter_amuna_down_forged_sheet = sprite_sheet((50, 75), player_fighter_amuna_down_forged_url)
    loaded_dict["player_fighter_amuna_male_down_1_forged"] = player_fighter_amuna_down_forged_sheet[0]
    loaded_dict["player_fighter_amuna_male_down_2_forged"] = player_fighter_amuna_down_forged_sheet[1]
    loaded_dict["player_fighter_amuna_male_down_3_forged"] = player_fighter_amuna_down_forged_sheet[2]
    loaded_dict["player_fighter_amuna_male_down_4_forged"] = player_fighter_amuna_down_forged_sheet[3]
    # mythic
    player_fighter_amuna_down_mythic_url = resource_path('resources/art/player_fighter_amuna_down_male_mythic.png')
    player_fighter_amuna_down_mythic_sheet = sprite_sheet((50, 75), player_fighter_amuna_down_mythic_url)
    loaded_dict["player_fighter_amuna_male_down_1_mythic"] = player_fighter_amuna_down_mythic_sheet[0]
    loaded_dict["player_fighter_amuna_male_down_2_mythic"] = player_fighter_amuna_down_mythic_sheet[1]
    loaded_dict["player_fighter_amuna_male_down_3_mythic"] = player_fighter_amuna_down_mythic_sheet[2]
    loaded_dict["player_fighter_amuna_male_down_4_mythic"] = player_fighter_amuna_down_mythic_sheet[3]
    # legend
    player_fighter_amuna_down_legend_url = resource_path('resources/art/player_fighter_amuna_down_male_legend.png')
    player_fighter_amuna_down_legend_sheet = sprite_sheet((50, 75), player_fighter_amuna_down_legend_url)
    loaded_dict["player_fighter_amuna_male_down_1_legend"] = player_fighter_amuna_down_legend_sheet[0]
    loaded_dict["player_fighter_amuna_male_down_2_legend"] = player_fighter_amuna_down_legend_sheet[1]
    loaded_dict["player_fighter_amuna_male_down_3_legend"] = player_fighter_amuna_down_legend_sheet[2]
    loaded_dict["player_fighter_amuna_male_down_4_legend"] = player_fighter_amuna_down_legend_sheet[3]
    player_fighter_amuna_up_url = resource_path('resources/art/player_fighter_amuna_up_male.png')
    player_fighter_amuna_up_sheet = sprite_sheet((50, 75), player_fighter_amuna_up_url)
    loaded_dict["player_fighter_amuna_male_up_1"] = player_fighter_amuna_up_sheet[0]
    loaded_dict["player_fighter_amuna_male_up_2"] = player_fighter_amuna_up_sheet[1]
    loaded_dict["player_fighter_amuna_male_up_3"] = player_fighter_amuna_up_sheet[2]
    loaded_dict["player_fighter_amuna_male_up_4"] = player_fighter_amuna_up_sheet[3]
    # basic
    player_fighter_amuna_up_basic_url = resource_path('resources/art/player_fighter_amuna_up_male_basic.png')
    player_fighter_amuna_up_basic_sheet = sprite_sheet((50, 75), player_fighter_amuna_up_basic_url)
    loaded_dict["player_fighter_amuna_male_up_1_basic"] = player_fighter_amuna_up_basic_sheet[0]
    loaded_dict["player_fighter_amuna_male_up_2_basic"] = player_fighter_amuna_up_basic_sheet[1]
    loaded_dict["player_fighter_amuna_male_up_3_basic"] = player_fighter_amuna_up_basic_sheet[2]
    loaded_dict["player_fighter_amuna_male_up_4_basic"] = player_fighter_amuna_up_basic_sheet[3]
    # forged
    player_fighter_amuna_up_forged_url = resource_path('resources/art/player_fighter_amuna_up_male_forged.png')
    player_fighter_amuna_up_forged_sheet = sprite_sheet((50, 75), player_fighter_amuna_up_forged_url)
    loaded_dict["player_fighter_amuna_male_up_1_forged"] = player_fighter_amuna_up_forged_sheet[0]
    loaded_dict["player_fighter_amuna_male_up_2_forged"] = player_fighter_amuna_up_forged_sheet[1]
    loaded_dict["player_fighter_amuna_male_up_3_forged"] = player_fighter_amuna_up_forged_sheet[2]
    loaded_dict["player_fighter_amuna_male_up_4_forged"] = player_fighter_amuna_up_forged_sheet[3]
    # mythic
    player_fighter_amuna_up_mythic_url = resource_path('resources/art/player_fighter_amuna_up_male_mythic.png')
    player_fighter_amuna_up_mythic_sheet = sprite_sheet((50, 75), player_fighter_amuna_up_mythic_url)
    loaded_dict["player_fighter_amuna_male_up_1_mythic"] = player_fighter_amuna_up_mythic_sheet[0]
    loaded_dict["player_fighter_amuna_male_up_2_mythic"] = player_fighter_amuna_up_mythic_sheet[1]
    loaded_dict["player_fighter_amuna_male_up_3_mythic"] = player_fighter_amuna_up_mythic_sheet[2]
    loaded_dict["player_fighter_amuna_male_up_4_mythic"] = player_fighter_amuna_up_mythic_sheet[3]
    # legend
    player_fighter_amuna_up_legend_url = resource_path('resources/art/player_fighter_amuna_up_male_legend.png')
    player_fighter_amuna_up_legend_sheet = sprite_sheet((50, 75), player_fighter_amuna_up_legend_url)
    loaded_dict["player_fighter_amuna_male_up_1_legend"] = player_fighter_amuna_up_legend_sheet[0]
    loaded_dict["player_fighter_amuna_male_up_2_legend"] = player_fighter_amuna_up_legend_sheet[1]
    loaded_dict["player_fighter_amuna_male_up_3_legend"] = player_fighter_amuna_up_legend_sheet[2]
    loaded_dict["player_fighter_amuna_male_up_4_legend"] = player_fighter_amuna_up_legend_sheet[3]
    player_fighter_amuna_left_url = resource_path('resources/art/player_fighter_amuna_left_male.png')
    player_fighter_amuna_left_sheet = sprite_sheet((50, 75), player_fighter_amuna_left_url)
    loaded_dict["player_fighter_amuna_male_left_1"] = player_fighter_amuna_left_sheet[0]
    loaded_dict["player_fighter_amuna_male_left_2"] = player_fighter_amuna_left_sheet[1]
    loaded_dict["player_fighter_amuna_male_left_3"] = player_fighter_amuna_left_sheet[2]
    loaded_dict["player_fighter_amuna_male_left_4"] = player_fighter_amuna_left_sheet[3]
    # basic
    player_fighter_amuna_left_basic_url = resource_path('resources/art/player_fighter_amuna_left_male_basic.png')
    player_fighter_amuna_left_basic_sheet = sprite_sheet((50, 75), player_fighter_amuna_left_basic_url)
    loaded_dict["player_fighter_amuna_male_left_1_basic"] = player_fighter_amuna_left_basic_sheet[0]
    loaded_dict["player_fighter_amuna_male_left_2_basic"] = player_fighter_amuna_left_basic_sheet[1]
    loaded_dict["player_fighter_amuna_male_left_3_basic"] = player_fighter_amuna_left_basic_sheet[2]
    loaded_dict["player_fighter_amuna_male_left_4_basic"] = player_fighter_amuna_left_basic_sheet[3]
    # forged
    player_fighter_amuna_left_forged_url = resource_path('resources/art/player_fighter_amuna_left_male_forged.png')
    player_fighter_amuna_left_forged_sheet = sprite_sheet((50, 75), player_fighter_amuna_left_forged_url)
    loaded_dict["player_fighter_amuna_male_left_1_forged"] = player_fighter_amuna_left_forged_sheet[0]
    loaded_dict["player_fighter_amuna_male_left_2_forged"] = player_fighter_amuna_left_forged_sheet[1]
    loaded_dict["player_fighter_amuna_male_left_3_forged"] = player_fighter_amuna_left_forged_sheet[2]
    loaded_dict["player_fighter_amuna_male_left_4_forged"] = player_fighter_amuna_left_forged_sheet[3]
    # mythic
    player_fighter_amuna_left_mythic_url = resource_path('resources/art/player_fighter_amuna_left_male_mythic.png')
    player_fighter_amuna_left_mythic_sheet = sprite_sheet((50, 75), player_fighter_amuna_left_mythic_url)
    loaded_dict["player_fighter_amuna_male_left_1_mythic"] = player_fighter_amuna_left_mythic_sheet[0]
    loaded_dict["player_fighter_amuna_male_left_2_mythic"] = player_fighter_amuna_left_mythic_sheet[1]
    loaded_dict["player_fighter_amuna_male_left_3_mythic"] = player_fighter_amuna_left_mythic_sheet[2]
    loaded_dict["player_fighter_amuna_male_left_4_mythic"] = player_fighter_amuna_left_mythic_sheet[3]
    # legend
    player_fighter_amuna_left_legend_url = resource_path('resources/art/player_fighter_amuna_left_male_legend.png')
    player_fighter_amuna_left_legend_sheet = sprite_sheet((50, 75), player_fighter_amuna_left_legend_url)
    loaded_dict["player_fighter_amuna_male_left_1_legend"] = player_fighter_amuna_left_legend_sheet[0]
    loaded_dict["player_fighter_amuna_male_left_2_legend"] = player_fighter_amuna_left_legend_sheet[1]
    loaded_dict["player_fighter_amuna_male_left_3_legend"] = player_fighter_amuna_left_legend_sheet[2]
    loaded_dict["player_fighter_amuna_male_left_4_legend"] = player_fighter_amuna_left_legend_sheet[3]
    player_fighter_amuna_right_url = resource_path('resources/art/player_fighter_amuna_right_male.png')
    player_fighter_amuna_right_sheet = sprite_sheet((50, 75), player_fighter_amuna_right_url)
    loaded_dict["player_fighter_amuna_male_right_1"] = player_fighter_amuna_right_sheet[0]
    loaded_dict["player_fighter_amuna_male_right_2"] = player_fighter_amuna_right_sheet[1]
    loaded_dict["player_fighter_amuna_male_right_3"] = player_fighter_amuna_right_sheet[2]
    loaded_dict["player_fighter_amuna_male_right_4"] = player_fighter_amuna_right_sheet[3]
    # basic
    player_fighter_amuna_right_basic_url = resource_path('resources/art/player_fighter_amuna_right_male_basic.png')
    player_fighter_amuna_right_basic_sheet = sprite_sheet((50, 75), player_fighter_amuna_right_basic_url)
    loaded_dict["player_fighter_amuna_male_right_1_basic"] = player_fighter_amuna_right_basic_sheet[0]
    loaded_dict["player_fighter_amuna_male_right_2_basic"] = player_fighter_amuna_right_basic_sheet[1]
    loaded_dict["player_fighter_amuna_male_right_3_basic"] = player_fighter_amuna_right_basic_sheet[2]
    loaded_dict["player_fighter_amuna_male_right_4_basic"] = player_fighter_amuna_right_basic_sheet[3]
    # forged
    player_fighter_amuna_right_forged_url = resource_path('resources/art/player_fighter_amuna_right_male_forged.png')
    player_fighter_amuna_right_forged_sheet = sprite_sheet((50, 75), player_fighter_amuna_right_forged_url)
    loaded_dict["player_fighter_amuna_male_right_1_forged"] = player_fighter_amuna_right_forged_sheet[0]
    loaded_dict["player_fighter_amuna_male_right_2_forged"] = player_fighter_amuna_right_forged_sheet[1]
    loaded_dict["player_fighter_amuna_male_right_3_forged"] = player_fighter_amuna_right_forged_sheet[2]
    loaded_dict["player_fighter_amuna_male_right_4_forged"] = player_fighter_amuna_right_forged_sheet[3]
    # mythic
    player_fighter_amuna_right_mythic_url = resource_path('resources/art/player_fighter_amuna_right_male_mythic.png')
    player_fighter_amuna_right_mythic_sheet = sprite_sheet((50, 75), player_fighter_amuna_right_mythic_url)
    loaded_dict["player_fighter_amuna_male_right_1_mythic"] = player_fighter_amuna_right_mythic_sheet[0]
    loaded_dict["player_fighter_amuna_male_right_2_mythic"] = player_fighter_amuna_right_mythic_sheet[1]
    loaded_dict["player_fighter_amuna_male_right_3_mythic"] = player_fighter_amuna_right_mythic_sheet[2]
    loaded_dict["player_fighter_amuna_male_right_4_mythic"] = player_fighter_amuna_right_mythic_sheet[3]
    # legend
    player_fighter_amuna_right_legend_url = resource_path('resources/art/player_fighter_amuna_right_male_legend.png')
    player_fighter_amuna_right_legend_sheet = sprite_sheet((50, 75), player_fighter_amuna_right_legend_url)
    loaded_dict["player_fighter_amuna_male_right_1_legend"] = player_fighter_amuna_right_legend_sheet[0]
    loaded_dict["player_fighter_amuna_male_right_2_legend"] = player_fighter_amuna_right_legend_sheet[1]
    loaded_dict["player_fighter_amuna_male_right_3_legend"] = player_fighter_amuna_right_legend_sheet[2]
    loaded_dict["player_fighter_amuna_male_right_4_legend"] = player_fighter_amuna_right_legend_sheet[3]
    # female -----------------------------------------------------------------------------------------------------------
    player_fighter_amuna_female_down_url = resource_path('resources/art/player_fighter_amuna_down_female.png')
    player_fighter_amuna_female_down_sheet = sprite_sheet((50, 75), player_fighter_amuna_female_down_url)
    loaded_dict["player_fighter_amuna_female_down_1"] = player_fighter_amuna_female_down_sheet[0]
    loaded_dict["player_fighter_amuna_female_down_2"] = player_fighter_amuna_female_down_sheet[1]
    loaded_dict["player_fighter_amuna_female_down_3"] = player_fighter_amuna_female_down_sheet[2]
    loaded_dict["player_fighter_amuna_female_down_4"] = player_fighter_amuna_female_down_sheet[3]
    # basic
    player_fighter_amuna_female_down_basic_url = resource_path('resources/art/'
                                                               'player_fighter_amuna_down_female_basic.png')
    player_fighter_amuna_female_down_basic_sheet = sprite_sheet((50, 75), player_fighter_amuna_female_down_basic_url)
    loaded_dict["player_fighter_amuna_female_down_1_basic"] = player_fighter_amuna_female_down_basic_sheet[0]
    loaded_dict["player_fighter_amuna_female_down_2_basic"] = player_fighter_amuna_female_down_basic_sheet[1]
    loaded_dict["player_fighter_amuna_female_down_3_basic"] = player_fighter_amuna_female_down_basic_sheet[2]
    loaded_dict["player_fighter_amuna_female_down_4_basic"] = player_fighter_amuna_female_down_basic_sheet[3]
    # forged
    player_fighter_amuna_female_down_forged_url = resource_path('resources/art/'
                                                                'player_fighter_amuna_down_female_forged.png')
    player_fighter_amuna_female_down_forged_sheet = sprite_sheet((50, 75), player_fighter_amuna_female_down_forged_url)
    loaded_dict["player_fighter_amuna_female_down_1_forged"] = player_fighter_amuna_female_down_forged_sheet[0]
    loaded_dict["player_fighter_amuna_female_down_2_forged"] = player_fighter_amuna_female_down_forged_sheet[1]
    loaded_dict["player_fighter_amuna_female_down_3_forged"] = player_fighter_amuna_female_down_forged_sheet[2]
    loaded_dict["player_fighter_amuna_female_down_4_forged"] = player_fighter_amuna_female_down_forged_sheet[3]
    # mythic
    player_fighter_amuna_female_down_mythic_url = resource_path('resources/art/'
                                                                'player_fighter_amuna_down_female_mythic.png')
    player_fighter_amuna_female_down_mythic_sheet = sprite_sheet((50, 75), player_fighter_amuna_female_down_mythic_url)
    loaded_dict["player_fighter_amuna_female_down_1_mythic"] = player_fighter_amuna_female_down_mythic_sheet[0]
    loaded_dict["player_fighter_amuna_female_down_2_mythic"] = player_fighter_amuna_female_down_mythic_sheet[1]
    loaded_dict["player_fighter_amuna_female_down_3_mythic"] = player_fighter_amuna_female_down_mythic_sheet[2]
    loaded_dict["player_fighter_amuna_female_down_4_mythic"] = player_fighter_amuna_female_down_mythic_sheet[3]
    # legend
    player_fighter_amuna_female_down_legend_url = resource_path('resources/art/'
                                                                'player_fighter_amuna_down_female_legend.png')
    player_fighter_amuna_female_down_legend_sheet = sprite_sheet((50, 75), player_fighter_amuna_female_down_legend_url)
    loaded_dict["player_fighter_amuna_female_down_1_legend"] = player_fighter_amuna_female_down_legend_sheet[0]
    loaded_dict["player_fighter_amuna_female_down_2_legend"] = player_fighter_amuna_female_down_legend_sheet[1]
    loaded_dict["player_fighter_amuna_female_down_3_legend"] = player_fighter_amuna_female_down_legend_sheet[2]
    loaded_dict["player_fighter_amuna_female_down_4_legend"] = player_fighter_amuna_female_down_legend_sheet[3]
    player_fighter_amuna_female_up_url = resource_path('resources/art/player_fighter_amuna_up_female.png')
    player_fighter_amuna_female_up_sheet = sprite_sheet((50, 75), player_fighter_amuna_female_up_url)
    loaded_dict["player_fighter_amuna_female_up_1"] = player_fighter_amuna_female_up_sheet[0]
    loaded_dict["player_fighter_amuna_female_up_2"] = player_fighter_amuna_female_up_sheet[1]
    loaded_dict["player_fighter_amuna_female_up_3"] = player_fighter_amuna_female_up_sheet[2]
    loaded_dict["player_fighter_amuna_female_up_4"] = player_fighter_amuna_female_up_sheet[3]
    # basic
    player_fighter_amuna_female_up_basic_url = resource_path('resources/art/player_fighter_amuna_up_female_basic.png')
    player_fighter_amuna_female_up_basic_sheet = sprite_sheet((50, 75), player_fighter_amuna_female_up_basic_url)
    loaded_dict["player_fighter_amuna_female_up_1_basic"] = player_fighter_amuna_female_up_basic_sheet[0]
    loaded_dict["player_fighter_amuna_female_up_2_basic"] = player_fighter_amuna_female_up_basic_sheet[1]
    loaded_dict["player_fighter_amuna_female_up_3_basic"] = player_fighter_amuna_female_up_basic_sheet[2]
    loaded_dict["player_fighter_amuna_female_up_4_basic"] = player_fighter_amuna_female_up_basic_sheet[3]
    # forged
    player_fighter_amuna_female_up_forged_url = resource_path('resources/art/player_fighter_amuna_up_female_forged.png')
    player_fighter_amuna_female_up_forged_sheet = sprite_sheet((50, 75), player_fighter_amuna_female_up_forged_url)
    loaded_dict["player_fighter_amuna_female_up_1_forged"] = player_fighter_amuna_female_up_forged_sheet[0]
    loaded_dict["player_fighter_amuna_female_up_2_forged"] = player_fighter_amuna_female_up_forged_sheet[1]
    loaded_dict["player_fighter_amuna_female_up_3_forged"] = player_fighter_amuna_female_up_forged_sheet[2]
    loaded_dict["player_fighter_amuna_female_up_4_forged"] = player_fighter_amuna_female_up_forged_sheet[3]
    # mythic
    player_fighter_amuna_female_up_mythic_url = resource_path('resources/art/player_fighter_amuna_up_female_mythic.png')
    player_fighter_amuna_female_up_mythic_sheet = sprite_sheet((50, 75), player_fighter_amuna_female_up_mythic_url)
    loaded_dict["player_fighter_amuna_female_up_1_mythic"] = player_fighter_amuna_female_up_mythic_sheet[0]
    loaded_dict["player_fighter_amuna_female_up_2_mythic"] = player_fighter_amuna_female_up_mythic_sheet[1]
    loaded_dict["player_fighter_amuna_female_up_3_mythic"] = player_fighter_amuna_female_up_mythic_sheet[2]
    loaded_dict["player_fighter_amuna_female_up_4_mythic"] = player_fighter_amuna_female_up_mythic_sheet[3]
    # legend
    player_fighter_amuna_female_up_legend_url = resource_path('resources/art/player_fighter_amuna_up_female_legend.png')
    player_fighter_amuna_female_up_legend_sheet = sprite_sheet((50, 75), player_fighter_amuna_female_up_legend_url)
    loaded_dict["player_fighter_amuna_female_up_1_legend"] = player_fighter_amuna_female_up_legend_sheet[0]
    loaded_dict["player_fighter_amuna_female_up_2_legend"] = player_fighter_amuna_female_up_legend_sheet[1]
    loaded_dict["player_fighter_amuna_female_up_3_legend"] = player_fighter_amuna_female_up_legend_sheet[2]
    loaded_dict["player_fighter_amuna_female_up_4_legend"] = player_fighter_amuna_female_up_legend_sheet[3]
    player_fighter_amuna_female_left_url = resource_path('resources/art/player_fighter_amuna_left_female.png')
    player_fighter_amuna_female_left_sheet = sprite_sheet((50, 75), player_fighter_amuna_female_left_url)
    loaded_dict["player_fighter_amuna_female_left_1"] = player_fighter_amuna_female_left_sheet[0]
    loaded_dict["player_fighter_amuna_female_left_2"] = player_fighter_amuna_female_left_sheet[1]
    loaded_dict["player_fighter_amuna_female_left_3"] = player_fighter_amuna_female_left_sheet[2]
    loaded_dict["player_fighter_amuna_female_left_4"] = player_fighter_amuna_female_left_sheet[3]
    # basic
    player_fighter_amuna_female_left_basic_url = resource_path('resources/art/'
                                                               'player_fighter_amuna_left_female_basic.png')
    player_fighter_amuna_female_left_basic_sheet = sprite_sheet((50, 75), player_fighter_amuna_female_left_basic_url)
    loaded_dict["player_fighter_amuna_female_left_1_basic"] = player_fighter_amuna_female_left_basic_sheet[0]
    loaded_dict["player_fighter_amuna_female_left_2_basic"] = player_fighter_amuna_female_left_basic_sheet[1]
    loaded_dict["player_fighter_amuna_female_left_3_basic"] = player_fighter_amuna_female_left_basic_sheet[2]
    loaded_dict["player_fighter_amuna_female_left_4_basic"] = player_fighter_amuna_female_left_basic_sheet[3]
    # forged
    player_fighter_amuna_female_left_forged_url = resource_path('resources/art/'
                                                                'player_fighter_amuna_left_female_forged.png')
    player_fighter_amuna_female_left_forged_sheet = sprite_sheet((50, 75), player_fighter_amuna_female_left_forged_url)
    loaded_dict["player_fighter_amuna_female_left_1_forged"] = player_fighter_amuna_female_left_forged_sheet[0]
    loaded_dict["player_fighter_amuna_female_left_2_forged"] = player_fighter_amuna_female_left_forged_sheet[1]
    loaded_dict["player_fighter_amuna_female_left_3_forged"] = player_fighter_amuna_female_left_forged_sheet[2]
    loaded_dict["player_fighter_amuna_female_left_4_forged"] = player_fighter_amuna_female_left_forged_sheet[3]
    # mythic
    player_fighter_amuna_female_left_mythic_url = resource_path('resources/art/'
                                                                'player_fighter_amuna_left_female_mythic.png')
    player_fighter_amuna_female_left_mythic_sheet = sprite_sheet((50, 75), player_fighter_amuna_female_left_mythic_url)
    loaded_dict["player_fighter_amuna_female_left_1_mythic"] = player_fighter_amuna_female_left_mythic_sheet[0]
    loaded_dict["player_fighter_amuna_female_left_2_mythic"] = player_fighter_amuna_female_left_mythic_sheet[1]
    loaded_dict["player_fighter_amuna_female_left_3_mythic"] = player_fighter_amuna_female_left_mythic_sheet[2]
    loaded_dict["player_fighter_amuna_female_left_4_mythic"] = player_fighter_amuna_female_left_mythic_sheet[3]
    # legend
    player_fighter_amuna_female_left_legend_url = resource_path('resources/art/'
                                                                'player_fighter_amuna_left_female_legend.png')
    player_fighter_amuna_female_left_legend_sheet = sprite_sheet((50, 75), player_fighter_amuna_female_left_legend_url)
    loaded_dict["player_fighter_amuna_female_left_1_legend"] = player_fighter_amuna_female_left_legend_sheet[0]
    loaded_dict["player_fighter_amuna_female_left_2_legend"] = player_fighter_amuna_female_left_legend_sheet[1]
    loaded_dict["player_fighter_amuna_female_left_3_legend"] = player_fighter_amuna_female_left_legend_sheet[2]
    loaded_dict["player_fighter_amuna_female_left_4_legend"] = player_fighter_amuna_female_left_legend_sheet[3]
    player_fighter_amuna_female_right_url = resource_path('resources/art/player_fighter_amuna_right_female.png')
    player_fighter_amuna_female_right_sheet = sprite_sheet((50, 75), player_fighter_amuna_female_right_url)
    loaded_dict["player_fighter_amuna_female_right_1"] = player_fighter_amuna_female_right_sheet[0]
    loaded_dict["player_fighter_amuna_female_right_2"] = player_fighter_amuna_female_right_sheet[1]
    loaded_dict["player_fighter_amuna_female_right_3"] = player_fighter_amuna_female_right_sheet[2]
    loaded_dict["player_fighter_amuna_female_right_4"] = player_fighter_amuna_female_right_sheet[3]
    # basic
    player_fighter_amuna_female_right_basic_url = resource_path('resources/art/'
                                                                'player_fighter_amuna_right_female_basic.png')
    player_fighter_amuna_female_right_basic_sheet = sprite_sheet((50, 75), player_fighter_amuna_female_right_basic_url)
    loaded_dict["player_fighter_amuna_female_right_1_basic"] = player_fighter_amuna_female_right_basic_sheet[0]
    loaded_dict["player_fighter_amuna_female_right_2_basic"] = player_fighter_amuna_female_right_basic_sheet[1]
    loaded_dict["player_fighter_amuna_female_right_3_basic"] = player_fighter_amuna_female_right_basic_sheet[2]
    loaded_dict["player_fighter_amuna_female_right_4_basic"] = player_fighter_amuna_female_right_basic_sheet[3]
    # forged
    player_fighter_amuna_female_right_forged_url = resource_path('resources/art/'
                                                                 'player_fighter_amuna_right_female_forged.png')
    player_fighter_amuna_female_right_forged_sheet = sprite_sheet((50, 75),
                                                                  player_fighter_amuna_female_right_forged_url)
    loaded_dict["player_fighter_amuna_female_right_1_forged"] = player_fighter_amuna_female_right_forged_sheet[0]
    loaded_dict["player_fighter_amuna_female_right_2_forged"] = player_fighter_amuna_female_right_forged_sheet[1]
    loaded_dict["player_fighter_amuna_female_right_3_forged"] = player_fighter_amuna_female_right_forged_sheet[2]
    loaded_dict["player_fighter_amuna_female_right_4_forged"] = player_fighter_amuna_female_right_forged_sheet[3]
    # mythic
    player_fighter_amuna_female_right_mythic_url = resource_path('resources/art/'
                                                                 'player_fighter_amuna_right_female_mythic.png')
    player_fighter_amuna_female_right_mythic_sheet = sprite_sheet((50, 75),
                                                                  player_fighter_amuna_female_right_mythic_url)
    loaded_dict["player_fighter_amuna_female_right_1_mythic"] = player_fighter_amuna_female_right_mythic_sheet[0]
    loaded_dict["player_fighter_amuna_female_right_2_mythic"] = player_fighter_amuna_female_right_mythic_sheet[1]
    loaded_dict["player_fighter_amuna_female_right_3_mythic"] = player_fighter_amuna_female_right_mythic_sheet[2]
    loaded_dict["player_fighter_amuna_female_right_4_mythic"] = player_fighter_amuna_female_right_mythic_sheet[3]
    # legend
    player_fighter_amuna_female_right_legend_url = resource_path('resources/art/'
                                                                 'player_fighter_amuna_right_female_legend.png')
    player_fighter_amuna_female_right_legend_sheet = sprite_sheet((50, 75),
                                                                  player_fighter_amuna_female_right_legend_url)
    loaded_dict["player_fighter_amuna_female_right_1_legend"] = player_fighter_amuna_female_right_legend_sheet[0]
    loaded_dict["player_fighter_amuna_female_right_2_legend"] = player_fighter_amuna_female_right_legend_sheet[1]
    loaded_dict["player_fighter_amuna_female_right_3_legend"] = player_fighter_amuna_female_right_legend_sheet[2]
    loaded_dict["player_fighter_amuna_female_right_4_legend"] = player_fighter_amuna_female_right_legend_sheet[3]

    # player fighter nuldar race ---------------------------------------------------------------------------------------
    # male -------------------------------------------------------------------------------------------------------------
    player_fighter_nuldar_down_url = resource_path('resources/art/player_fighter_nuldar_down_male.png')
    player_fighter_nuldar_down_sheet = sprite_sheet((50, 75), player_fighter_nuldar_down_url)
    loaded_dict["player_fighter_nuldar_male_down_1"] = player_fighter_nuldar_down_sheet[0]
    loaded_dict["player_fighter_nuldar_male_down_2"] = player_fighter_nuldar_down_sheet[1]
    loaded_dict["player_fighter_nuldar_male_down_3"] = player_fighter_nuldar_down_sheet[2]
    loaded_dict["player_fighter_nuldar_male_down_4"] = player_fighter_nuldar_down_sheet[3]
    # basic
    player_fighter_nuldar_down_basic_url = resource_path('resources/art/player_fighter_nuldar_down_male_basic.png')
    player_fighter_nuldar_down_basic_sheet = sprite_sheet((50, 75), player_fighter_nuldar_down_basic_url)
    loaded_dict["player_fighter_nuldar_male_down_1_basic"] = player_fighter_nuldar_down_basic_sheet[0]
    loaded_dict["player_fighter_nuldar_male_down_2_basic"] = player_fighter_nuldar_down_basic_sheet[1]
    loaded_dict["player_fighter_nuldar_male_down_3_basic"] = player_fighter_nuldar_down_basic_sheet[2]
    loaded_dict["player_fighter_nuldar_male_down_4_basic"] = player_fighter_nuldar_down_basic_sheet[3]
    # forged
    player_fighter_nuldar_down_forged_url = resource_path('resources/art/player_fighter_nuldar_down_male_forged.png')
    player_fighter_nuldar_down_forged_sheet = sprite_sheet((50, 75), player_fighter_nuldar_down_forged_url)
    loaded_dict["player_fighter_nuldar_male_down_1_forged"] = player_fighter_nuldar_down_forged_sheet[0]
    loaded_dict["player_fighter_nuldar_male_down_2_forged"] = player_fighter_nuldar_down_forged_sheet[1]
    loaded_dict["player_fighter_nuldar_male_down_3_forged"] = player_fighter_nuldar_down_forged_sheet[2]
    loaded_dict["player_fighter_nuldar_male_down_4_forged"] = player_fighter_nuldar_down_forged_sheet[3]
    # mythic
    player_fighter_nuldar_down_mythic_url = resource_path('resources/art/player_fighter_nuldar_down_male_mythic.png')
    player_fighter_nuldar_down_mythic_sheet = sprite_sheet((50, 75), player_fighter_nuldar_down_mythic_url)
    loaded_dict["player_fighter_nuldar_male_down_1_mythic"] = player_fighter_nuldar_down_mythic_sheet[0]
    loaded_dict["player_fighter_nuldar_male_down_2_mythic"] = player_fighter_nuldar_down_mythic_sheet[1]
    loaded_dict["player_fighter_nuldar_male_down_3_mythic"] = player_fighter_nuldar_down_mythic_sheet[2]
    loaded_dict["player_fighter_nuldar_male_down_4_mythic"] = player_fighter_nuldar_down_mythic_sheet[3]
    # legend
    player_fighter_nuldar_down_legend_url = resource_path('resources/art/player_fighter_nuldar_down_male_legend.png')
    player_fighter_nuldar_down_legend_sheet = sprite_sheet((50, 75), player_fighter_nuldar_down_legend_url)
    loaded_dict["player_fighter_nuldar_male_down_1_legend"] = player_fighter_nuldar_down_legend_sheet[0]
    loaded_dict["player_fighter_nuldar_male_down_2_legend"] = player_fighter_nuldar_down_legend_sheet[1]
    loaded_dict["player_fighter_nuldar_male_down_3_legend"] = player_fighter_nuldar_down_legend_sheet[2]
    loaded_dict["player_fighter_nuldar_male_down_4_legend"] = player_fighter_nuldar_down_legend_sheet[3]
    player_fighter_nuldar_up_url = resource_path('resources/art/player_fighter_nuldar_up_male.png')
    player_fighter_nuldar_up_sheet = sprite_sheet((50, 75), player_fighter_nuldar_up_url)
    loaded_dict["player_fighter_nuldar_male_up_1"] = player_fighter_nuldar_up_sheet[0]
    loaded_dict["player_fighter_nuldar_male_up_2"] = player_fighter_nuldar_up_sheet[1]
    loaded_dict["player_fighter_nuldar_male_up_3"] = player_fighter_nuldar_up_sheet[2]
    loaded_dict["player_fighter_nuldar_male_up_4"] = player_fighter_nuldar_up_sheet[3]
    # basic
    player_fighter_nuldar_up_basic_url = resource_path('resources/art/player_fighter_nuldar_up_male_basic.png')
    player_fighter_nuldar_up_basic_sheet = sprite_sheet((50, 75), player_fighter_nuldar_up_basic_url)
    loaded_dict["player_fighter_nuldar_male_up_1_basic"] = player_fighter_nuldar_up_basic_sheet[0]
    loaded_dict["player_fighter_nuldar_male_up_2_basic"] = player_fighter_nuldar_up_basic_sheet[1]
    loaded_dict["player_fighter_nuldar_male_up_3_basic"] = player_fighter_nuldar_up_basic_sheet[2]
    loaded_dict["player_fighter_nuldar_male_up_4_basic"] = player_fighter_nuldar_up_basic_sheet[3]
    # forged
    player_fighter_nuldar_up_forged_url = resource_path('resources/art/player_fighter_nuldar_up_male_forged.png')
    player_fighter_nuldar_up_forged_sheet = sprite_sheet((50, 75), player_fighter_nuldar_up_forged_url)
    loaded_dict["player_fighter_nuldar_male_up_1_forged"] = player_fighter_nuldar_up_forged_sheet[0]
    loaded_dict["player_fighter_nuldar_male_up_2_forged"] = player_fighter_nuldar_up_forged_sheet[1]
    loaded_dict["player_fighter_nuldar_male_up_3_forged"] = player_fighter_nuldar_up_forged_sheet[2]
    loaded_dict["player_fighter_nuldar_male_up_4_forged"] = player_fighter_nuldar_up_forged_sheet[3]
    # mythic
    player_fighter_nuldar_up_mythic_url = resource_path('resources/art/player_fighter_nuldar_up_male_mythic.png')
    player_fighter_nuldar_up_mythic_sheet = sprite_sheet((50, 75), player_fighter_nuldar_up_mythic_url)
    loaded_dict["player_fighter_nuldar_male_up_1_mythic"] = player_fighter_nuldar_up_mythic_sheet[0]
    loaded_dict["player_fighter_nuldar_male_up_2_mythic"] = player_fighter_nuldar_up_mythic_sheet[1]
    loaded_dict["player_fighter_nuldar_male_up_3_mythic"] = player_fighter_nuldar_up_mythic_sheet[2]
    loaded_dict["player_fighter_nuldar_male_up_4_mythic"] = player_fighter_nuldar_up_mythic_sheet[3]
    # legend
    player_fighter_nuldar_up_legend_url = resource_path('resources/art/player_fighter_nuldar_up_male_legend.png')
    player_fighter_nuldar_up_legend_sheet = sprite_sheet((50, 75), player_fighter_nuldar_up_legend_url)
    loaded_dict["player_fighter_nuldar_male_up_1_legend"] = player_fighter_nuldar_up_legend_sheet[0]
    loaded_dict["player_fighter_nuldar_male_up_2_legend"] = player_fighter_nuldar_up_legend_sheet[1]
    loaded_dict["player_fighter_nuldar_male_up_3_legend"] = player_fighter_nuldar_up_legend_sheet[2]
    loaded_dict["player_fighter_nuldar_male_up_4_legend"] = player_fighter_nuldar_up_legend_sheet[3]
    player_fighter_nuldar_left_url = resource_path('resources/art/player_fighter_nuldar_left_male.png')
    player_fighter_nuldar_left_sheet = sprite_sheet((50, 75), player_fighter_nuldar_left_url)
    loaded_dict["player_fighter_nuldar_male_left_1"] = player_fighter_nuldar_left_sheet[0]
    loaded_dict["player_fighter_nuldar_male_left_2"] = player_fighter_nuldar_left_sheet[1]
    loaded_dict["player_fighter_nuldar_male_left_3"] = player_fighter_nuldar_left_sheet[2]
    loaded_dict["player_fighter_nuldar_male_left_4"] = player_fighter_nuldar_left_sheet[3]
    # basic
    player_fighter_nuldar_left_basic_url = resource_path('resources/art/player_fighter_nuldar_left_male_basic.png')
    player_fighter_nuldar_left_basic_sheet = sprite_sheet((50, 75), player_fighter_nuldar_left_basic_url)
    loaded_dict["player_fighter_nuldar_male_left_1_basic"] = player_fighter_nuldar_left_basic_sheet[0]
    loaded_dict["player_fighter_nuldar_male_left_2_basic"] = player_fighter_nuldar_left_basic_sheet[1]
    loaded_dict["player_fighter_nuldar_male_left_3_basic"] = player_fighter_nuldar_left_basic_sheet[2]
    loaded_dict["player_fighter_nuldar_male_left_4_basic"] = player_fighter_nuldar_left_basic_sheet[3]
    # forged
    player_fighter_nuldar_left_forged_url = resource_path('resources/art/player_fighter_nuldar_left_male_forged.png')
    player_fighter_nuldar_left_forged_sheet = sprite_sheet((50, 75), player_fighter_nuldar_left_forged_url)
    loaded_dict["player_fighter_nuldar_male_left_1_forged"] = player_fighter_nuldar_left_forged_sheet[0]
    loaded_dict["player_fighter_nuldar_male_left_2_forged"] = player_fighter_nuldar_left_forged_sheet[1]
    loaded_dict["player_fighter_nuldar_male_left_3_forged"] = player_fighter_nuldar_left_forged_sheet[2]
    loaded_dict["player_fighter_nuldar_male_left_4_forged"] = player_fighter_nuldar_left_forged_sheet[3]
    # mythic
    player_fighter_nuldar_left_mythic_url = resource_path('resources/art/player_fighter_nuldar_left_male_mythic.png')
    player_fighter_nuldar_left_mythic_sheet = sprite_sheet((50, 75), player_fighter_nuldar_left_mythic_url)
    loaded_dict["player_fighter_nuldar_male_left_1_mythic"] = player_fighter_nuldar_left_mythic_sheet[0]
    loaded_dict["player_fighter_nuldar_male_left_2_mythic"] = player_fighter_nuldar_left_mythic_sheet[1]
    loaded_dict["player_fighter_nuldar_male_left_3_mythic"] = player_fighter_nuldar_left_mythic_sheet[2]
    loaded_dict["player_fighter_nuldar_male_left_4_mythic"] = player_fighter_nuldar_left_mythic_sheet[3]
    # legend
    player_fighter_nuldar_left_legend_url = resource_path('resources/art/player_fighter_nuldar_left_male_legend.png')
    player_fighter_nuldar_left_legend_sheet = sprite_sheet((50, 75), player_fighter_nuldar_left_legend_url)
    loaded_dict["player_fighter_nuldar_male_left_1_legend"] = player_fighter_nuldar_left_legend_sheet[0]
    loaded_dict["player_fighter_nuldar_male_left_2_legend"] = player_fighter_nuldar_left_legend_sheet[1]
    loaded_dict["player_fighter_nuldar_male_left_3_legend"] = player_fighter_nuldar_left_legend_sheet[2]
    loaded_dict["player_fighter_nuldar_male_left_4_legend"] = player_fighter_nuldar_left_legend_sheet[3]
    player_fighter_nuldar_right_url = resource_path('resources/art/player_fighter_nuldar_right_male.png')
    player_fighter_nuldar_right_sheet = sprite_sheet((50, 75), player_fighter_nuldar_right_url)
    loaded_dict["player_fighter_nuldar_male_right_1"] = player_fighter_nuldar_right_sheet[0]
    loaded_dict["player_fighter_nuldar_male_right_2"] = player_fighter_nuldar_right_sheet[1]
    loaded_dict["player_fighter_nuldar_male_right_3"] = player_fighter_nuldar_right_sheet[2]
    loaded_dict["player_fighter_nuldar_male_right_4"] = player_fighter_nuldar_right_sheet[3]
    # basic
    player_fighter_nuldar_right_basic_url = resource_path('resources/art/player_fighter_nuldar_right_male_basic.png')
    player_fighter_nuldar_right_basic_sheet = sprite_sheet((50, 75), player_fighter_nuldar_right_basic_url)
    loaded_dict["player_fighter_nuldar_male_right_1_basic"] = player_fighter_nuldar_right_basic_sheet[0]
    loaded_dict["player_fighter_nuldar_male_right_2_basic"] = player_fighter_nuldar_right_basic_sheet[1]
    loaded_dict["player_fighter_nuldar_male_right_3_basic"] = player_fighter_nuldar_right_basic_sheet[2]
    loaded_dict["player_fighter_nuldar_male_right_4_basic"] = player_fighter_nuldar_right_basic_sheet[3]
    # forged
    player_fighter_nuldar_right_forged_url = resource_path('resources/art/player_fighter_nuldar_right_male_forged.png')
    player_fighter_nuldar_right_forged_sheet = sprite_sheet((50, 75), player_fighter_nuldar_right_forged_url)
    loaded_dict["player_fighter_nuldar_male_right_1_forged"] = player_fighter_nuldar_right_forged_sheet[0]
    loaded_dict["player_fighter_nuldar_male_right_2_forged"] = player_fighter_nuldar_right_forged_sheet[1]
    loaded_dict["player_fighter_nuldar_male_right_3_forged"] = player_fighter_nuldar_right_forged_sheet[2]
    loaded_dict["player_fighter_nuldar_male_right_4_forged"] = player_fighter_nuldar_right_forged_sheet[3]
    # mythic
    player_fighter_nuldar_right_mythic_url = resource_path('resources/art/player_fighter_nuldar_right_male_mythic.png')
    player_fighter_nuldar_right_mythic_sheet = sprite_sheet((50, 75), player_fighter_nuldar_right_mythic_url)
    loaded_dict["player_fighter_nuldar_male_right_1_mythic"] = player_fighter_nuldar_right_mythic_sheet[0]
    loaded_dict["player_fighter_nuldar_male_right_2_mythic"] = player_fighter_nuldar_right_mythic_sheet[1]
    loaded_dict["player_fighter_nuldar_male_right_3_mythic"] = player_fighter_nuldar_right_mythic_sheet[2]
    loaded_dict["player_fighter_nuldar_male_right_4_mythic"] = player_fighter_nuldar_right_mythic_sheet[3]
    # legend
    player_fighter_nuldar_right_legend_url = resource_path('resources/art/player_fighter_nuldar_right_male_legend.png')
    player_fighter_nuldar_right_legend_sheet = sprite_sheet((50, 75), player_fighter_nuldar_right_legend_url)
    loaded_dict["player_fighter_nuldar_male_right_1_legend"] = player_fighter_nuldar_right_legend_sheet[0]
    loaded_dict["player_fighter_nuldar_male_right_2_legend"] = player_fighter_nuldar_right_legend_sheet[1]
    loaded_dict["player_fighter_nuldar_male_right_3_legend"] = player_fighter_nuldar_right_legend_sheet[2]
    loaded_dict["player_fighter_nuldar_male_right_4_legend"] = player_fighter_nuldar_right_legend_sheet[3]
    # female -----------------------------------------------------------------------------------------------------------
    player_fighter_nuldar_female_down_url = resource_path('resources/art/player_fighter_nuldar_down_female.png')
    player_fighter_nuldar_female_down_sheet = sprite_sheet((50, 75), player_fighter_nuldar_female_down_url)
    loaded_dict["player_fighter_nuldar_female_down_1"] = player_fighter_nuldar_female_down_sheet[0]
    loaded_dict["player_fighter_nuldar_female_down_2"] = player_fighter_nuldar_female_down_sheet[1]
    loaded_dict["player_fighter_nuldar_female_down_3"] = player_fighter_nuldar_female_down_sheet[2]
    loaded_dict["player_fighter_nuldar_female_down_4"] = player_fighter_nuldar_female_down_sheet[3]
    # basic
    player_fighter_nuldar_female_down_basic_url = resource_path('resources/art/'
                                                                'player_fighter_nuldar_down_female_basic.png')
    player_fighter_nuldar_female_down_basic_sheet = sprite_sheet((50, 75), player_fighter_nuldar_female_down_basic_url)
    loaded_dict["player_fighter_nuldar_female_down_1_basic"] = player_fighter_nuldar_female_down_basic_sheet[0]
    loaded_dict["player_fighter_nuldar_female_down_2_basic"] = player_fighter_nuldar_female_down_basic_sheet[1]
    loaded_dict["player_fighter_nuldar_female_down_3_basic"] = player_fighter_nuldar_female_down_basic_sheet[2]
    loaded_dict["player_fighter_nuldar_female_down_4_basic"] = player_fighter_nuldar_female_down_basic_sheet[3]
    # forged
    player_fighter_nuldar_female_down_forged_url = resource_path('resources/art/'
                                                                 'player_fighter_nuldar_down_female_forged.png')
    player_fighter_nuldar_female_down_forged_sheet = sprite_sheet((50, 75),
                                                                  player_fighter_nuldar_female_down_forged_url)
    loaded_dict["player_fighter_nuldar_female_down_1_forged"] = player_fighter_nuldar_female_down_forged_sheet[0]
    loaded_dict["player_fighter_nuldar_female_down_2_forged"] = player_fighter_nuldar_female_down_forged_sheet[1]
    loaded_dict["player_fighter_nuldar_female_down_3_forged"] = player_fighter_nuldar_female_down_forged_sheet[2]
    loaded_dict["player_fighter_nuldar_female_down_4_forged"] = player_fighter_nuldar_female_down_forged_sheet[3]
    # mythic
    player_fighter_nuldar_female_down_mythic_url = resource_path('resources/art/'
                                                                 'player_fighter_nuldar_down_female_mythic.png')
    player_fighter_nuldar_female_down_mythic_sheet = sprite_sheet((50, 75),
                                                                  player_fighter_nuldar_female_down_mythic_url)
    loaded_dict["player_fighter_nuldar_female_down_1_mythic"] = player_fighter_nuldar_female_down_mythic_sheet[0]
    loaded_dict["player_fighter_nuldar_female_down_2_mythic"] = player_fighter_nuldar_female_down_mythic_sheet[1]
    loaded_dict["player_fighter_nuldar_female_down_3_mythic"] = player_fighter_nuldar_female_down_mythic_sheet[2]
    loaded_dict["player_fighter_nuldar_female_down_4_mythic"] = player_fighter_nuldar_female_down_mythic_sheet[3]
    # legend
    player_fighter_nuldar_female_down_legend_url = resource_path('resources/art/'
                                                                 'player_fighter_nuldar_down_female_legend.png')
    player_fighter_nuldar_female_down_legend_sheet = sprite_sheet((50, 75),
                                                                  player_fighter_nuldar_female_down_legend_url)
    loaded_dict["player_fighter_nuldar_female_down_1_legend"] = player_fighter_nuldar_female_down_legend_sheet[0]
    loaded_dict["player_fighter_nuldar_female_down_2_legend"] = player_fighter_nuldar_female_down_legend_sheet[1]
    loaded_dict["player_fighter_nuldar_female_down_3_legend"] = player_fighter_nuldar_female_down_legend_sheet[2]
    loaded_dict["player_fighter_nuldar_female_down_4_legend"] = player_fighter_nuldar_female_down_legend_sheet[3]
    player_fighter_nuldar_female_up_url = resource_path('resources/art/player_fighter_nuldar_up_female.png')
    player_fighter_nuldar_female_up_sheet = sprite_sheet((50, 75), player_fighter_nuldar_female_up_url)
    loaded_dict["player_fighter_nuldar_female_up_1"] = player_fighter_nuldar_female_up_sheet[0]
    loaded_dict["player_fighter_nuldar_female_up_2"] = player_fighter_nuldar_female_up_sheet[1]
    loaded_dict["player_fighter_nuldar_female_up_3"] = player_fighter_nuldar_female_up_sheet[2]
    loaded_dict["player_fighter_nuldar_female_up_4"] = player_fighter_nuldar_female_up_sheet[3]
    # basic
    player_fighter_nuldar_female_up_basic_url = resource_path('resources/art/player_fighter_nuldar_up_female_basic.png')
    player_fighter_nuldar_female_up_basic_sheet = sprite_sheet((50, 75), player_fighter_nuldar_female_up_basic_url)
    loaded_dict["player_fighter_nuldar_female_up_1_basic"] = player_fighter_nuldar_female_up_basic_sheet[0]
    loaded_dict["player_fighter_nuldar_female_up_2_basic"] = player_fighter_nuldar_female_up_basic_sheet[1]
    loaded_dict["player_fighter_nuldar_female_up_3_basic"] = player_fighter_nuldar_female_up_basic_sheet[2]
    loaded_dict["player_fighter_nuldar_female_up_4_basic"] = player_fighter_nuldar_female_up_basic_sheet[3]
    # forged
    player_fighter_nuldar_female_up_forged_url = resource_path('resources/art/'
                                                               'player_fighter_nuldar_up_female_forged.png')
    player_fighter_nuldar_female_up_forged_sheet = sprite_sheet((50, 75), player_fighter_nuldar_female_up_forged_url)
    loaded_dict["player_fighter_nuldar_female_up_1_forged"] = player_fighter_nuldar_female_up_forged_sheet[0]
    loaded_dict["player_fighter_nuldar_female_up_2_forged"] = player_fighter_nuldar_female_up_forged_sheet[1]
    loaded_dict["player_fighter_nuldar_female_up_3_forged"] = player_fighter_nuldar_female_up_forged_sheet[2]
    loaded_dict["player_fighter_nuldar_female_up_4_forged"] = player_fighter_nuldar_female_up_forged_sheet[3]
    # mythic
    player_fighter_nuldar_female_up_mythic_url = resource_path('resources/art/'
                                                               'player_fighter_nuldar_up_female_mythic.png')
    player_fighter_nuldar_female_up_mythic_sheet = sprite_sheet((50, 75), player_fighter_nuldar_female_up_mythic_url)
    loaded_dict["player_fighter_nuldar_female_up_1_mythic"] = player_fighter_nuldar_female_up_mythic_sheet[0]
    loaded_dict["player_fighter_nuldar_female_up_2_mythic"] = player_fighter_nuldar_female_up_mythic_sheet[1]
    loaded_dict["player_fighter_nuldar_female_up_3_mythic"] = player_fighter_nuldar_female_up_mythic_sheet[2]
    loaded_dict["player_fighter_nuldar_female_up_4_mythic"] = player_fighter_nuldar_female_up_mythic_sheet[3]
    # legend
    player_fighter_nuldar_female_up_legend_url = resource_path('resources/art/'
                                                               'player_fighter_nuldar_up_female_legend.png')
    player_fighter_nuldar_female_up_legend_sheet = sprite_sheet((50, 75), player_fighter_nuldar_female_up_legend_url)
    loaded_dict["player_fighter_nuldar_female_up_1_legend"] = player_fighter_nuldar_female_up_legend_sheet[0]
    loaded_dict["player_fighter_nuldar_female_up_2_legend"] = player_fighter_nuldar_female_up_legend_sheet[1]
    loaded_dict["player_fighter_nuldar_female_up_3_legend"] = player_fighter_nuldar_female_up_legend_sheet[2]
    loaded_dict["player_fighter_nuldar_female_up_4_legend"] = player_fighter_nuldar_female_up_legend_sheet[3]
    player_fighter_nuldar_female_left_url = resource_path('resources/art/player_fighter_nuldar_left_female.png')
    player_fighter_nuldar_female_left_sheet = sprite_sheet((50, 75), player_fighter_nuldar_female_left_url)
    loaded_dict["player_fighter_nuldar_female_left_1"] = player_fighter_nuldar_female_left_sheet[0]
    loaded_dict["player_fighter_nuldar_female_left_2"] = player_fighter_nuldar_female_left_sheet[1]
    loaded_dict["player_fighter_nuldar_female_left_3"] = player_fighter_nuldar_female_left_sheet[2]
    loaded_dict["player_fighter_nuldar_female_left_4"] = player_fighter_nuldar_female_left_sheet[3]
    # basic
    player_fighter_nuldar_female_left_basic_url = resource_path('resources/art/'
                                                                'player_fighter_nuldar_left_female_basic.png')
    player_fighter_nuldar_female_left_basic_sheet = sprite_sheet((50, 75), player_fighter_nuldar_female_left_basic_url)
    loaded_dict["player_fighter_nuldar_female_left_1_basic"] = player_fighter_nuldar_female_left_basic_sheet[0]
    loaded_dict["player_fighter_nuldar_female_left_2_basic"] = player_fighter_nuldar_female_left_basic_sheet[1]
    loaded_dict["player_fighter_nuldar_female_left_3_basic"] = player_fighter_nuldar_female_left_basic_sheet[2]
    loaded_dict["player_fighter_nuldar_female_left_4_basic"] = player_fighter_nuldar_female_left_basic_sheet[3]
    # forged
    player_fighter_nuldar_female_left_forged_url = resource_path('resources/art/'
                                                                 'player_fighter_nuldar_left_female_forged.png')
    player_fighter_nuldar_female_left_forged_sheet = sprite_sheet((50, 75),
                                                                  player_fighter_nuldar_female_left_forged_url)
    loaded_dict["player_fighter_nuldar_female_left_1_forged"] = player_fighter_nuldar_female_left_forged_sheet[0]
    loaded_dict["player_fighter_nuldar_female_left_2_forged"] = player_fighter_nuldar_female_left_forged_sheet[1]
    loaded_dict["player_fighter_nuldar_female_left_3_forged"] = player_fighter_nuldar_female_left_forged_sheet[2]
    loaded_dict["player_fighter_nuldar_female_left_4_forged"] = player_fighter_nuldar_female_left_forged_sheet[3]
    # mythic
    player_fighter_nuldar_female_left_mythic_url = resource_path('resources/art/'
                                                                 'player_fighter_nuldar_left_female_mythic.png')
    player_fighter_nuldar_female_left_mythic_sheet = sprite_sheet((50, 75),
                                                                  player_fighter_nuldar_female_left_mythic_url)
    loaded_dict["player_fighter_nuldar_female_left_1_mythic"] = player_fighter_nuldar_female_left_mythic_sheet[0]
    loaded_dict["player_fighter_nuldar_female_left_2_mythic"] = player_fighter_nuldar_female_left_mythic_sheet[1]
    loaded_dict["player_fighter_nuldar_female_left_3_mythic"] = player_fighter_nuldar_female_left_mythic_sheet[2]
    loaded_dict["player_fighter_nuldar_female_left_4_mythic"] = player_fighter_nuldar_female_left_mythic_sheet[3]
    # legend
    player_fighter_nuldar_female_left_legend_url = resource_path('resources/art/'
                                                                 'player_fighter_nuldar_left_female_legend.png')
    player_fighter_nuldar_female_left_legend_sheet = sprite_sheet((50, 75),
                                                                  player_fighter_nuldar_female_left_legend_url)
    loaded_dict["player_fighter_nuldar_female_left_1_legend"] = player_fighter_nuldar_female_left_legend_sheet[0]
    loaded_dict["player_fighter_nuldar_female_left_2_legend"] = player_fighter_nuldar_female_left_legend_sheet[1]
    loaded_dict["player_fighter_nuldar_female_left_3_legend"] = player_fighter_nuldar_female_left_legend_sheet[2]
    loaded_dict["player_fighter_nuldar_female_left_4_legend"] = player_fighter_nuldar_female_left_legend_sheet[3]
    player_fighter_nuldar_female_right_url = resource_path('resources/art/player_fighter_nuldar_right_female.png')
    player_fighter_nuldar_female_right_sheet = sprite_sheet((50, 75), player_fighter_nuldar_female_right_url)
    loaded_dict["player_fighter_nuldar_female_right_1"] = player_fighter_nuldar_female_right_sheet[0]
    loaded_dict["player_fighter_nuldar_female_right_2"] = player_fighter_nuldar_female_right_sheet[1]
    loaded_dict["player_fighter_nuldar_female_right_3"] = player_fighter_nuldar_female_right_sheet[2]
    loaded_dict["player_fighter_nuldar_female_right_4"] = player_fighter_nuldar_female_right_sheet[3]
    # basic
    player_fighter_nuldar_female_right_basic_url = resource_path('resources/art/'
                                                                 'player_fighter_nuldar_right_female_basic.png')
    player_fighter_nuldar_female_right_basic_sheet = sprite_sheet((50, 75),
                                                                  player_fighter_nuldar_female_right_basic_url)
    loaded_dict["player_fighter_nuldar_female_right_1_basic"] = player_fighter_nuldar_female_right_basic_sheet[0]
    loaded_dict["player_fighter_nuldar_female_right_2_basic"] = player_fighter_nuldar_female_right_basic_sheet[1]
    loaded_dict["player_fighter_nuldar_female_right_3_basic"] = player_fighter_nuldar_female_right_basic_sheet[2]
    loaded_dict["player_fighter_nuldar_female_right_4_basic"] = player_fighter_nuldar_female_right_basic_sheet[3]
    # forged
    player_fighter_nuldar_female_right_forged_url = resource_path('resources/art/player_fighter_nuldar_right_'
                                                                  'female_forged.png')
    player_fighter_nuldar_female_right_forged_sheet = sprite_sheet((50, 75),
                                                                   player_fighter_nuldar_female_right_forged_url)
    loaded_dict["player_fighter_nuldar_female_right_1_forged"] = player_fighter_nuldar_female_right_forged_sheet[0]
    loaded_dict["player_fighter_nuldar_female_right_2_forged"] = player_fighter_nuldar_female_right_forged_sheet[1]
    loaded_dict["player_fighter_nuldar_female_right_3_forged"] = player_fighter_nuldar_female_right_forged_sheet[2]
    loaded_dict["player_fighter_nuldar_female_right_4_forged"] = player_fighter_nuldar_female_right_forged_sheet[3]
    # mythic
    player_fighter_nuldar_female_right_mythic_url = resource_path('resources/art/player_fighter_nuldar_right_'
                                                                  'female_mythic.png')
    player_fighter_nuldar_female_right_mythic_sheet = sprite_sheet((50, 75),
                                                                   player_fighter_nuldar_female_right_mythic_url)
    loaded_dict["player_fighter_nuldar_female_right_1_mythic"] = player_fighter_nuldar_female_right_mythic_sheet[0]
    loaded_dict["player_fighter_nuldar_female_right_2_mythic"] = player_fighter_nuldar_female_right_mythic_sheet[1]
    loaded_dict["player_fighter_nuldar_female_right_3_mythic"] = player_fighter_nuldar_female_right_mythic_sheet[2]
    loaded_dict["player_fighter_nuldar_female_right_4_mythic"] = player_fighter_nuldar_female_right_mythic_sheet[3]
    # legend
    player_fighter_nuldar_female_right_legend_url = resource_path('resources/art/player_fighter_nuldar_right_'
                                                                  'female_legend.png')
    player_fighter_nuldar_female_right_legend_sheet = sprite_sheet((50, 75),
                                                                   player_fighter_nuldar_female_right_legend_url)
    loaded_dict["player_fighter_nuldar_female_right_1_legend"] = player_fighter_nuldar_female_right_legend_sheet[0]
    loaded_dict["player_fighter_nuldar_female_right_2_legend"] = player_fighter_nuldar_female_right_legend_sheet[1]
    loaded_dict["player_fighter_nuldar_female_right_3_legend"] = player_fighter_nuldar_female_right_legend_sheet[2]
    loaded_dict["player_fighter_nuldar_female_right_4_legend"] = player_fighter_nuldar_female_right_legend_sheet[3]

    # player fighter sorae race ----------------------------------------------------------------------------------------
    # alpha ------------------------------------------------------------------------------------------------------------
    player_fighter_sorae_down_url = resource_path('resources/art/player_fighter_sorae_down_a.png')
    player_fighter_sorae_down_sheet = sprite_sheet((50, 75), player_fighter_sorae_down_url)
    loaded_dict["player_fighter_sorae_a_down_1"] = player_fighter_sorae_down_sheet[0]
    loaded_dict["player_fighter_sorae_a_down_2"] = player_fighter_sorae_down_sheet[1]
    loaded_dict["player_fighter_sorae_a_down_3"] = player_fighter_sorae_down_sheet[2]
    loaded_dict["player_fighter_sorae_a_down_4"] = player_fighter_sorae_down_sheet[3]
    # basic
    player_fighter_sorae_down_basic_url = resource_path('resources/art/player_fighter_sorae_down_a_basic.png')
    player_fighter_sorae_down_basic_sheet = sprite_sheet((50, 75), player_fighter_sorae_down_basic_url)
    loaded_dict["player_fighter_sorae_a_down_1_basic"] = player_fighter_sorae_down_basic_sheet[0]
    loaded_dict["player_fighter_sorae_a_down_2_basic"] = player_fighter_sorae_down_basic_sheet[1]
    loaded_dict["player_fighter_sorae_a_down_3_basic"] = player_fighter_sorae_down_basic_sheet[2]
    loaded_dict["player_fighter_sorae_a_down_4_basic"] = player_fighter_sorae_down_basic_sheet[3]
    # forged
    player_fighter_sorae_down_forged_url = resource_path('resources/art/player_fighter_sorae_down_a_forged.png')
    player_fighter_sorae_down_forged_sheet = sprite_sheet((50, 75), player_fighter_sorae_down_forged_url)
    loaded_dict["player_fighter_sorae_a_down_1_forged"] = player_fighter_sorae_down_forged_sheet[0]
    loaded_dict["player_fighter_sorae_a_down_2_forged"] = player_fighter_sorae_down_forged_sheet[1]
    loaded_dict["player_fighter_sorae_a_down_3_forged"] = player_fighter_sorae_down_forged_sheet[2]
    loaded_dict["player_fighter_sorae_a_down_4_forged"] = player_fighter_sorae_down_forged_sheet[3]
    # mythic
    player_fighter_sorae_down_mythic_url = resource_path('resources/art/player_fighter_sorae_down_a_mythic.png')
    player_fighter_sorae_down_mythic_sheet = sprite_sheet((50, 75), player_fighter_sorae_down_mythic_url)
    loaded_dict["player_fighter_sorae_a_down_1_mythic"] = player_fighter_sorae_down_mythic_sheet[0]
    loaded_dict["player_fighter_sorae_a_down_2_mythic"] = player_fighter_sorae_down_mythic_sheet[1]
    loaded_dict["player_fighter_sorae_a_down_3_mythic"] = player_fighter_sorae_down_mythic_sheet[2]
    loaded_dict["player_fighter_sorae_a_down_4_mythic"] = player_fighter_sorae_down_mythic_sheet[3]
    # legend
    player_fighter_sorae_down_legend_url = resource_path('resources/art/player_fighter_sorae_down_a_legend.png')
    player_fighter_sorae_down_legend_sheet = sprite_sheet((50, 75), player_fighter_sorae_down_legend_url)
    loaded_dict["player_fighter_sorae_a_down_1_legend"] = player_fighter_sorae_down_legend_sheet[0]
    loaded_dict["player_fighter_sorae_a_down_2_legend"] = player_fighter_sorae_down_legend_sheet[1]
    loaded_dict["player_fighter_sorae_a_down_3_legend"] = player_fighter_sorae_down_legend_sheet[2]
    loaded_dict["player_fighter_sorae_a_down_4_legend"] = player_fighter_sorae_down_legend_sheet[3]
    player_fighter_sorae_up_url = resource_path('resources/art/player_fighter_sorae_up_a.png')
    player_fighter_sorae_up_sheet = sprite_sheet((50, 75), player_fighter_sorae_up_url)
    loaded_dict["player_fighter_sorae_a_up_1"] = player_fighter_sorae_up_sheet[0]
    loaded_dict["player_fighter_sorae_a_up_2"] = player_fighter_sorae_up_sheet[1]
    loaded_dict["player_fighter_sorae_a_up_3"] = player_fighter_sorae_up_sheet[2]
    loaded_dict["player_fighter_sorae_a_up_4"] = player_fighter_sorae_up_sheet[3]
    # basic
    player_fighter_sorae_up_basic_url = resource_path('resources/art/player_fighter_sorae_up_a_basic.png')
    player_fighter_sorae_up_basic_sheet = sprite_sheet((50, 75), player_fighter_sorae_up_basic_url)
    loaded_dict["player_fighter_sorae_a_up_1_basic"] = player_fighter_sorae_up_basic_sheet[0]
    loaded_dict["player_fighter_sorae_a_up_2_basic"] = player_fighter_sorae_up_basic_sheet[1]
    loaded_dict["player_fighter_sorae_a_up_3_basic"] = player_fighter_sorae_up_basic_sheet[2]
    loaded_dict["player_fighter_sorae_a_up_4_basic"] = player_fighter_sorae_up_basic_sheet[3]
    # forged
    player_fighter_sorae_up_forged_url = resource_path('resources/art/player_fighter_sorae_up_a_forged.png')
    player_fighter_sorae_up_forged_sheet = sprite_sheet((50, 75), player_fighter_sorae_up_forged_url)
    loaded_dict["player_fighter_sorae_a_up_1_forged"] = player_fighter_sorae_up_forged_sheet[0]
    loaded_dict["player_fighter_sorae_a_up_2_forged"] = player_fighter_sorae_up_forged_sheet[1]
    loaded_dict["player_fighter_sorae_a_up_3_forged"] = player_fighter_sorae_up_forged_sheet[2]
    loaded_dict["player_fighter_sorae_a_up_4_forged"] = player_fighter_sorae_up_forged_sheet[3]
    # mythic
    player_fighter_sorae_up_mythic_url = resource_path('resources/art/player_fighter_sorae_up_a_mythic.png')
    player_fighter_sorae_up_mythic_sheet = sprite_sheet((50, 75), player_fighter_sorae_up_mythic_url)
    loaded_dict["player_fighter_sorae_a_up_1_mythic"] = player_fighter_sorae_up_mythic_sheet[0]
    loaded_dict["player_fighter_sorae_a_up_2_mythic"] = player_fighter_sorae_up_mythic_sheet[1]
    loaded_dict["player_fighter_sorae_a_up_3_mythic"] = player_fighter_sorae_up_mythic_sheet[2]
    loaded_dict["player_fighter_sorae_a_up_4_mythic"] = player_fighter_sorae_up_mythic_sheet[3]
    # legend
    player_fighter_sorae_up_legend_url = resource_path('resources/art/player_fighter_sorae_up_a_legend.png')
    player_fighter_sorae_up_legend_sheet = sprite_sheet((50, 75), player_fighter_sorae_up_legend_url)
    loaded_dict["player_fighter_sorae_a_up_1_legend"] = player_fighter_sorae_up_legend_sheet[0]
    loaded_dict["player_fighter_sorae_a_up_2_legend"] = player_fighter_sorae_up_legend_sheet[1]
    loaded_dict["player_fighter_sorae_a_up_3_legend"] = player_fighter_sorae_up_legend_sheet[2]
    loaded_dict["player_fighter_sorae_a_up_4_legend"] = player_fighter_sorae_up_legend_sheet[3]
    player_fighter_sorae_left_url = resource_path('resources/art/player_fighter_sorae_left_a.png')
    player_fighter_sorae_left_sheet = sprite_sheet((50, 75), player_fighter_sorae_left_url)
    loaded_dict["player_fighter_sorae_a_left_1"] = player_fighter_sorae_left_sheet[0]
    loaded_dict["player_fighter_sorae_a_left_2"] = player_fighter_sorae_left_sheet[1]
    loaded_dict["player_fighter_sorae_a_left_3"] = player_fighter_sorae_left_sheet[2]
    loaded_dict["player_fighter_sorae_a_left_4"] = player_fighter_sorae_left_sheet[3]
    # basic
    player_fighter_sorae_left_basic_url = resource_path('resources/art/player_fighter_sorae_left_a_basic.png')
    player_fighter_sorae_left_basic_sheet = sprite_sheet((50, 75), player_fighter_sorae_left_basic_url)
    loaded_dict["player_fighter_sorae_a_left_1_basic"] = player_fighter_sorae_left_basic_sheet[0]
    loaded_dict["player_fighter_sorae_a_left_2_basic"] = player_fighter_sorae_left_basic_sheet[1]
    loaded_dict["player_fighter_sorae_a_left_3_basic"] = player_fighter_sorae_left_basic_sheet[2]
    loaded_dict["player_fighter_sorae_a_left_4_basic"] = player_fighter_sorae_left_basic_sheet[3]
    # forged
    player_fighter_sorae_left_forged_url = resource_path('resources/art/player_fighter_sorae_left_a_forged.png')
    player_fighter_sorae_left_forged_sheet = sprite_sheet((50, 75), player_fighter_sorae_left_forged_url)
    loaded_dict["player_fighter_sorae_a_left_1_forged"] = player_fighter_sorae_left_forged_sheet[0]
    loaded_dict["player_fighter_sorae_a_left_2_forged"] = player_fighter_sorae_left_forged_sheet[1]
    loaded_dict["player_fighter_sorae_a_left_3_forged"] = player_fighter_sorae_left_forged_sheet[2]
    loaded_dict["player_fighter_sorae_a_left_4_forged"] = player_fighter_sorae_left_forged_sheet[3]
    # mythic
    player_fighter_sorae_left_mythic_url = resource_path('resources/art/player_fighter_sorae_left_a_mythic.png')
    player_fighter_sorae_left_mythic_sheet = sprite_sheet((50, 75), player_fighter_sorae_left_mythic_url)
    loaded_dict["player_fighter_sorae_a_left_1_mythic"] = player_fighter_sorae_left_mythic_sheet[0]
    loaded_dict["player_fighter_sorae_a_left_2_mythic"] = player_fighter_sorae_left_mythic_sheet[1]
    loaded_dict["player_fighter_sorae_a_left_3_mythic"] = player_fighter_sorae_left_mythic_sheet[2]
    loaded_dict["player_fighter_sorae_a_left_4_mythic"] = player_fighter_sorae_left_mythic_sheet[3]
    # legend
    player_fighter_sorae_left_legend_url = resource_path('resources/art/player_fighter_sorae_left_a_legend.png')
    player_fighter_sorae_left_legend_sheet = sprite_sheet((50, 75), player_fighter_sorae_left_legend_url)
    loaded_dict["player_fighter_sorae_a_left_1_legend"] = player_fighter_sorae_left_legend_sheet[0]
    loaded_dict["player_fighter_sorae_a_left_2_legend"] = player_fighter_sorae_left_legend_sheet[1]
    loaded_dict["player_fighter_sorae_a_left_3_legend"] = player_fighter_sorae_left_legend_sheet[2]
    loaded_dict["player_fighter_sorae_a_left_4_legend"] = player_fighter_sorae_left_legend_sheet[3]
    player_fighter_sorae_right_url = resource_path('resources/art/player_fighter_sorae_right_a.png')
    player_fighter_sorae_right_sheet = sprite_sheet((50, 75), player_fighter_sorae_right_url)
    loaded_dict["player_fighter_sorae_a_right_1"] = player_fighter_sorae_right_sheet[0]
    loaded_dict["player_fighter_sorae_a_right_2"] = player_fighter_sorae_right_sheet[1]
    loaded_dict["player_fighter_sorae_a_right_3"] = player_fighter_sorae_right_sheet[2]
    loaded_dict["player_fighter_sorae_a_right_4"] = player_fighter_sorae_right_sheet[3]
    # basic
    player_fighter_sorae_right_basic_url = resource_path('resources/art/player_fighter_sorae_right_a_basic.png')
    player_fighter_sorae_right_basic_sheet = sprite_sheet((50, 75), player_fighter_sorae_right_basic_url)
    loaded_dict["player_fighter_sorae_a_right_1_basic"] = player_fighter_sorae_right_basic_sheet[0]
    loaded_dict["player_fighter_sorae_a_right_2_basic"] = player_fighter_sorae_right_basic_sheet[1]
    loaded_dict["player_fighter_sorae_a_right_3_basic"] = player_fighter_sorae_right_basic_sheet[2]
    loaded_dict["player_fighter_sorae_a_right_4_basic"] = player_fighter_sorae_right_basic_sheet[3]
    # forged
    player_fighter_sorae_right_forged_url = resource_path('resources/art/player_fighter_sorae_right_a_forged.png')
    player_fighter_sorae_right_forged_sheet = sprite_sheet((50, 75), player_fighter_sorae_right_forged_url)
    loaded_dict["player_fighter_sorae_a_right_1_forged"] = player_fighter_sorae_right_forged_sheet[0]
    loaded_dict["player_fighter_sorae_a_right_2_forged"] = player_fighter_sorae_right_forged_sheet[1]
    loaded_dict["player_fighter_sorae_a_right_3_forged"] = player_fighter_sorae_right_forged_sheet[2]
    loaded_dict["player_fighter_sorae_a_right_4_forged"] = player_fighter_sorae_right_forged_sheet[3]
    # mythic
    player_fighter_sorae_right_mythic_url = resource_path('resources/art/player_fighter_sorae_right_a_mythic.png')
    player_fighter_sorae_right_mythic_sheet = sprite_sheet((50, 75), player_fighter_sorae_right_mythic_url)
    loaded_dict["player_fighter_sorae_a_right_1_mythic"] = player_fighter_sorae_right_mythic_sheet[0]
    loaded_dict["player_fighter_sorae_a_right_2_mythic"] = player_fighter_sorae_right_mythic_sheet[1]
    loaded_dict["player_fighter_sorae_a_right_3_mythic"] = player_fighter_sorae_right_mythic_sheet[2]
    loaded_dict["player_fighter_sorae_a_right_4_mythic"] = player_fighter_sorae_right_mythic_sheet[3]
    # legend
    player_fighter_sorae_right_legend_url = resource_path('resources/art/player_fighter_sorae_right_a_legend.png')
    player_fighter_sorae_right_legend_sheet = sprite_sheet((50, 75), player_fighter_sorae_right_legend_url)
    loaded_dict["player_fighter_sorae_a_right_1_legend"] = player_fighter_sorae_right_legend_sheet[0]
    loaded_dict["player_fighter_sorae_a_right_2_legend"] = player_fighter_sorae_right_legend_sheet[1]
    loaded_dict["player_fighter_sorae_a_right_3_legend"] = player_fighter_sorae_right_legend_sheet[2]
    loaded_dict["player_fighter_sorae_a_right_4_legend"] = player_fighter_sorae_right_legend_sheet[3]
    # beta -------------------------------------------------------------------------------------------------------------
    player_fighter_sorae_b_down_url = resource_path('resources/art/player_fighter_sorae_down_b.png')
    player_fighter_sorae_b_down_sheet = sprite_sheet((50, 75), player_fighter_sorae_b_down_url)
    loaded_dict["player_fighter_sorae_b_down_1"] = player_fighter_sorae_b_down_sheet[0]
    loaded_dict["player_fighter_sorae_b_down_2"] = player_fighter_sorae_b_down_sheet[1]
    loaded_dict["player_fighter_sorae_b_down_3"] = player_fighter_sorae_b_down_sheet[2]
    loaded_dict["player_fighter_sorae_b_down_4"] = player_fighter_sorae_b_down_sheet[3]
    # basic
    player_fighter_sorae_b_down_basic_url = resource_path('resources/art/player_fighter_sorae_down_b_basic.png')
    player_fighter_sorae_b_down_basic_sheet = sprite_sheet((50, 75), player_fighter_sorae_b_down_basic_url)
    loaded_dict["player_fighter_sorae_b_down_1_basic"] = player_fighter_sorae_b_down_basic_sheet[0]
    loaded_dict["player_fighter_sorae_b_down_2_basic"] = player_fighter_sorae_b_down_basic_sheet[1]
    loaded_dict["player_fighter_sorae_b_down_3_basic"] = player_fighter_sorae_b_down_basic_sheet[2]
    loaded_dict["player_fighter_sorae_b_down_4_basic"] = player_fighter_sorae_b_down_basic_sheet[3]
    # forged
    player_fighter_sorae_b_down_forged_url = resource_path('resources/art/player_fighter_sorae_down_b_forged.png')
    player_fighter_sorae_b_down_forged_sheet = sprite_sheet((50, 75), player_fighter_sorae_b_down_forged_url)
    loaded_dict["player_fighter_sorae_b_down_1_forged"] = player_fighter_sorae_b_down_forged_sheet[0]
    loaded_dict["player_fighter_sorae_b_down_2_forged"] = player_fighter_sorae_b_down_forged_sheet[1]
    loaded_dict["player_fighter_sorae_b_down_3_forged"] = player_fighter_sorae_b_down_forged_sheet[2]
    loaded_dict["player_fighter_sorae_b_down_4_forged"] = player_fighter_sorae_b_down_forged_sheet[3]
    # mythic
    player_fighter_sorae_b_down_mythic_url = resource_path('resources/art/player_fighter_sorae_down_b_mythic.png')
    player_fighter_sorae_b_down_mythic_sheet = sprite_sheet((50, 75), player_fighter_sorae_b_down_mythic_url)
    loaded_dict["player_fighter_sorae_b_down_1_mythic"] = player_fighter_sorae_b_down_mythic_sheet[0]
    loaded_dict["player_fighter_sorae_b_down_2_mythic"] = player_fighter_sorae_b_down_mythic_sheet[1]
    loaded_dict["player_fighter_sorae_b_down_3_mythic"] = player_fighter_sorae_b_down_mythic_sheet[2]
    loaded_dict["player_fighter_sorae_b_down_4_mythic"] = player_fighter_sorae_b_down_mythic_sheet[3]
    # legend
    player_fighter_sorae_b_down_legend_url = resource_path('resources/art/player_fighter_sorae_down_b_legend.png')
    player_fighter_sorae_b_down_legend_sheet = sprite_sheet((50, 75), player_fighter_sorae_b_down_legend_url)
    loaded_dict["player_fighter_sorae_b_down_1_legend"] = player_fighter_sorae_b_down_legend_sheet[0]
    loaded_dict["player_fighter_sorae_b_down_2_legend"] = player_fighter_sorae_b_down_legend_sheet[1]
    loaded_dict["player_fighter_sorae_b_down_3_legend"] = player_fighter_sorae_b_down_legend_sheet[2]
    loaded_dict["player_fighter_sorae_b_down_4_legend"] = player_fighter_sorae_b_down_legend_sheet[3]
    player_fighter_sorae_b_up_url = resource_path('resources/art/player_fighter_sorae_up_b.png')
    player_fighter_sorae_b_up_sheet = sprite_sheet((50, 75), player_fighter_sorae_b_up_url)
    loaded_dict["player_fighter_sorae_b_up_1"] = player_fighter_sorae_b_up_sheet[0]
    loaded_dict["player_fighter_sorae_b_up_2"] = player_fighter_sorae_b_up_sheet[1]
    loaded_dict["player_fighter_sorae_b_up_3"] = player_fighter_sorae_b_up_sheet[2]
    loaded_dict["player_fighter_sorae_b_up_4"] = player_fighter_sorae_b_up_sheet[3]
    # basic
    player_fighter_sorae_b_up_basic_url = resource_path('resources/art/player_fighter_sorae_up_b_basic.png')
    player_fighter_sorae_b_up_basic_sheet = sprite_sheet((50, 75), player_fighter_sorae_b_up_basic_url)
    loaded_dict["player_fighter_sorae_b_up_1_basic"] = player_fighter_sorae_b_up_basic_sheet[0]
    loaded_dict["player_fighter_sorae_b_up_2_basic"] = player_fighter_sorae_b_up_basic_sheet[1]
    loaded_dict["player_fighter_sorae_b_up_3_basic"] = player_fighter_sorae_b_up_basic_sheet[2]
    loaded_dict["player_fighter_sorae_b_up_4_basic"] = player_fighter_sorae_b_up_basic_sheet[3]
    # forged
    player_fighter_sorae_b_up_forged_url = resource_path('resources/art/player_fighter_sorae_up_b_forged.png')
    player_fighter_sorae_b_up_forged_sheet = sprite_sheet((50, 75), player_fighter_sorae_b_up_forged_url)
    loaded_dict["player_fighter_sorae_b_up_1_forged"] = player_fighter_sorae_b_up_forged_sheet[0]
    loaded_dict["player_fighter_sorae_b_up_2_forged"] = player_fighter_sorae_b_up_forged_sheet[1]
    loaded_dict["player_fighter_sorae_b_up_3_forged"] = player_fighter_sorae_b_up_forged_sheet[2]
    loaded_dict["player_fighter_sorae_b_up_4_forged"] = player_fighter_sorae_b_up_forged_sheet[3]
    # mythic
    player_fighter_sorae_b_up_mythic_url = resource_path('resources/art/player_fighter_sorae_up_b_mythic.png')
    player_fighter_sorae_b_up_mythic_sheet = sprite_sheet((50, 75), player_fighter_sorae_b_up_mythic_url)
    loaded_dict["player_fighter_sorae_b_up_1_mythic"] = player_fighter_sorae_b_up_mythic_sheet[0]
    loaded_dict["player_fighter_sorae_b_up_2_mythic"] = player_fighter_sorae_b_up_mythic_sheet[1]
    loaded_dict["player_fighter_sorae_b_up_3_mythic"] = player_fighter_sorae_b_up_mythic_sheet[2]
    loaded_dict["player_fighter_sorae_b_up_4_mythic"] = player_fighter_sorae_b_up_mythic_sheet[3]
    # legend
    player_fighter_sorae_b_up_legend_url = resource_path('resources/art/player_fighter_sorae_up_b_legend.png')
    player_fighter_sorae_b_up_legend_sheet = sprite_sheet((50, 75), player_fighter_sorae_b_up_legend_url)
    loaded_dict["player_fighter_sorae_b_up_1_legend"] = player_fighter_sorae_b_up_legend_sheet[0]
    loaded_dict["player_fighter_sorae_b_up_2_legend"] = player_fighter_sorae_b_up_legend_sheet[1]
    loaded_dict["player_fighter_sorae_b_up_3_legend"] = player_fighter_sorae_b_up_legend_sheet[2]
    loaded_dict["player_fighter_sorae_b_up_4_legend"] = player_fighter_sorae_b_up_legend_sheet[3]
    player_fighter_sorae_b_left_url = resource_path('resources/art/player_fighter_sorae_left_b.png')
    player_fighter_sorae_b_left_sheet = sprite_sheet((50, 75), player_fighter_sorae_b_left_url)
    loaded_dict["player_fighter_sorae_b_left_1"] = player_fighter_sorae_b_left_sheet[0]
    loaded_dict["player_fighter_sorae_b_left_2"] = player_fighter_sorae_b_left_sheet[1]
    loaded_dict["player_fighter_sorae_b_left_3"] = player_fighter_sorae_b_left_sheet[2]
    loaded_dict["player_fighter_sorae_b_left_4"] = player_fighter_sorae_b_left_sheet[3]
    # basic
    player_fighter_sorae_b_left_basic_url = resource_path('resources/art/player_fighter_sorae_left_b_basic.png')
    player_fighter_sorae_b_left_basic_sheet = sprite_sheet((50, 75), player_fighter_sorae_b_left_basic_url)
    loaded_dict["player_fighter_sorae_b_left_1_basic"] = player_fighter_sorae_b_left_basic_sheet[0]
    loaded_dict["player_fighter_sorae_b_left_2_basic"] = player_fighter_sorae_b_left_basic_sheet[1]
    loaded_dict["player_fighter_sorae_b_left_3_basic"] = player_fighter_sorae_b_left_basic_sheet[2]
    loaded_dict["player_fighter_sorae_b_left_4_basic"] = player_fighter_sorae_b_left_basic_sheet[3]
    # forged
    player_fighter_sorae_b_left_forged_url = resource_path('resources/art/player_fighter_sorae_left_b_forged.png')
    player_fighter_sorae_b_left_forged_sheet = sprite_sheet((50, 75), player_fighter_sorae_b_left_forged_url)
    loaded_dict["player_fighter_sorae_b_left_1_forged"] = player_fighter_sorae_b_left_forged_sheet[0]
    loaded_dict["player_fighter_sorae_b_left_2_forged"] = player_fighter_sorae_b_left_forged_sheet[1]
    loaded_dict["player_fighter_sorae_b_left_3_forged"] = player_fighter_sorae_b_left_forged_sheet[2]
    loaded_dict["player_fighter_sorae_b_left_4_forged"] = player_fighter_sorae_b_left_forged_sheet[3]
    # mythic
    player_fighter_sorae_b_left_mythic_url = resource_path('resources/art/player_fighter_sorae_left_b_mythic.png')
    player_fighter_sorae_b_left_mythic_sheet = sprite_sheet((50, 75), player_fighter_sorae_b_left_mythic_url)
    loaded_dict["player_fighter_sorae_b_left_1_mythic"] = player_fighter_sorae_b_left_mythic_sheet[0]
    loaded_dict["player_fighter_sorae_b_left_2_mythic"] = player_fighter_sorae_b_left_mythic_sheet[1]
    loaded_dict["player_fighter_sorae_b_left_3_mythic"] = player_fighter_sorae_b_left_mythic_sheet[2]
    loaded_dict["player_fighter_sorae_b_left_4_mythic"] = player_fighter_sorae_b_left_mythic_sheet[3]
    # legend
    player_fighter_sorae_b_left_legend_url = resource_path('resources/art/player_fighter_sorae_left_b_legend.png')
    player_fighter_sorae_b_left_legend_sheet = sprite_sheet((50, 75), player_fighter_sorae_b_left_legend_url)
    loaded_dict["player_fighter_sorae_b_left_1_legend"] = player_fighter_sorae_b_left_legend_sheet[0]
    loaded_dict["player_fighter_sorae_b_left_2_legend"] = player_fighter_sorae_b_left_legend_sheet[1]
    loaded_dict["player_fighter_sorae_b_left_3_legend"] = player_fighter_sorae_b_left_legend_sheet[2]
    loaded_dict["player_fighter_sorae_b_left_4_legend"] = player_fighter_sorae_b_left_legend_sheet[3]
    player_fighter_sorae_b_right_url = resource_path('resources/art/player_fighter_sorae_right_b.png')
    player_fighter_sorae_b_right_sheet = sprite_sheet((50, 75), player_fighter_sorae_b_right_url)
    loaded_dict["player_fighter_sorae_b_right_1"] = player_fighter_sorae_b_right_sheet[0]
    loaded_dict["player_fighter_sorae_b_right_2"] = player_fighter_sorae_b_right_sheet[1]
    loaded_dict["player_fighter_sorae_b_right_3"] = player_fighter_sorae_b_right_sheet[2]
    loaded_dict["player_fighter_sorae_b_right_4"] = player_fighter_sorae_b_right_sheet[3]
    # basic
    player_fighter_sorae_b_right_basic_url = resource_path('resources/art/player_fighter_sorae_right_b_basic.png')
    player_fighter_sorae_b_right_basic_sheet = sprite_sheet((50, 75), player_fighter_sorae_b_right_basic_url)
    loaded_dict["player_fighter_sorae_b_right_1_basic"] = player_fighter_sorae_b_right_basic_sheet[0]
    loaded_dict["player_fighter_sorae_b_right_2_basic"] = player_fighter_sorae_b_right_basic_sheet[1]
    loaded_dict["player_fighter_sorae_b_right_3_basic"] = player_fighter_sorae_b_right_basic_sheet[2]
    loaded_dict["player_fighter_sorae_b_right_4_basic"] = player_fighter_sorae_b_right_basic_sheet[3]
    # forged
    player_fighter_sorae_b_right_forged_url = resource_path('resources/art/player_fighter_sorae_right_b_forged.png')
    player_fighter_sorae_b_right_forged_sheet = sprite_sheet((50, 75), player_fighter_sorae_b_right_forged_url)
    loaded_dict["player_fighter_sorae_b_right_1_forged"] = player_fighter_sorae_b_right_forged_sheet[0]
    loaded_dict["player_fighter_sorae_b_right_2_forged"] = player_fighter_sorae_b_right_forged_sheet[1]
    loaded_dict["player_fighter_sorae_b_right_3_forged"] = player_fighter_sorae_b_right_forged_sheet[2]
    loaded_dict["player_fighter_sorae_b_right_4_forged"] = player_fighter_sorae_b_right_forged_sheet[3]
    # mythic
    player_fighter_sorae_b_right_mythic_url = resource_path('resources/art/player_fighter_sorae_right_b_mythic.png')
    player_fighter_sorae_b_right_mythic_sheet = sprite_sheet((50, 75), player_fighter_sorae_b_right_mythic_url)
    loaded_dict["player_fighter_sorae_b_right_1_mythic"] = player_fighter_sorae_b_right_mythic_sheet[0]
    loaded_dict["player_fighter_sorae_b_right_2_mythic"] = player_fighter_sorae_b_right_mythic_sheet[1]
    loaded_dict["player_fighter_sorae_b_right_3_mythic"] = player_fighter_sorae_b_right_mythic_sheet[2]
    loaded_dict["player_fighter_sorae_b_right_4_mythic"] = player_fighter_sorae_b_right_mythic_sheet[3]
    # legend
    player_fighter_sorae_b_right_legend_url = resource_path('resources/art/player_fighter_sorae_right_b_legend.png')
    player_fighter_sorae_b_right_legend_sheet = sprite_sheet((50, 75), player_fighter_sorae_b_right_legend_url)
    loaded_dict["player_fighter_sorae_b_right_1_legend"] = player_fighter_sorae_b_right_legend_sheet[0]
    loaded_dict["player_fighter_sorae_b_right_2_legend"] = player_fighter_sorae_b_right_legend_sheet[1]
    loaded_dict["player_fighter_sorae_b_right_3_legend"] = player_fighter_sorae_b_right_legend_sheet[2]
    loaded_dict["player_fighter_sorae_b_right_4_legend"] = player_fighter_sorae_b_right_legend_sheet[3]

    # player scout amuna race ------------------------------------------------------------------------------------------
    # male -------------------------------------------------------------------------------------------------------------
    player_scout_amuna_down_url = resource_path('resources/art/player_scout_amuna_down_male.png')
    player_scout_amuna_down_sheet = sprite_sheet((50, 75), player_scout_amuna_down_url)
    loaded_dict["player_scout_amuna_male_down_1"] = player_scout_amuna_down_sheet[0]
    loaded_dict["player_scout_amuna_male_down_2"] = player_scout_amuna_down_sheet[1]
    loaded_dict["player_scout_amuna_male_down_3"] = player_scout_amuna_down_sheet[2]
    loaded_dict["player_scout_amuna_male_down_4"] = player_scout_amuna_down_sheet[3]
    # basic
    player_scout_amuna_down_basic_url = resource_path('resources/art/player_scout_amuna_down_male_basic.png')
    player_scout_amuna_down_basic_sheet = sprite_sheet((50, 75), player_scout_amuna_down_basic_url)
    loaded_dict["player_scout_amuna_male_down_1_basic"] = player_scout_amuna_down_basic_sheet[0]
    loaded_dict["player_scout_amuna_male_down_2_basic"] = player_scout_amuna_down_basic_sheet[1]
    loaded_dict["player_scout_amuna_male_down_3_basic"] = player_scout_amuna_down_basic_sheet[2]
    loaded_dict["player_scout_amuna_male_down_4_basic"] = player_scout_amuna_down_basic_sheet[3]
    # forged
    player_scout_amuna_down_forged_url = resource_path('resources/art/player_scout_amuna_down_male_forged.png')
    player_scout_amuna_down_forged_sheet = sprite_sheet((50, 75), player_scout_amuna_down_forged_url)
    loaded_dict["player_scout_amuna_male_down_1_forged"] = player_scout_amuna_down_forged_sheet[0]
    loaded_dict["player_scout_amuna_male_down_2_forged"] = player_scout_amuna_down_forged_sheet[1]
    loaded_dict["player_scout_amuna_male_down_3_forged"] = player_scout_amuna_down_forged_sheet[2]
    loaded_dict["player_scout_amuna_male_down_4_forged"] = player_scout_amuna_down_forged_sheet[3]
    # mythic
    player_scout_amuna_down_mythic_url = resource_path('resources/art/player_scout_amuna_down_male_mythic.png')
    player_scout_amuna_down_mythic_sheet = sprite_sheet((50, 75), player_scout_amuna_down_mythic_url)
    loaded_dict["player_scout_amuna_male_down_1_mythic"] = player_scout_amuna_down_mythic_sheet[0]
    loaded_dict["player_scout_amuna_male_down_2_mythic"] = player_scout_amuna_down_mythic_sheet[1]
    loaded_dict["player_scout_amuna_male_down_3_mythic"] = player_scout_amuna_down_mythic_sheet[2]
    loaded_dict["player_scout_amuna_male_down_4_mythic"] = player_scout_amuna_down_mythic_sheet[3]
    # legend
    player_scout_amuna_down_legend_url = resource_path('resources/art/player_scout_amuna_down_male_legend.png')
    player_scout_amuna_down_legend_sheet = sprite_sheet((50, 75), player_scout_amuna_down_legend_url)
    loaded_dict["player_scout_amuna_male_down_1_legend"] = player_scout_amuna_down_legend_sheet[0]
    loaded_dict["player_scout_amuna_male_down_2_legend"] = player_scout_amuna_down_legend_sheet[1]
    loaded_dict["player_scout_amuna_male_down_3_legend"] = player_scout_amuna_down_legend_sheet[2]
    loaded_dict["player_scout_amuna_male_down_4_legend"] = player_scout_amuna_down_legend_sheet[3]
    player_scout_amuna_up_url = resource_path('resources/art/player_scout_amuna_up_male.png')
    player_scout_amuna_up_sheet = sprite_sheet((50, 75), player_scout_amuna_up_url)
    loaded_dict["player_scout_amuna_male_up_1"] = player_scout_amuna_up_sheet[0]
    loaded_dict["player_scout_amuna_male_up_2"] = player_scout_amuna_up_sheet[1]
    loaded_dict["player_scout_amuna_male_up_3"] = player_scout_amuna_up_sheet[2]
    loaded_dict["player_scout_amuna_male_up_4"] = player_scout_amuna_up_sheet[3]
    # basic
    player_scout_amuna_up_basic_url = resource_path('resources/art/player_scout_amuna_up_male_basic.png')
    player_scout_amuna_up_basic_sheet = sprite_sheet((50, 75), player_scout_amuna_up_basic_url)
    loaded_dict["player_scout_amuna_male_up_1_basic"] = player_scout_amuna_up_basic_sheet[0]
    loaded_dict["player_scout_amuna_male_up_2_basic"] = player_scout_amuna_up_basic_sheet[1]
    loaded_dict["player_scout_amuna_male_up_3_basic"] = player_scout_amuna_up_basic_sheet[2]
    loaded_dict["player_scout_amuna_male_up_4_basic"] = player_scout_amuna_up_basic_sheet[3]
    # forged
    player_scout_amuna_up_forged_url = resource_path('resources/art/player_scout_amuna_up_male_forged.png')
    player_scout_amuna_up_forged_sheet = sprite_sheet((50, 75), player_scout_amuna_up_forged_url)
    loaded_dict["player_scout_amuna_male_up_1_forged"] = player_scout_amuna_up_forged_sheet[0]
    loaded_dict["player_scout_amuna_male_up_2_forged"] = player_scout_amuna_up_forged_sheet[1]
    loaded_dict["player_scout_amuna_male_up_3_forged"] = player_scout_amuna_up_forged_sheet[2]
    loaded_dict["player_scout_amuna_male_up_4_forged"] = player_scout_amuna_up_forged_sheet[3]
    # mythic
    player_scout_amuna_up_mythic_url = resource_path('resources/art/player_scout_amuna_up_male_mythic.png')
    player_scout_amuna_up_mythic_sheet = sprite_sheet((50, 75), player_scout_amuna_up_mythic_url)
    loaded_dict["player_scout_amuna_male_up_1_mythic"] = player_scout_amuna_up_mythic_sheet[0]
    loaded_dict["player_scout_amuna_male_up_2_mythic"] = player_scout_amuna_up_mythic_sheet[1]
    loaded_dict["player_scout_amuna_male_up_3_mythic"] = player_scout_amuna_up_mythic_sheet[2]
    loaded_dict["player_scout_amuna_male_up_4_mythic"] = player_scout_amuna_up_mythic_sheet[3]
    # legend
    player_scout_amuna_up_legend_url = resource_path('resources/art/player_scout_amuna_up_male_legend.png')
    player_scout_amuna_up_legend_sheet = sprite_sheet((50, 75), player_scout_amuna_up_legend_url)
    loaded_dict["player_scout_amuna_male_up_1_legend"] = player_scout_amuna_up_legend_sheet[0]
    loaded_dict["player_scout_amuna_male_up_2_legend"] = player_scout_amuna_up_legend_sheet[1]
    loaded_dict["player_scout_amuna_male_up_3_legend"] = player_scout_amuna_up_legend_sheet[2]
    loaded_dict["player_scout_amuna_male_up_4_legend"] = player_scout_amuna_up_legend_sheet[3]
    player_scout_amuna_left_url = resource_path('resources/art/player_scout_amuna_left_male.png')
    player_scout_amuna_left_sheet = sprite_sheet((50, 75), player_scout_amuna_left_url)
    loaded_dict["player_scout_amuna_male_left_1"] = player_scout_amuna_left_sheet[0]
    loaded_dict["player_scout_amuna_male_left_2"] = player_scout_amuna_left_sheet[1]
    loaded_dict["player_scout_amuna_male_left_3"] = player_scout_amuna_left_sheet[2]
    loaded_dict["player_scout_amuna_male_left_4"] = player_scout_amuna_left_sheet[3]
    # basic
    player_scout_amuna_left_basic_url = resource_path('resources/art/player_scout_amuna_left_male_basic.png')
    player_scout_amuna_left_basic_sheet = sprite_sheet((50, 75), player_scout_amuna_left_basic_url)
    loaded_dict["player_scout_amuna_male_left_1_basic"] = player_scout_amuna_left_basic_sheet[0]
    loaded_dict["player_scout_amuna_male_left_2_basic"] = player_scout_amuna_left_basic_sheet[1]
    loaded_dict["player_scout_amuna_male_left_3_basic"] = player_scout_amuna_left_basic_sheet[2]
    loaded_dict["player_scout_amuna_male_left_4_basic"] = player_scout_amuna_left_basic_sheet[3]
    # forged
    player_scout_amuna_left_forged_url = resource_path('resources/art/player_scout_amuna_left_male_forged.png')
    player_scout_amuna_left_forged_sheet = sprite_sheet((50, 75), player_scout_amuna_left_forged_url)
    loaded_dict["player_scout_amuna_male_left_1_forged"] = player_scout_amuna_left_forged_sheet[0]
    loaded_dict["player_scout_amuna_male_left_2_forged"] = player_scout_amuna_left_forged_sheet[1]
    loaded_dict["player_scout_amuna_male_left_3_forged"] = player_scout_amuna_left_forged_sheet[2]
    loaded_dict["player_scout_amuna_male_left_4_forged"] = player_scout_amuna_left_forged_sheet[3]
    # mythic
    player_scout_amuna_left_mythic_url = resource_path('resources/art/player_scout_amuna_left_male_mythic.png')
    player_scout_amuna_left_mythic_sheet = sprite_sheet((50, 75), player_scout_amuna_left_mythic_url)
    loaded_dict["player_scout_amuna_male_left_1_mythic"] = player_scout_amuna_left_mythic_sheet[0]
    loaded_dict["player_scout_amuna_male_left_2_mythic"] = player_scout_amuna_left_mythic_sheet[1]
    loaded_dict["player_scout_amuna_male_left_3_mythic"] = player_scout_amuna_left_mythic_sheet[2]
    loaded_dict["player_scout_amuna_male_left_4_mythic"] = player_scout_amuna_left_mythic_sheet[3]
    # legend
    player_scout_amuna_left_legend_url = resource_path('resources/art/player_scout_amuna_left_male_legend.png')
    player_scout_amuna_left_legend_sheet = sprite_sheet((50, 75), player_scout_amuna_left_legend_url)
    loaded_dict["player_scout_amuna_male_left_1_legend"] = player_scout_amuna_left_legend_sheet[0]
    loaded_dict["player_scout_amuna_male_left_2_legend"] = player_scout_amuna_left_legend_sheet[1]
    loaded_dict["player_scout_amuna_male_left_3_legend"] = player_scout_amuna_left_legend_sheet[2]
    loaded_dict["player_scout_amuna_male_left_4_legend"] = player_scout_amuna_left_legend_sheet[3]
    player_scout_amuna_right_url = resource_path('resources/art/player_scout_amuna_right_male.png')
    player_scout_amuna_right_sheet = sprite_sheet((50, 75), player_scout_amuna_right_url)
    loaded_dict["player_scout_amuna_male_right_1"] = player_scout_amuna_right_sheet[0]
    loaded_dict["player_scout_amuna_male_right_2"] = player_scout_amuna_right_sheet[1]
    loaded_dict["player_scout_amuna_male_right_3"] = player_scout_amuna_right_sheet[2]
    loaded_dict["player_scout_amuna_male_right_4"] = player_scout_amuna_right_sheet[3]
    # basic
    player_scout_amuna_right_basic_url = resource_path('resources/art/player_scout_amuna_right_male_basic.png')
    player_scout_amuna_right_basic_sheet = sprite_sheet((50, 75), player_scout_amuna_right_basic_url)
    loaded_dict["player_scout_amuna_male_right_1_basic"] = player_scout_amuna_right_basic_sheet[0]
    loaded_dict["player_scout_amuna_male_right_2_basic"] = player_scout_amuna_right_basic_sheet[1]
    loaded_dict["player_scout_amuna_male_right_3_basic"] = player_scout_amuna_right_basic_sheet[2]
    loaded_dict["player_scout_amuna_male_right_4_basic"] = player_scout_amuna_right_basic_sheet[3]
    # forged
    player_scout_amuna_right_forged_url = resource_path('resources/art/player_scout_amuna_right_male_forged.png')
    player_scout_amuna_right_forged_sheet = sprite_sheet((50, 75), player_scout_amuna_right_forged_url)
    loaded_dict["player_scout_amuna_male_right_1_forged"] = player_scout_amuna_right_forged_sheet[0]
    loaded_dict["player_scout_amuna_male_right_2_forged"] = player_scout_amuna_right_forged_sheet[1]
    loaded_dict["player_scout_amuna_male_right_3_forged"] = player_scout_amuna_right_forged_sheet[2]
    loaded_dict["player_scout_amuna_male_right_4_forged"] = player_scout_amuna_right_forged_sheet[3]
    # mythic
    player_scout_amuna_right_mythic_url = resource_path('resources/art/player_scout_amuna_right_male_mythic.png')
    player_scout_amuna_right_mythic_sheet = sprite_sheet((50, 75), player_scout_amuna_right_mythic_url)
    loaded_dict["player_scout_amuna_male_right_1_mythic"] = player_scout_amuna_right_mythic_sheet[0]
    loaded_dict["player_scout_amuna_male_right_2_mythic"] = player_scout_amuna_right_mythic_sheet[1]
    loaded_dict["player_scout_amuna_male_right_3_mythic"] = player_scout_amuna_right_mythic_sheet[2]
    loaded_dict["player_scout_amuna_male_right_4_mythic"] = player_scout_amuna_right_mythic_sheet[3]
    # legend
    player_scout_amuna_right_legend_url = resource_path('resources/art/player_scout_amuna_right_male_legend.png')
    player_scout_amuna_right_legend_sheet = sprite_sheet((50, 75), player_scout_amuna_right_legend_url)
    loaded_dict["player_scout_amuna_male_right_1_legend"] = player_scout_amuna_right_legend_sheet[0]
    loaded_dict["player_scout_amuna_male_right_2_legend"] = player_scout_amuna_right_legend_sheet[1]
    loaded_dict["player_scout_amuna_male_right_3_legend"] = player_scout_amuna_right_legend_sheet[2]
    loaded_dict["player_scout_amuna_male_right_4_legend"] = player_scout_amuna_right_legend_sheet[3]
    # female -----------------------------------------------------------------------------------------------------------
    player_scout_amuna_female_down_url = resource_path('resources/art/player_scout_amuna_down_female.png')
    player_scout_amuna_female_down_sheet = sprite_sheet((50, 75), player_scout_amuna_female_down_url)
    loaded_dict["player_scout_amuna_female_down_1"] = player_scout_amuna_female_down_sheet[0]
    loaded_dict["player_scout_amuna_female_down_2"] = player_scout_amuna_female_down_sheet[1]
    loaded_dict["player_scout_amuna_female_down_3"] = player_scout_amuna_female_down_sheet[2]
    loaded_dict["player_scout_amuna_female_down_4"] = player_scout_amuna_female_down_sheet[3]
    # basic
    player_scout_amuna_female_down_basic_url = resource_path('resources/art/player_scout_amuna_down_female_basic.png')
    player_scout_amuna_female_down_basic_sheet = sprite_sheet((50, 75), player_scout_amuna_female_down_basic_url)
    loaded_dict["player_scout_amuna_female_down_1_basic"] = player_scout_amuna_female_down_basic_sheet[0]
    loaded_dict["player_scout_amuna_female_down_2_basic"] = player_scout_amuna_female_down_basic_sheet[1]
    loaded_dict["player_scout_amuna_female_down_3_basic"] = player_scout_amuna_female_down_basic_sheet[2]
    loaded_dict["player_scout_amuna_female_down_4_basic"] = player_scout_amuna_female_down_basic_sheet[3]
    # forged
    player_scout_amuna_female_down_forged_url = resource_path('resources/art/player_scout_amuna_down_female_forged.png')
    player_scout_amuna_female_down_forged_sheet = sprite_sheet((50, 75), player_scout_amuna_female_down_forged_url)
    loaded_dict["player_scout_amuna_female_down_1_forged"] = player_scout_amuna_female_down_forged_sheet[0]
    loaded_dict["player_scout_amuna_female_down_2_forged"] = player_scout_amuna_female_down_forged_sheet[1]
    loaded_dict["player_scout_amuna_female_down_3_forged"] = player_scout_amuna_female_down_forged_sheet[2]
    loaded_dict["player_scout_amuna_female_down_4_forged"] = player_scout_amuna_female_down_forged_sheet[3]
    # mythic
    player_scout_amuna_female_down_mythic_url = resource_path('resources/art/player_scout_amuna_down_female_mythic.png')
    player_scout_amuna_female_down_mythic_sheet = sprite_sheet((50, 75), player_scout_amuna_female_down_mythic_url)
    loaded_dict["player_scout_amuna_female_down_1_mythic"] = player_scout_amuna_female_down_mythic_sheet[0]
    loaded_dict["player_scout_amuna_female_down_2_mythic"] = player_scout_amuna_female_down_mythic_sheet[1]
    loaded_dict["player_scout_amuna_female_down_3_mythic"] = player_scout_amuna_female_down_mythic_sheet[2]
    loaded_dict["player_scout_amuna_female_down_4_mythic"] = player_scout_amuna_female_down_mythic_sheet[3]
    # legend
    player_scout_amuna_female_down_legend_url = resource_path('resources/art/player_scout_amuna_down_female_legend.png')
    player_scout_amuna_female_down_legend_sheet = sprite_sheet((50, 75), player_scout_amuna_female_down_legend_url)
    loaded_dict["player_scout_amuna_female_down_1_legend"] = player_scout_amuna_female_down_legend_sheet[0]
    loaded_dict["player_scout_amuna_female_down_2_legend"] = player_scout_amuna_female_down_legend_sheet[1]
    loaded_dict["player_scout_amuna_female_down_3_legend"] = player_scout_amuna_female_down_legend_sheet[2]
    loaded_dict["player_scout_amuna_female_down_4_legend"] = player_scout_amuna_female_down_legend_sheet[3]
    player_scout_amuna_female_up_url = resource_path('resources/art/player_scout_amuna_up_female.png')
    player_scout_amuna_female_up_sheet = sprite_sheet((50, 75), player_scout_amuna_female_up_url)
    loaded_dict["player_scout_amuna_female_up_1"] = player_scout_amuna_female_up_sheet[0]
    loaded_dict["player_scout_amuna_female_up_2"] = player_scout_amuna_female_up_sheet[1]
    loaded_dict["player_scout_amuna_female_up_3"] = player_scout_amuna_female_up_sheet[2]
    loaded_dict["player_scout_amuna_female_up_4"] = player_scout_amuna_female_up_sheet[3]
    # basic
    player_scout_amuna_female_up_basic_url = resource_path('resources/art/player_scout_amuna_up_female_basic.png')
    player_scout_amuna_female_up_basic_sheet = sprite_sheet((50, 75), player_scout_amuna_female_up_basic_url)
    loaded_dict["player_scout_amuna_female_up_1_basic"] = player_scout_amuna_female_up_basic_sheet[0]
    loaded_dict["player_scout_amuna_female_up_2_basic"] = player_scout_amuna_female_up_basic_sheet[1]
    loaded_dict["player_scout_amuna_female_up_3_basic"] = player_scout_amuna_female_up_basic_sheet[2]
    loaded_dict["player_scout_amuna_female_up_4_basic"] = player_scout_amuna_female_up_basic_sheet[3]
    # forged
    player_scout_amuna_female_up_forged_url = resource_path('resources/art/player_scout_amuna_up_female_forged.png')
    player_scout_amuna_female_up_forged_sheet = sprite_sheet((50, 75), player_scout_amuna_female_up_forged_url)
    loaded_dict["player_scout_amuna_female_up_1_forged"] = player_scout_amuna_female_up_forged_sheet[0]
    loaded_dict["player_scout_amuna_female_up_2_forged"] = player_scout_amuna_female_up_forged_sheet[1]
    loaded_dict["player_scout_amuna_female_up_3_forged"] = player_scout_amuna_female_up_forged_sheet[2]
    loaded_dict["player_scout_amuna_female_up_4_forged"] = player_scout_amuna_female_up_forged_sheet[3]
    # mythic
    player_scout_amuna_female_up_mythic_url = resource_path('resources/art/player_scout_amuna_up_female_mythic.png')
    player_scout_amuna_female_up_mythic_sheet = sprite_sheet((50, 75), player_scout_amuna_female_up_mythic_url)
    loaded_dict["player_scout_amuna_female_up_1_mythic"] = player_scout_amuna_female_up_mythic_sheet[0]
    loaded_dict["player_scout_amuna_female_up_2_mythic"] = player_scout_amuna_female_up_mythic_sheet[1]
    loaded_dict["player_scout_amuna_female_up_3_mythic"] = player_scout_amuna_female_up_mythic_sheet[2]
    loaded_dict["player_scout_amuna_female_up_4_mythic"] = player_scout_amuna_female_up_mythic_sheet[3]
    # legend
    player_scout_amuna_female_up_legend_url = resource_path('resources/art/player_scout_amuna_up_female_legend.png')
    player_scout_amuna_female_up_legend_sheet = sprite_sheet((50, 75), player_scout_amuna_female_up_legend_url)
    loaded_dict["player_scout_amuna_female_up_1_legend"] = player_scout_amuna_female_up_legend_sheet[0]
    loaded_dict["player_scout_amuna_female_up_2_legend"] = player_scout_amuna_female_up_legend_sheet[1]
    loaded_dict["player_scout_amuna_female_up_3_legend"] = player_scout_amuna_female_up_legend_sheet[2]
    loaded_dict["player_scout_amuna_female_up_4_legend"] = player_scout_amuna_female_up_legend_sheet[3]
    player_scout_amuna_female_left_url = resource_path('resources/art/player_scout_amuna_left_female.png')
    player_scout_amuna_female_left_sheet = sprite_sheet((50, 75), player_scout_amuna_female_left_url)
    loaded_dict["player_scout_amuna_female_left_1"] = player_scout_amuna_female_left_sheet[0]
    loaded_dict["player_scout_amuna_female_left_2"] = player_scout_amuna_female_left_sheet[1]
    loaded_dict["player_scout_amuna_female_left_3"] = player_scout_amuna_female_left_sheet[2]
    loaded_dict["player_scout_amuna_female_left_4"] = player_scout_amuna_female_left_sheet[3]
    # basic
    player_scout_amuna_female_left_basic_url = resource_path('resources/art/player_scout_amuna_left_female_basic.png')
    player_scout_amuna_female_left_basic_sheet = sprite_sheet((50, 75), player_scout_amuna_female_left_basic_url)
    loaded_dict["player_scout_amuna_female_left_1_basic"] = player_scout_amuna_female_left_basic_sheet[0]
    loaded_dict["player_scout_amuna_female_left_2_basic"] = player_scout_amuna_female_left_basic_sheet[1]
    loaded_dict["player_scout_amuna_female_left_3_basic"] = player_scout_amuna_female_left_basic_sheet[2]
    loaded_dict["player_scout_amuna_female_left_4_basic"] = player_scout_amuna_female_left_basic_sheet[3]
    # forged
    player_scout_amuna_female_left_forged_url = resource_path('resources/art/player_scout_amuna_left_female_forged.png')
    player_scout_amuna_female_left_forged_sheet = sprite_sheet((50, 75), player_scout_amuna_female_left_forged_url)
    loaded_dict["player_scout_amuna_female_left_1_forged"] = player_scout_amuna_female_left_forged_sheet[0]
    loaded_dict["player_scout_amuna_female_left_2_forged"] = player_scout_amuna_female_left_forged_sheet[1]
    loaded_dict["player_scout_amuna_female_left_3_forged"] = player_scout_amuna_female_left_forged_sheet[2]
    loaded_dict["player_scout_amuna_female_left_4_forged"] = player_scout_amuna_female_left_forged_sheet[3]
    # mythic
    player_scout_amuna_female_left_mythic_url = resource_path('resources/art/player_scout_amuna_left_female_mythic.png')
    player_scout_amuna_female_left_mythic_sheet = sprite_sheet((50, 75), player_scout_amuna_female_left_mythic_url)
    loaded_dict["player_scout_amuna_female_left_1_mythic"] = player_scout_amuna_female_left_mythic_sheet[0]
    loaded_dict["player_scout_amuna_female_left_2_mythic"] = player_scout_amuna_female_left_mythic_sheet[1]
    loaded_dict["player_scout_amuna_female_left_3_mythic"] = player_scout_amuna_female_left_mythic_sheet[2]
    loaded_dict["player_scout_amuna_female_left_4_mythic"] = player_scout_amuna_female_left_mythic_sheet[3]
    # legend
    player_scout_amuna_female_left_legend_url = resource_path('resources/art/player_scout_amuna_left_female_legend.png')
    player_scout_amuna_female_left_legend_sheet = sprite_sheet((50, 75), player_scout_amuna_female_left_legend_url)
    loaded_dict["player_scout_amuna_female_left_1_legend"] = player_scout_amuna_female_left_legend_sheet[0]
    loaded_dict["player_scout_amuna_female_left_2_legend"] = player_scout_amuna_female_left_legend_sheet[1]
    loaded_dict["player_scout_amuna_female_left_3_legend"] = player_scout_amuna_female_left_legend_sheet[2]
    loaded_dict["player_scout_amuna_female_left_4_legend"] = player_scout_amuna_female_left_legend_sheet[3]
    player_scout_amuna_female_right_url = resource_path('resources/art/player_scout_amuna_right_female.png')
    player_scout_amuna_female_right_sheet = sprite_sheet((50, 75), player_scout_amuna_female_right_url)
    loaded_dict["player_scout_amuna_female_right_1"] = player_scout_amuna_female_right_sheet[0]
    loaded_dict["player_scout_amuna_female_right_2"] = player_scout_amuna_female_right_sheet[1]
    loaded_dict["player_scout_amuna_female_right_3"] = player_scout_amuna_female_right_sheet[2]
    loaded_dict["player_scout_amuna_female_right_4"] = player_scout_amuna_female_right_sheet[3]
    # basic
    player_scout_amuna_female_right_basic_url = resource_path('resources/art/player_scout_amuna_right_female_basic.png')
    player_scout_amuna_female_right_basic_sheet = sprite_sheet((50, 75), player_scout_amuna_female_right_basic_url)
    loaded_dict["player_scout_amuna_female_right_1_basic"] = player_scout_amuna_female_right_basic_sheet[0]
    loaded_dict["player_scout_amuna_female_right_2_basic"] = player_scout_amuna_female_right_basic_sheet[1]
    loaded_dict["player_scout_amuna_female_right_3_basic"] = player_scout_amuna_female_right_basic_sheet[2]
    loaded_dict["player_scout_amuna_female_right_4_basic"] = player_scout_amuna_female_right_basic_sheet[3]
    # forged
    player_scout_amuna_female_right_forged_url = resource_path('resources/art/'
                                                               'player_scout_amuna_right_female_forged.png')
    player_scout_amuna_female_right_forged_sheet = sprite_sheet((50, 75), player_scout_amuna_female_right_forged_url)
    loaded_dict["player_scout_amuna_female_right_1_forged"] = player_scout_amuna_female_right_forged_sheet[0]
    loaded_dict["player_scout_amuna_female_right_2_forged"] = player_scout_amuna_female_right_forged_sheet[1]
    loaded_dict["player_scout_amuna_female_right_3_forged"] = player_scout_amuna_female_right_forged_sheet[2]
    loaded_dict["player_scout_amuna_female_right_4_forged"] = player_scout_amuna_female_right_forged_sheet[3]
    # mythic
    player_scout_amuna_female_right_mythic_url = resource_path('resources/art/'
                                                               'player_scout_amuna_right_female_mythic.png')
    player_scout_amuna_female_right_mythic_sheet = sprite_sheet((50, 75), player_scout_amuna_female_right_mythic_url)
    loaded_dict["player_scout_amuna_female_right_1_mythic"] = player_scout_amuna_female_right_mythic_sheet[0]
    loaded_dict["player_scout_amuna_female_right_2_mythic"] = player_scout_amuna_female_right_mythic_sheet[1]
    loaded_dict["player_scout_amuna_female_right_3_mythic"] = player_scout_amuna_female_right_mythic_sheet[2]
    loaded_dict["player_scout_amuna_female_right_4_mythic"] = player_scout_amuna_female_right_mythic_sheet[3]
    # legend
    player_scout_amuna_female_right_legend_url = resource_path('resources/art/'
                                                               'player_scout_amuna_right_female_legend.png')
    player_scout_amuna_female_right_legend_sheet = sprite_sheet((50, 75), player_scout_amuna_female_right_legend_url)
    loaded_dict["player_scout_amuna_female_right_1_legend"] = player_scout_amuna_female_right_legend_sheet[0]
    loaded_dict["player_scout_amuna_female_right_2_legend"] = player_scout_amuna_female_right_legend_sheet[1]
    loaded_dict["player_scout_amuna_female_right_3_legend"] = player_scout_amuna_female_right_legend_sheet[2]
    loaded_dict["player_scout_amuna_female_right_4_legend"] = player_scout_amuna_female_right_legend_sheet[3]

    # player scout nuldar race -----------------------------------------------------------------------------------------
    # male -------------------------------------------------------------------------------------------------------------
    player_scout_nuldar_down_url = resource_path('resources/art/player_scout_nuldar_down_male.png')
    player_scout_nuldar_down_sheet = sprite_sheet((50, 75), player_scout_nuldar_down_url)
    loaded_dict["player_scout_nuldar_male_down_1"] = player_scout_nuldar_down_sheet[0]
    loaded_dict["player_scout_nuldar_male_down_2"] = player_scout_nuldar_down_sheet[1]
    loaded_dict["player_scout_nuldar_male_down_3"] = player_scout_nuldar_down_sheet[2]
    loaded_dict["player_scout_nuldar_male_down_4"] = player_scout_nuldar_down_sheet[3]
    # basic
    player_scout_nuldar_down_basic_url = resource_path('resources/art/player_scout_nuldar_down_male_basic.png')
    player_scout_nuldar_down_basic_sheet = sprite_sheet((50, 75), player_scout_nuldar_down_basic_url)
    loaded_dict["player_scout_nuldar_male_down_1_basic"] = player_scout_nuldar_down_basic_sheet[0]
    loaded_dict["player_scout_nuldar_male_down_2_basic"] = player_scout_nuldar_down_basic_sheet[1]
    loaded_dict["player_scout_nuldar_male_down_3_basic"] = player_scout_nuldar_down_basic_sheet[2]
    loaded_dict["player_scout_nuldar_male_down_4_basic"] = player_scout_nuldar_down_basic_sheet[3]
    # forged
    player_scout_nuldar_down_forged_url = resource_path('resources/art/player_scout_nuldar_down_male_forged.png')
    player_scout_nuldar_down_forged_sheet = sprite_sheet((50, 75), player_scout_nuldar_down_forged_url)
    loaded_dict["player_scout_nuldar_male_down_1_forged"] = player_scout_nuldar_down_forged_sheet[0]
    loaded_dict["player_scout_nuldar_male_down_2_forged"] = player_scout_nuldar_down_forged_sheet[1]
    loaded_dict["player_scout_nuldar_male_down_3_forged"] = player_scout_nuldar_down_forged_sheet[2]
    loaded_dict["player_scout_nuldar_male_down_4_forged"] = player_scout_nuldar_down_forged_sheet[3]
    # mythic
    player_scout_nuldar_down_mythic_url = resource_path('resources/art/player_scout_nuldar_down_male_mythic.png')
    player_scout_nuldar_down_mythic_sheet = sprite_sheet((50, 75), player_scout_nuldar_down_mythic_url)
    loaded_dict["player_scout_nuldar_male_down_1_mythic"] = player_scout_nuldar_down_mythic_sheet[0]
    loaded_dict["player_scout_nuldar_male_down_2_mythic"] = player_scout_nuldar_down_mythic_sheet[1]
    loaded_dict["player_scout_nuldar_male_down_3_mythic"] = player_scout_nuldar_down_mythic_sheet[2]
    loaded_dict["player_scout_nuldar_male_down_4_mythic"] = player_scout_nuldar_down_mythic_sheet[3]
    # legend
    player_scout_nuldar_down_legend_url = resource_path('resources/art/player_scout_nuldar_down_male_legend.png')
    player_scout_nuldar_down_legend_sheet = sprite_sheet((50, 75), player_scout_nuldar_down_legend_url)
    loaded_dict["player_scout_nuldar_male_down_1_legend"] = player_scout_nuldar_down_legend_sheet[0]
    loaded_dict["player_scout_nuldar_male_down_2_legend"] = player_scout_nuldar_down_legend_sheet[1]
    loaded_dict["player_scout_nuldar_male_down_3_legend"] = player_scout_nuldar_down_legend_sheet[2]
    loaded_dict["player_scout_nuldar_male_down_4_legend"] = player_scout_nuldar_down_legend_sheet[3]
    player_scout_nuldar_up_url = resource_path('resources/art/player_scout_nuldar_up_male.png')
    player_scout_nuldar_up_sheet = sprite_sheet((50, 75), player_scout_nuldar_up_url)
    loaded_dict["player_scout_nuldar_male_up_1"] = player_scout_nuldar_up_sheet[0]
    loaded_dict["player_scout_nuldar_male_up_2"] = player_scout_nuldar_up_sheet[1]
    loaded_dict["player_scout_nuldar_male_up_3"] = player_scout_nuldar_up_sheet[2]
    loaded_dict["player_scout_nuldar_male_up_4"] = player_scout_nuldar_up_sheet[3]
    # basic
    player_scout_nuldar_up_basic_url = resource_path('resources/art/player_scout_nuldar_up_male_basic.png')
    player_scout_nuldar_up_basic_sheet = sprite_sheet((50, 75), player_scout_nuldar_up_basic_url)
    loaded_dict["player_scout_nuldar_male_up_1_basic"] = player_scout_nuldar_up_basic_sheet[0]
    loaded_dict["player_scout_nuldar_male_up_2_basic"] = player_scout_nuldar_up_basic_sheet[1]
    loaded_dict["player_scout_nuldar_male_up_3_basic"] = player_scout_nuldar_up_basic_sheet[2]
    loaded_dict["player_scout_nuldar_male_up_4_basic"] = player_scout_nuldar_up_basic_sheet[3]
    # forged
    player_scout_nuldar_up_forged_url = resource_path('resources/art/player_scout_nuldar_up_male_forged.png')
    player_scout_nuldar_up_forged_sheet = sprite_sheet((50, 75), player_scout_nuldar_up_forged_url)
    loaded_dict["player_scout_nuldar_male_up_1_forged"] = player_scout_nuldar_up_forged_sheet[0]
    loaded_dict["player_scout_nuldar_male_up_2_forged"] = player_scout_nuldar_up_forged_sheet[1]
    loaded_dict["player_scout_nuldar_male_up_3_forged"] = player_scout_nuldar_up_forged_sheet[2]
    loaded_dict["player_scout_nuldar_male_up_4_forged"] = player_scout_nuldar_up_forged_sheet[3]
    # mythic
    player_scout_nuldar_up_mythic_url = resource_path('resources/art/player_scout_nuldar_up_male_mythic.png')
    player_scout_nuldar_up_mythic_sheet = sprite_sheet((50, 75), player_scout_nuldar_up_mythic_url)
    loaded_dict["player_scout_nuldar_male_up_1_mythic"] = player_scout_nuldar_up_mythic_sheet[0]
    loaded_dict["player_scout_nuldar_male_up_2_mythic"] = player_scout_nuldar_up_mythic_sheet[1]
    loaded_dict["player_scout_nuldar_male_up_3_mythic"] = player_scout_nuldar_up_mythic_sheet[2]
    loaded_dict["player_scout_nuldar_male_up_4_mythic"] = player_scout_nuldar_up_mythic_sheet[3]
    # legend
    player_scout_nuldar_up_legend_url = resource_path('resources/art/player_scout_nuldar_up_male_legend.png')
    player_scout_nuldar_up_legend_sheet = sprite_sheet((50, 75), player_scout_nuldar_up_legend_url)
    loaded_dict["player_scout_nuldar_male_up_1_legend"] = player_scout_nuldar_up_legend_sheet[0]
    loaded_dict["player_scout_nuldar_male_up_2_legend"] = player_scout_nuldar_up_legend_sheet[1]
    loaded_dict["player_scout_nuldar_male_up_3_legend"] = player_scout_nuldar_up_legend_sheet[2]
    loaded_dict["player_scout_nuldar_male_up_4_legend"] = player_scout_nuldar_up_legend_sheet[3]
    player_scout_nuldar_left_url = resource_path('resources/art/player_scout_nuldar_left_male.png')
    player_scout_nuldar_left_sheet = sprite_sheet((50, 75), player_scout_nuldar_left_url)
    loaded_dict["player_scout_nuldar_male_left_1"] = player_scout_nuldar_left_sheet[0]
    loaded_dict["player_scout_nuldar_male_left_2"] = player_scout_nuldar_left_sheet[1]
    loaded_dict["player_scout_nuldar_male_left_3"] = player_scout_nuldar_left_sheet[2]
    loaded_dict["player_scout_nuldar_male_left_4"] = player_scout_nuldar_left_sheet[3]
    # basic
    player_scout_nuldar_left_basic_url = resource_path('resources/art/player_scout_nuldar_left_male_basic.png')
    player_scout_nuldar_left_basic_sheet = sprite_sheet((50, 75), player_scout_nuldar_left_basic_url)
    loaded_dict["player_scout_nuldar_male_left_1_basic"] = player_scout_nuldar_left_basic_sheet[0]
    loaded_dict["player_scout_nuldar_male_left_2_basic"] = player_scout_nuldar_left_basic_sheet[1]
    loaded_dict["player_scout_nuldar_male_left_3_basic"] = player_scout_nuldar_left_basic_sheet[2]
    loaded_dict["player_scout_nuldar_male_left_4_basic"] = player_scout_nuldar_left_basic_sheet[3]
    # forged
    player_scout_nuldar_left_forged_url = resource_path('resources/art/player_scout_nuldar_left_male_forged.png')
    player_scout_nuldar_left_forged_sheet = sprite_sheet((50, 75), player_scout_nuldar_left_forged_url)
    loaded_dict["player_scout_nuldar_male_left_1_forged"] = player_scout_nuldar_left_forged_sheet[0]
    loaded_dict["player_scout_nuldar_male_left_2_forged"] = player_scout_nuldar_left_forged_sheet[1]
    loaded_dict["player_scout_nuldar_male_left_3_forged"] = player_scout_nuldar_left_forged_sheet[2]
    loaded_dict["player_scout_nuldar_male_left_4_forged"] = player_scout_nuldar_left_forged_sheet[3]
    # mythic
    player_scout_nuldar_left_mythic_url = resource_path('resources/art/player_scout_nuldar_left_male_mythic.png')
    player_scout_nuldar_left_mythic_sheet = sprite_sheet((50, 75), player_scout_nuldar_left_mythic_url)
    loaded_dict["player_scout_nuldar_male_left_1_mythic"] = player_scout_nuldar_left_mythic_sheet[0]
    loaded_dict["player_scout_nuldar_male_left_2_mythic"] = player_scout_nuldar_left_mythic_sheet[1]
    loaded_dict["player_scout_nuldar_male_left_3_mythic"] = player_scout_nuldar_left_mythic_sheet[2]
    loaded_dict["player_scout_nuldar_male_left_4_mythic"] = player_scout_nuldar_left_mythic_sheet[3]
    # legend
    player_scout_nuldar_left_legend_url = resource_path('resources/art/player_scout_nuldar_left_male_legend.png')
    player_scout_nuldar_left_legend_sheet = sprite_sheet((50, 75), player_scout_nuldar_left_legend_url)
    loaded_dict["player_scout_nuldar_male_left_1_legend"] = player_scout_nuldar_left_legend_sheet[0]
    loaded_dict["player_scout_nuldar_male_left_2_legend"] = player_scout_nuldar_left_legend_sheet[1]
    loaded_dict["player_scout_nuldar_male_left_3_legend"] = player_scout_nuldar_left_legend_sheet[2]
    loaded_dict["player_scout_nuldar_male_left_4_legend"] = player_scout_nuldar_left_legend_sheet[3]
    player_scout_nuldar_right_url = resource_path('resources/art/player_scout_nuldar_right_male.png')
    player_scout_nuldar_right_sheet = sprite_sheet((50, 75), player_scout_nuldar_right_url)
    loaded_dict["player_scout_nuldar_male_right_1"] = player_scout_nuldar_right_sheet[0]
    loaded_dict["player_scout_nuldar_male_right_2"] = player_scout_nuldar_right_sheet[1]
    loaded_dict["player_scout_nuldar_male_right_3"] = player_scout_nuldar_right_sheet[2]
    loaded_dict["player_scout_nuldar_male_right_4"] = player_scout_nuldar_right_sheet[3]
    # basic
    player_scout_nuldar_right_basic_url = resource_path('resources/art/player_scout_nuldar_right_male_basic.png')
    player_scout_nuldar_right_basic_sheet = sprite_sheet((50, 75), player_scout_nuldar_right_basic_url)
    loaded_dict["player_scout_nuldar_male_right_1_basic"] = player_scout_nuldar_right_basic_sheet[0]
    loaded_dict["player_scout_nuldar_male_right_2_basic"] = player_scout_nuldar_right_basic_sheet[1]
    loaded_dict["player_scout_nuldar_male_right_3_basic"] = player_scout_nuldar_right_basic_sheet[2]
    loaded_dict["player_scout_nuldar_male_right_4_basic"] = player_scout_nuldar_right_basic_sheet[3]
    # forged
    player_scout_nuldar_right_forged_url = resource_path('resources/art/player_scout_nuldar_right_male_forged.png')
    player_scout_nuldar_right_forged_sheet = sprite_sheet((50, 75), player_scout_nuldar_right_forged_url)
    loaded_dict["player_scout_nuldar_male_right_1_forged"] = player_scout_nuldar_right_forged_sheet[0]
    loaded_dict["player_scout_nuldar_male_right_2_forged"] = player_scout_nuldar_right_forged_sheet[1]
    loaded_dict["player_scout_nuldar_male_right_3_forged"] = player_scout_nuldar_right_forged_sheet[2]
    loaded_dict["player_scout_nuldar_male_right_4_forged"] = player_scout_nuldar_right_forged_sheet[3]
    # mythic
    player_scout_nuldar_right_mythic_url = resource_path('resources/art/player_scout_nuldar_right_male_mythic.png')
    player_scout_nuldar_right_mythic_sheet = sprite_sheet((50, 75), player_scout_nuldar_right_mythic_url)
    loaded_dict["player_scout_nuldar_male_right_1_mythic"] = player_scout_nuldar_right_mythic_sheet[0]
    loaded_dict["player_scout_nuldar_male_right_2_mythic"] = player_scout_nuldar_right_mythic_sheet[1]
    loaded_dict["player_scout_nuldar_male_right_3_mythic"] = player_scout_nuldar_right_mythic_sheet[2]
    loaded_dict["player_scout_nuldar_male_right_4_mythic"] = player_scout_nuldar_right_mythic_sheet[3]
    # legend
    player_scout_nuldar_right_legend_url = resource_path('resources/art/player_scout_nuldar_right_male_legend.png')
    player_scout_nuldar_right_legend_sheet = sprite_sheet((50, 75), player_scout_nuldar_right_legend_url)
    loaded_dict["player_scout_nuldar_male_right_1_legend"] = player_scout_nuldar_right_legend_sheet[0]
    loaded_dict["player_scout_nuldar_male_right_2_legend"] = player_scout_nuldar_right_legend_sheet[1]
    loaded_dict["player_scout_nuldar_male_right_3_legend"] = player_scout_nuldar_right_legend_sheet[2]
    loaded_dict["player_scout_nuldar_male_right_4_legend"] = player_scout_nuldar_right_legend_sheet[3]
    # female -----------------------------------------------------------------------------------------------------------
    player_scout_nuldar_female_down_url = resource_path('resources/art/player_scout_nuldar_down_female.png')
    player_scout_nuldar_female_down_sheet = sprite_sheet((50, 75), player_scout_nuldar_female_down_url)
    loaded_dict["player_scout_nuldar_female_down_1"] = player_scout_nuldar_female_down_sheet[0]
    loaded_dict["player_scout_nuldar_female_down_2"] = player_scout_nuldar_female_down_sheet[1]
    loaded_dict["player_scout_nuldar_female_down_3"] = player_scout_nuldar_female_down_sheet[2]
    loaded_dict["player_scout_nuldar_female_down_4"] = player_scout_nuldar_female_down_sheet[3]
    # basic
    player_scout_nuldar_female_down_basic_url = resource_path('resources/art/player_scout_nuldar_down_female_basic.png')
    player_scout_nuldar_female_down_basic_sheet = sprite_sheet((50, 75), player_scout_nuldar_female_down_basic_url)
    loaded_dict["player_scout_nuldar_female_down_1_basic"] = player_scout_nuldar_female_down_basic_sheet[0]
    loaded_dict["player_scout_nuldar_female_down_2_basic"] = player_scout_nuldar_female_down_basic_sheet[1]
    loaded_dict["player_scout_nuldar_female_down_3_basic"] = player_scout_nuldar_female_down_basic_sheet[2]
    loaded_dict["player_scout_nuldar_female_down_4_basic"] = player_scout_nuldar_female_down_basic_sheet[3]
    # forged
    player_scout_nuldar_female_down_forged_url = resource_path('resources/art/'
                                                               'player_scout_nuldar_down_female_forged.png')
    player_scout_nuldar_female_down_forged_sheet = sprite_sheet((50, 75), player_scout_nuldar_female_down_forged_url)
    loaded_dict["player_scout_nuldar_female_down_1_forged"] = player_scout_nuldar_female_down_forged_sheet[0]
    loaded_dict["player_scout_nuldar_female_down_2_forged"] = player_scout_nuldar_female_down_forged_sheet[1]
    loaded_dict["player_scout_nuldar_female_down_3_forged"] = player_scout_nuldar_female_down_forged_sheet[2]
    loaded_dict["player_scout_nuldar_female_down_4_forged"] = player_scout_nuldar_female_down_forged_sheet[3]
    # mythic
    player_scout_nuldar_female_down_mythic_url = resource_path('resources/art/'
                                                               'player_scout_nuldar_down_female_mythic.png')
    player_scout_nuldar_female_down_mythic_sheet = sprite_sheet((50, 75), player_scout_nuldar_female_down_mythic_url)
    loaded_dict["player_scout_nuldar_female_down_1_mythic"] = player_scout_nuldar_female_down_mythic_sheet[0]
    loaded_dict["player_scout_nuldar_female_down_2_mythic"] = player_scout_nuldar_female_down_mythic_sheet[1]
    loaded_dict["player_scout_nuldar_female_down_3_mythic"] = player_scout_nuldar_female_down_mythic_sheet[2]
    loaded_dict["player_scout_nuldar_female_down_4_mythic"] = player_scout_nuldar_female_down_mythic_sheet[3]
    # legend
    player_scout_nuldar_female_down_legend_url = resource_path('resources/art/'
                                                               'player_scout_nuldar_down_female_legend.png')
    player_scout_nuldar_female_down_legend_sheet = sprite_sheet((50, 75), player_scout_nuldar_female_down_legend_url)
    loaded_dict["player_scout_nuldar_female_down_1_legend"] = player_scout_nuldar_female_down_legend_sheet[0]
    loaded_dict["player_scout_nuldar_female_down_2_legend"] = player_scout_nuldar_female_down_legend_sheet[1]
    loaded_dict["player_scout_nuldar_female_down_3_legend"] = player_scout_nuldar_female_down_legend_sheet[2]
    loaded_dict["player_scout_nuldar_female_down_4_legend"] = player_scout_nuldar_female_down_legend_sheet[3]
    player_scout_nuldar_female_up_url = resource_path('resources/art/player_scout_nuldar_up_female.png')
    player_scout_nuldar_female_up_sheet = sprite_sheet((50, 75), player_scout_nuldar_female_up_url)
    loaded_dict["player_scout_nuldar_female_up_1"] = player_scout_nuldar_female_up_sheet[0]
    loaded_dict["player_scout_nuldar_female_up_2"] = player_scout_nuldar_female_up_sheet[1]
    loaded_dict["player_scout_nuldar_female_up_3"] = player_scout_nuldar_female_up_sheet[2]
    loaded_dict["player_scout_nuldar_female_up_4"] = player_scout_nuldar_female_up_sheet[3]
    # basic
    player_scout_nuldar_female_up_basic_url = resource_path('resources/art/player_scout_nuldar_up_female_basic.png')
    player_scout_nuldar_female_up_basic_sheet = sprite_sheet((50, 75), player_scout_nuldar_female_up_basic_url)
    loaded_dict["player_scout_nuldar_female_up_1_basic"] = player_scout_nuldar_female_up_basic_sheet[0]
    loaded_dict["player_scout_nuldar_female_up_2_basic"] = player_scout_nuldar_female_up_basic_sheet[1]
    loaded_dict["player_scout_nuldar_female_up_3_basic"] = player_scout_nuldar_female_up_basic_sheet[2]
    loaded_dict["player_scout_nuldar_female_up_4_basic"] = player_scout_nuldar_female_up_basic_sheet[3]
    # forged
    player_scout_nuldar_female_up_forged_url = resource_path('resources/art/player_scout_nuldar_up_female_forged.png')
    player_scout_nuldar_female_up_forged_sheet = sprite_sheet((50, 75), player_scout_nuldar_female_up_forged_url)
    loaded_dict["player_scout_nuldar_female_up_1_forged"] = player_scout_nuldar_female_up_forged_sheet[0]
    loaded_dict["player_scout_nuldar_female_up_2_forged"] = player_scout_nuldar_female_up_forged_sheet[1]
    loaded_dict["player_scout_nuldar_female_up_3_forged"] = player_scout_nuldar_female_up_forged_sheet[2]
    loaded_dict["player_scout_nuldar_female_up_4_forged"] = player_scout_nuldar_female_up_forged_sheet[3]
    # mythic
    player_scout_nuldar_female_up_mythic_url = resource_path('resources/art/player_scout_nuldar_up_female_mythic.png')
    player_scout_nuldar_female_up_mythic_sheet = sprite_sheet((50, 75), player_scout_nuldar_female_up_mythic_url)
    loaded_dict["player_scout_nuldar_female_up_1_mythic"] = player_scout_nuldar_female_up_mythic_sheet[0]
    loaded_dict["player_scout_nuldar_female_up_2_mythic"] = player_scout_nuldar_female_up_mythic_sheet[1]
    loaded_dict["player_scout_nuldar_female_up_3_mythic"] = player_scout_nuldar_female_up_mythic_sheet[2]
    loaded_dict["player_scout_nuldar_female_up_4_mythic"] = player_scout_nuldar_female_up_mythic_sheet[3]
    # legend
    player_scout_nuldar_female_up_legend_url = resource_path('resources/art/player_scout_nuldar_up_female_legend.png')
    player_scout_nuldar_female_up_legend_sheet = sprite_sheet((50, 75), player_scout_nuldar_female_up_legend_url)
    loaded_dict["player_scout_nuldar_female_up_1_legend"] = player_scout_nuldar_female_up_legend_sheet[0]
    loaded_dict["player_scout_nuldar_female_up_2_legend"] = player_scout_nuldar_female_up_legend_sheet[1]
    loaded_dict["player_scout_nuldar_female_up_3_legend"] = player_scout_nuldar_female_up_legend_sheet[2]
    loaded_dict["player_scout_nuldar_female_up_4_legend"] = player_scout_nuldar_female_up_legend_sheet[3]
    player_scout_nuldar_female_left_url = resource_path('resources/art/player_scout_nuldar_left_female.png')
    player_scout_nuldar_female_left_sheet = sprite_sheet((50, 75), player_scout_nuldar_female_left_url)
    loaded_dict["player_scout_nuldar_female_left_1"] = player_scout_nuldar_female_left_sheet[0]
    loaded_dict["player_scout_nuldar_female_left_2"] = player_scout_nuldar_female_left_sheet[1]
    loaded_dict["player_scout_nuldar_female_left_3"] = player_scout_nuldar_female_left_sheet[2]
    loaded_dict["player_scout_nuldar_female_left_4"] = player_scout_nuldar_female_left_sheet[3]
    # basic
    player_scout_nuldar_female_left_basic_url = resource_path('resources/art/player_scout_nuldar_left_female_basic.png')
    player_scout_nuldar_female_left_basic_sheet = sprite_sheet((50, 75), player_scout_nuldar_female_left_basic_url)
    loaded_dict["player_scout_nuldar_female_left_1_basic"] = player_scout_nuldar_female_left_basic_sheet[0]
    loaded_dict["player_scout_nuldar_female_left_2_basic"] = player_scout_nuldar_female_left_basic_sheet[1]
    loaded_dict["player_scout_nuldar_female_left_3_basic"] = player_scout_nuldar_female_left_basic_sheet[2]
    loaded_dict["player_scout_nuldar_female_left_4_basic"] = player_scout_nuldar_female_left_basic_sheet[3]
    # forged
    player_scout_nuldar_female_left_forged_url = resource_path('resources/art/'
                                                               'player_scout_nuldar_left_female_forged.png')
    player_scout_nuldar_female_left_forged_sheet = sprite_sheet((50, 75), player_scout_nuldar_female_left_forged_url)
    loaded_dict["player_scout_nuldar_female_left_1_forged"] = player_scout_nuldar_female_left_forged_sheet[0]
    loaded_dict["player_scout_nuldar_female_left_2_forged"] = player_scout_nuldar_female_left_forged_sheet[1]
    loaded_dict["player_scout_nuldar_female_left_3_forged"] = player_scout_nuldar_female_left_forged_sheet[2]
    loaded_dict["player_scout_nuldar_female_left_4_forged"] = player_scout_nuldar_female_left_forged_sheet[3]
    # mythic
    player_scout_nuldar_female_left_mythic_url = resource_path('resources/art/'
                                                               'player_scout_nuldar_left_female_mythic.png')
    player_scout_nuldar_female_left_mythic_sheet = sprite_sheet((50, 75), player_scout_nuldar_female_left_mythic_url)
    loaded_dict["player_scout_nuldar_female_left_1_mythic"] = player_scout_nuldar_female_left_mythic_sheet[0]
    loaded_dict["player_scout_nuldar_female_left_2_mythic"] = player_scout_nuldar_female_left_mythic_sheet[1]
    loaded_dict["player_scout_nuldar_female_left_3_mythic"] = player_scout_nuldar_female_left_mythic_sheet[2]
    loaded_dict["player_scout_nuldar_female_left_4_mythic"] = player_scout_nuldar_female_left_mythic_sheet[3]
    # legend
    player_scout_nuldar_female_left_legend_url = resource_path('resources/art/'
                                                               'player_scout_nuldar_left_female_legend.png')
    player_scout_nuldar_female_left_legend_sheet = sprite_sheet((50, 75), player_scout_nuldar_female_left_legend_url)
    loaded_dict["player_scout_nuldar_female_left_1_legend"] = player_scout_nuldar_female_left_legend_sheet[0]
    loaded_dict["player_scout_nuldar_female_left_2_legend"] = player_scout_nuldar_female_left_legend_sheet[1]
    loaded_dict["player_scout_nuldar_female_left_3_legend"] = player_scout_nuldar_female_left_legend_sheet[2]
    loaded_dict["player_scout_nuldar_female_left_4_legend"] = player_scout_nuldar_female_left_legend_sheet[3]
    player_scout_nuldar_female_right_url = resource_path('resources/art/player_scout_nuldar_right_female.png')
    player_scout_nuldar_female_right_sheet = sprite_sheet((50, 75), player_scout_nuldar_female_right_url)
    loaded_dict["player_scout_nuldar_female_right_1"] = player_scout_nuldar_female_right_sheet[0]
    loaded_dict["player_scout_nuldar_female_right_2"] = player_scout_nuldar_female_right_sheet[1]
    loaded_dict["player_scout_nuldar_female_right_3"] = player_scout_nuldar_female_right_sheet[2]
    loaded_dict["player_scout_nuldar_female_right_4"] = player_scout_nuldar_female_right_sheet[3]
    # basic
    player_scout_nuldar_female_right_basic_url = resource_path('resources/art/'
                                                               'player_scout_nuldar_right_female_basic.png')
    player_scout_nuldar_female_right_basic_sheet = sprite_sheet((50, 75), player_scout_nuldar_female_right_basic_url)
    loaded_dict["player_scout_nuldar_female_right_1_basic"] = player_scout_nuldar_female_right_basic_sheet[0]
    loaded_dict["player_scout_nuldar_female_right_2_basic"] = player_scout_nuldar_female_right_basic_sheet[1]
    loaded_dict["player_scout_nuldar_female_right_3_basic"] = player_scout_nuldar_female_right_basic_sheet[2]
    loaded_dict["player_scout_nuldar_female_right_4_basic"] = player_scout_nuldar_female_right_basic_sheet[3]
    # forged
    player_scout_nuldar_female_right_forged_url = resource_path('resources/art/'
                                                                'player_scout_nuldar_right_female_forged.png')
    player_scout_nuldar_female_right_forged_sheet = sprite_sheet((50, 75), player_scout_nuldar_female_right_forged_url)
    loaded_dict["player_scout_nuldar_female_right_1_forged"] = player_scout_nuldar_female_right_forged_sheet[0]
    loaded_dict["player_scout_nuldar_female_right_2_forged"] = player_scout_nuldar_female_right_forged_sheet[1]
    loaded_dict["player_scout_nuldar_female_right_3_forged"] = player_scout_nuldar_female_right_forged_sheet[2]
    loaded_dict["player_scout_nuldar_female_right_4_forged"] = player_scout_nuldar_female_right_forged_sheet[3]
    # mythic
    player_scout_nuldar_female_right_mythic_url = resource_path('resources/art/'
                                                                'player_scout_nuldar_right_female_mythic.png')
    player_scout_nuldar_female_right_mythic_sheet = sprite_sheet((50, 75), player_scout_nuldar_female_right_mythic_url)
    loaded_dict["player_scout_nuldar_female_right_1_mythic"] = player_scout_nuldar_female_right_mythic_sheet[0]
    loaded_dict["player_scout_nuldar_female_right_2_mythic"] = player_scout_nuldar_female_right_mythic_sheet[1]
    loaded_dict["player_scout_nuldar_female_right_3_mythic"] = player_scout_nuldar_female_right_mythic_sheet[2]
    loaded_dict["player_scout_nuldar_female_right_4_mythic"] = player_scout_nuldar_female_right_mythic_sheet[3]
    # legend
    player_scout_nuldar_female_right_legend_url = resource_path('resources/art/'
                                                                'player_scout_nuldar_right_female_legend.png')
    player_scout_nuldar_female_right_legend_sheet = sprite_sheet((50, 75), player_scout_nuldar_female_right_legend_url)
    loaded_dict["player_scout_nuldar_female_right_1_legend"] = player_scout_nuldar_female_right_legend_sheet[0]
    loaded_dict["player_scout_nuldar_female_right_2_legend"] = player_scout_nuldar_female_right_legend_sheet[1]
    loaded_dict["player_scout_nuldar_female_right_3_legend"] = player_scout_nuldar_female_right_legend_sheet[2]
    loaded_dict["player_scout_nuldar_female_right_4_legend"] = player_scout_nuldar_female_right_legend_sheet[3]

    # player scout sorae race ------------------------------------------------------------------------------------------
    # alpha ------------------------------------------------------------------------------------------------------------
    player_scout_sorae_down_url = resource_path('resources/art/player_scout_sorae_down_a.png')
    player_scout_sorae_down_sheet = sprite_sheet((50, 75), player_scout_sorae_down_url)
    loaded_dict["player_scout_sorae_a_down_1"] = player_scout_sorae_down_sheet[0]
    loaded_dict["player_scout_sorae_a_down_2"] = player_scout_sorae_down_sheet[1]
    loaded_dict["player_scout_sorae_a_down_3"] = player_scout_sorae_down_sheet[2]
    loaded_dict["player_scout_sorae_a_down_4"] = player_scout_sorae_down_sheet[3]
    # basic
    player_scout_sorae_down_basic_url = resource_path('resources/art/player_scout_sorae_down_a_basic.png')
    player_scout_sorae_down_basic_sheet = sprite_sheet((50, 75), player_scout_sorae_down_basic_url)
    loaded_dict["player_scout_sorae_a_down_1_basic"] = player_scout_sorae_down_basic_sheet[0]
    loaded_dict["player_scout_sorae_a_down_2_basic"] = player_scout_sorae_down_basic_sheet[1]
    loaded_dict["player_scout_sorae_a_down_3_basic"] = player_scout_sorae_down_basic_sheet[2]
    loaded_dict["player_scout_sorae_a_down_4_basic"] = player_scout_sorae_down_basic_sheet[3]
    # forged
    player_scout_sorae_down_forged_url = resource_path('resources/art/player_scout_sorae_down_a_forged.png')
    player_scout_sorae_down_forged_sheet = sprite_sheet((50, 75), player_scout_sorae_down_forged_url)
    loaded_dict["player_scout_sorae_a_down_1_forged"] = player_scout_sorae_down_forged_sheet[0]
    loaded_dict["player_scout_sorae_a_down_2_forged"] = player_scout_sorae_down_forged_sheet[1]
    loaded_dict["player_scout_sorae_a_down_3_forged"] = player_scout_sorae_down_forged_sheet[2]
    loaded_dict["player_scout_sorae_a_down_4_forged"] = player_scout_sorae_down_forged_sheet[3]
    # mythic
    player_scout_sorae_down_mythic_url = resource_path('resources/art/player_scout_sorae_down_a_mythic.png')
    player_scout_sorae_down_mythic_sheet = sprite_sheet((50, 75), player_scout_sorae_down_mythic_url)
    loaded_dict["player_scout_sorae_a_down_1_mythic"] = player_scout_sorae_down_mythic_sheet[0]
    loaded_dict["player_scout_sorae_a_down_2_mythic"] = player_scout_sorae_down_mythic_sheet[1]
    loaded_dict["player_scout_sorae_a_down_3_mythic"] = player_scout_sorae_down_mythic_sheet[2]
    loaded_dict["player_scout_sorae_a_down_4_mythic"] = player_scout_sorae_down_mythic_sheet[3]
    # legend
    player_scout_sorae_down_legend_url = resource_path('resources/art/player_scout_sorae_down_a_legend.png')
    player_scout_sorae_down_legend_sheet = sprite_sheet((50, 75), player_scout_sorae_down_legend_url)
    loaded_dict["player_scout_sorae_a_down_1_legend"] = player_scout_sorae_down_legend_sheet[0]
    loaded_dict["player_scout_sorae_a_down_2_legend"] = player_scout_sorae_down_legend_sheet[1]
    loaded_dict["player_scout_sorae_a_down_3_legend"] = player_scout_sorae_down_legend_sheet[2]
    loaded_dict["player_scout_sorae_a_down_4_legend"] = player_scout_sorae_down_legend_sheet[3]
    player_scout_sorae_up_url = resource_path('resources/art/player_scout_sorae_up_a.png')
    player_scout_sorae_up_sheet = sprite_sheet((50, 75), player_scout_sorae_up_url)
    loaded_dict["player_scout_sorae_a_up_1"] = player_scout_sorae_up_sheet[0]
    loaded_dict["player_scout_sorae_a_up_2"] = player_scout_sorae_up_sheet[1]
    loaded_dict["player_scout_sorae_a_up_3"] = player_scout_sorae_up_sheet[2]
    loaded_dict["player_scout_sorae_a_up_4"] = player_scout_sorae_up_sheet[3]
    # basic
    player_scout_sorae_up_basic_url = resource_path('resources/art/player_scout_sorae_up_a_basic.png')
    player_scout_sorae_up_basic_sheet = sprite_sheet((50, 75), player_scout_sorae_up_basic_url)
    loaded_dict["player_scout_sorae_a_up_1_basic"] = player_scout_sorae_up_basic_sheet[0]
    loaded_dict["player_scout_sorae_a_up_2_basic"] = player_scout_sorae_up_basic_sheet[1]
    loaded_dict["player_scout_sorae_a_up_3_basic"] = player_scout_sorae_up_basic_sheet[2]
    loaded_dict["player_scout_sorae_a_up_4_basic"] = player_scout_sorae_up_basic_sheet[3]
    # forged
    player_scout_sorae_up_forged_url = resource_path('resources/art/player_scout_sorae_up_a_forged.png')
    player_scout_sorae_up_forged_sheet = sprite_sheet((50, 75), player_scout_sorae_up_forged_url)
    loaded_dict["player_scout_sorae_a_up_1_forged"] = player_scout_sorae_up_forged_sheet[0]
    loaded_dict["player_scout_sorae_a_up_2_forged"] = player_scout_sorae_up_forged_sheet[1]
    loaded_dict["player_scout_sorae_a_up_3_forged"] = player_scout_sorae_up_forged_sheet[2]
    loaded_dict["player_scout_sorae_a_up_4_forged"] = player_scout_sorae_up_forged_sheet[3]
    # mythic
    player_scout_sorae_up_mythic_url = resource_path('resources/art/player_scout_sorae_up_a_mythic.png')
    player_scout_sorae_up_mythic_sheet = sprite_sheet((50, 75), player_scout_sorae_up_mythic_url)
    loaded_dict["player_scout_sorae_a_up_1_mythic"] = player_scout_sorae_up_mythic_sheet[0]
    loaded_dict["player_scout_sorae_a_up_2_mythic"] = player_scout_sorae_up_mythic_sheet[1]
    loaded_dict["player_scout_sorae_a_up_3_mythic"] = player_scout_sorae_up_mythic_sheet[2]
    loaded_dict["player_scout_sorae_a_up_4_mythic"] = player_scout_sorae_up_mythic_sheet[3]
    # legend
    player_scout_sorae_up_legend_url = resource_path('resources/art/player_scout_sorae_up_a_legend.png')
    player_scout_sorae_up_legend_sheet = sprite_sheet((50, 75), player_scout_sorae_up_legend_url)
    loaded_dict["player_scout_sorae_a_up_1_legend"] = player_scout_sorae_up_legend_sheet[0]
    loaded_dict["player_scout_sorae_a_up_2_legend"] = player_scout_sorae_up_legend_sheet[1]
    loaded_dict["player_scout_sorae_a_up_3_legend"] = player_scout_sorae_up_legend_sheet[2]
    loaded_dict["player_scout_sorae_a_up_4_legend"] = player_scout_sorae_up_legend_sheet[3]
    player_scout_sorae_left_url = resource_path('resources/art/player_scout_sorae_left_a.png')
    player_scout_sorae_left_sheet = sprite_sheet((50, 75), player_scout_sorae_left_url)
    loaded_dict["player_scout_sorae_a_left_1"] = player_scout_sorae_left_sheet[0]
    loaded_dict["player_scout_sorae_a_left_2"] = player_scout_sorae_left_sheet[1]
    loaded_dict["player_scout_sorae_a_left_3"] = player_scout_sorae_left_sheet[2]
    loaded_dict["player_scout_sorae_a_left_4"] = player_scout_sorae_left_sheet[3]
    # basic
    player_scout_sorae_left_basic_url = resource_path('resources/art/player_scout_sorae_left_a_basic.png')
    player_scout_sorae_left_basic_sheet = sprite_sheet((50, 75), player_scout_sorae_left_basic_url)
    loaded_dict["player_scout_sorae_a_left_1_basic"] = player_scout_sorae_left_basic_sheet[0]
    loaded_dict["player_scout_sorae_a_left_2_basic"] = player_scout_sorae_left_basic_sheet[1]
    loaded_dict["player_scout_sorae_a_left_3_basic"] = player_scout_sorae_left_basic_sheet[2]
    loaded_dict["player_scout_sorae_a_left_4_basic"] = player_scout_sorae_left_basic_sheet[3]
    # forged
    player_scout_sorae_left_forged_url = resource_path('resources/art/player_scout_sorae_left_a_forged.png')
    player_scout_sorae_left_forged_sheet = sprite_sheet((50, 75), player_scout_sorae_left_forged_url)
    loaded_dict["player_scout_sorae_a_left_1_forged"] = player_scout_sorae_left_forged_sheet[0]
    loaded_dict["player_scout_sorae_a_left_2_forged"] = player_scout_sorae_left_forged_sheet[1]
    loaded_dict["player_scout_sorae_a_left_3_forged"] = player_scout_sorae_left_forged_sheet[2]
    loaded_dict["player_scout_sorae_a_left_4_forged"] = player_scout_sorae_left_forged_sheet[3]
    # mythic
    player_scout_sorae_left_mythic_url = resource_path('resources/art/player_scout_sorae_left_a_mythic.png')
    player_scout_sorae_left_mythic_sheet = sprite_sheet((50, 75), player_scout_sorae_left_mythic_url)
    loaded_dict["player_scout_sorae_a_left_1_mythic"] = player_scout_sorae_left_mythic_sheet[0]
    loaded_dict["player_scout_sorae_a_left_2_mythic"] = player_scout_sorae_left_mythic_sheet[1]
    loaded_dict["player_scout_sorae_a_left_3_mythic"] = player_scout_sorae_left_mythic_sheet[2]
    loaded_dict["player_scout_sorae_a_left_4_mythic"] = player_scout_sorae_left_mythic_sheet[3]
    # legend
    player_scout_sorae_left_legend_url = resource_path('resources/art/player_scout_sorae_left_a_legend.png')
    player_scout_sorae_left_legend_sheet = sprite_sheet((50, 75), player_scout_sorae_left_legend_url)
    loaded_dict["player_scout_sorae_a_left_1_legend"] = player_scout_sorae_left_legend_sheet[0]
    loaded_dict["player_scout_sorae_a_left_2_legend"] = player_scout_sorae_left_legend_sheet[1]
    loaded_dict["player_scout_sorae_a_left_3_legend"] = player_scout_sorae_left_legend_sheet[2]
    loaded_dict["player_scout_sorae_a_left_4_legend"] = player_scout_sorae_left_legend_sheet[3]
    player_scout_sorae_right_url = resource_path('resources/art/player_scout_sorae_right_a.png')
    player_scout_sorae_right_sheet = sprite_sheet((50, 75), player_scout_sorae_right_url)
    loaded_dict["player_scout_sorae_a_right_1"] = player_scout_sorae_right_sheet[0]
    loaded_dict["player_scout_sorae_a_right_2"] = player_scout_sorae_right_sheet[1]
    loaded_dict["player_scout_sorae_a_right_3"] = player_scout_sorae_right_sheet[2]
    loaded_dict["player_scout_sorae_a_right_4"] = player_scout_sorae_right_sheet[3]
    # basic
    player_scout_sorae_right_basic_url = resource_path('resources/art/player_scout_sorae_right_a_basic.png')
    player_scout_sorae_right_basic_sheet = sprite_sheet((50, 75), player_scout_sorae_right_basic_url)
    loaded_dict["player_scout_sorae_a_right_1_basic"] = player_scout_sorae_right_basic_sheet[0]
    loaded_dict["player_scout_sorae_a_right_2_basic"] = player_scout_sorae_right_basic_sheet[1]
    loaded_dict["player_scout_sorae_a_right_3_basic"] = player_scout_sorae_right_basic_sheet[2]
    loaded_dict["player_scout_sorae_a_right_4_basic"] = player_scout_sorae_right_basic_sheet[3]
    # forged
    player_scout_sorae_right_forged_url = resource_path('resources/art/player_scout_sorae_right_a_forged.png')
    player_scout_sorae_right_forged_sheet = sprite_sheet((50, 75), player_scout_sorae_right_forged_url)
    loaded_dict["player_scout_sorae_a_right_1_forged"] = player_scout_sorae_right_forged_sheet[0]
    loaded_dict["player_scout_sorae_a_right_2_forged"] = player_scout_sorae_right_forged_sheet[1]
    loaded_dict["player_scout_sorae_a_right_3_forged"] = player_scout_sorae_right_forged_sheet[2]
    loaded_dict["player_scout_sorae_a_right_4_forged"] = player_scout_sorae_right_forged_sheet[3]
    # mythic
    player_scout_sorae_right_mythic_url = resource_path('resources/art/player_scout_sorae_right_a_mythic.png')
    player_scout_sorae_right_mythic_sheet = sprite_sheet((50, 75), player_scout_sorae_right_mythic_url)
    loaded_dict["player_scout_sorae_a_right_1_mythic"] = player_scout_sorae_right_mythic_sheet[0]
    loaded_dict["player_scout_sorae_a_right_2_mythic"] = player_scout_sorae_right_mythic_sheet[1]
    loaded_dict["player_scout_sorae_a_right_3_mythic"] = player_scout_sorae_right_mythic_sheet[2]
    loaded_dict["player_scout_sorae_a_right_4_mythic"] = player_scout_sorae_right_mythic_sheet[3]
    # legend
    player_scout_sorae_right_legend_url = resource_path('resources/art/player_scout_sorae_right_a_legend.png')
    player_scout_sorae_right_legend_sheet = sprite_sheet((50, 75), player_scout_sorae_right_legend_url)
    loaded_dict["player_scout_sorae_a_right_1_legend"] = player_scout_sorae_right_legend_sheet[0]
    loaded_dict["player_scout_sorae_a_right_2_legend"] = player_scout_sorae_right_legend_sheet[1]
    loaded_dict["player_scout_sorae_a_right_3_legend"] = player_scout_sorae_right_legend_sheet[2]
    loaded_dict["player_scout_sorae_a_right_4_legend"] = player_scout_sorae_right_legend_sheet[3]
    # beta -------------------------------------------------------------------------------------------------------------
    player_scout_sorae_b_down_url = resource_path('resources/art/player_scout_sorae_down_b.png')
    player_scout_sorae_b_down_sheet = sprite_sheet((50, 75), player_scout_sorae_b_down_url)
    loaded_dict["player_scout_sorae_b_down_1"] = player_scout_sorae_b_down_sheet[0]
    loaded_dict["player_scout_sorae_b_down_2"] = player_scout_sorae_b_down_sheet[1]
    loaded_dict["player_scout_sorae_b_down_3"] = player_scout_sorae_b_down_sheet[2]
    loaded_dict["player_scout_sorae_b_down_4"] = player_scout_sorae_b_down_sheet[3]
    # basic
    player_scout_sorae_b_down_basic_url = resource_path('resources/art/player_scout_sorae_down_b_basic.png')
    player_scout_sorae_b_down_basic_sheet = sprite_sheet((50, 75), player_scout_sorae_b_down_basic_url)
    loaded_dict["player_scout_sorae_b_down_1_basic"] = player_scout_sorae_b_down_basic_sheet[0]
    loaded_dict["player_scout_sorae_b_down_2_basic"] = player_scout_sorae_b_down_basic_sheet[1]
    loaded_dict["player_scout_sorae_b_down_3_basic"] = player_scout_sorae_b_down_basic_sheet[2]
    loaded_dict["player_scout_sorae_b_down_4_basic"] = player_scout_sorae_b_down_basic_sheet[3]
    # forged
    player_scout_sorae_b_down_forged_url = resource_path('resources/art/player_scout_sorae_down_b_forged.png')
    player_scout_sorae_b_down_forged_sheet = sprite_sheet((50, 75), player_scout_sorae_b_down_forged_url)
    loaded_dict["player_scout_sorae_b_down_1_forged"] = player_scout_sorae_b_down_forged_sheet[0]
    loaded_dict["player_scout_sorae_b_down_2_forged"] = player_scout_sorae_b_down_forged_sheet[1]
    loaded_dict["player_scout_sorae_b_down_3_forged"] = player_scout_sorae_b_down_forged_sheet[2]
    loaded_dict["player_scout_sorae_b_down_4_forged"] = player_scout_sorae_b_down_forged_sheet[3]
    # mythic
    player_scout_sorae_b_down_mythic_url = resource_path('resources/art/player_scout_sorae_down_b_mythic.png')
    player_scout_sorae_b_down_mythic_sheet = sprite_sheet((50, 75), player_scout_sorae_b_down_mythic_url)
    loaded_dict["player_scout_sorae_b_down_1_mythic"] = player_scout_sorae_b_down_mythic_sheet[0]
    loaded_dict["player_scout_sorae_b_down_2_mythic"] = player_scout_sorae_b_down_mythic_sheet[1]
    loaded_dict["player_scout_sorae_b_down_3_mythic"] = player_scout_sorae_b_down_mythic_sheet[2]
    loaded_dict["player_scout_sorae_b_down_4_mythic"] = player_scout_sorae_b_down_mythic_sheet[3]
    # legend
    player_scout_sorae_b_down_legend_url = resource_path('resources/art/player_scout_sorae_down_b_legend.png')
    player_scout_sorae_b_down_legend_sheet = sprite_sheet((50, 75), player_scout_sorae_b_down_legend_url)
    loaded_dict["player_scout_sorae_b_down_1_legend"] = player_scout_sorae_b_down_legend_sheet[0]
    loaded_dict["player_scout_sorae_b_down_2_legend"] = player_scout_sorae_b_down_legend_sheet[1]
    loaded_dict["player_scout_sorae_b_down_3_legend"] = player_scout_sorae_b_down_legend_sheet[2]
    loaded_dict["player_scout_sorae_b_down_4_legend"] = player_scout_sorae_b_down_legend_sheet[3]
    player_scout_sorae_b_up_url = resource_path('resources/art/player_scout_sorae_up_b.png')
    player_scout_sorae_b_up_sheet = sprite_sheet((50, 75), player_scout_sorae_b_up_url)
    loaded_dict["player_scout_sorae_b_up_1"] = player_scout_sorae_b_up_sheet[0]
    loaded_dict["player_scout_sorae_b_up_2"] = player_scout_sorae_b_up_sheet[1]
    loaded_dict["player_scout_sorae_b_up_3"] = player_scout_sorae_b_up_sheet[2]
    loaded_dict["player_scout_sorae_b_up_4"] = player_scout_sorae_b_up_sheet[3]
    # basic
    player_scout_sorae_b_up_basic_url = resource_path('resources/art/player_scout_sorae_up_b_basic.png')
    player_scout_sorae_b_up_basic_sheet = sprite_sheet((50, 75), player_scout_sorae_b_up_basic_url)
    loaded_dict["player_scout_sorae_b_up_1_basic"] = player_scout_sorae_b_up_basic_sheet[0]
    loaded_dict["player_scout_sorae_b_up_2_basic"] = player_scout_sorae_b_up_basic_sheet[1]
    loaded_dict["player_scout_sorae_b_up_3_basic"] = player_scout_sorae_b_up_basic_sheet[2]
    loaded_dict["player_scout_sorae_b_up_4_basic"] = player_scout_sorae_b_up_basic_sheet[3]
    # forged
    player_scout_sorae_b_up_forged_url = resource_path('resources/art/player_scout_sorae_up_b_forged.png')
    player_scout_sorae_b_up_forged_sheet = sprite_sheet((50, 75), player_scout_sorae_b_up_forged_url)
    loaded_dict["player_scout_sorae_b_up_1_forged"] = player_scout_sorae_b_up_forged_sheet[0]
    loaded_dict["player_scout_sorae_b_up_2_forged"] = player_scout_sorae_b_up_forged_sheet[1]
    loaded_dict["player_scout_sorae_b_up_3_forged"] = player_scout_sorae_b_up_forged_sheet[2]
    loaded_dict["player_scout_sorae_b_up_4_forged"] = player_scout_sorae_b_up_forged_sheet[3]
    # mythic
    player_scout_sorae_b_up_mythic_url = resource_path('resources/art/player_scout_sorae_up_b_mythic.png')
    player_scout_sorae_b_up_mythic_sheet = sprite_sheet((50, 75), player_scout_sorae_b_up_mythic_url)
    loaded_dict["player_scout_sorae_b_up_1_mythic"] = player_scout_sorae_b_up_mythic_sheet[0]
    loaded_dict["player_scout_sorae_b_up_2_mythic"] = player_scout_sorae_b_up_mythic_sheet[1]
    loaded_dict["player_scout_sorae_b_up_3_mythic"] = player_scout_sorae_b_up_mythic_sheet[2]
    loaded_dict["player_scout_sorae_b_up_4_mythic"] = player_scout_sorae_b_up_mythic_sheet[3]
    # legend
    player_scout_sorae_b_up_legend_url = resource_path('resources/art/player_scout_sorae_up_b_legend.png')
    player_scout_sorae_b_up_legend_sheet = sprite_sheet((50, 75), player_scout_sorae_b_up_legend_url)
    loaded_dict["player_scout_sorae_b_up_1_legend"] = player_scout_sorae_b_up_legend_sheet[0]
    loaded_dict["player_scout_sorae_b_up_2_legend"] = player_scout_sorae_b_up_legend_sheet[1]
    loaded_dict["player_scout_sorae_b_up_3_legend"] = player_scout_sorae_b_up_legend_sheet[2]
    loaded_dict["player_scout_sorae_b_up_4_legend"] = player_scout_sorae_b_up_legend_sheet[3]
    player_scout_sorae_b_left_url = resource_path('resources/art/player_scout_sorae_left_b.png')
    player_scout_sorae_b_left_sheet = sprite_sheet((50, 75), player_scout_sorae_b_left_url)
    loaded_dict["player_scout_sorae_b_left_1"] = player_scout_sorae_b_left_sheet[0]
    loaded_dict["player_scout_sorae_b_left_2"] = player_scout_sorae_b_left_sheet[1]
    loaded_dict["player_scout_sorae_b_left_3"] = player_scout_sorae_b_left_sheet[2]
    loaded_dict["player_scout_sorae_b_left_4"] = player_scout_sorae_b_left_sheet[3]
    # basic
    player_scout_sorae_b_left_basic_url = resource_path('resources/art/player_scout_sorae_left_b_basic.png')
    player_scout_sorae_b_left_basic_sheet = sprite_sheet((50, 75), player_scout_sorae_b_left_basic_url)
    loaded_dict["player_scout_sorae_b_left_1_basic"] = player_scout_sorae_b_left_basic_sheet[0]
    loaded_dict["player_scout_sorae_b_left_2_basic"] = player_scout_sorae_b_left_basic_sheet[1]
    loaded_dict["player_scout_sorae_b_left_3_basic"] = player_scout_sorae_b_left_basic_sheet[2]
    loaded_dict["player_scout_sorae_b_left_4_basic"] = player_scout_sorae_b_left_basic_sheet[3]
    # forged
    player_scout_sorae_b_left_forged_url = resource_path('resources/art/player_scout_sorae_left_b_forged.png')
    player_scout_sorae_b_left_forged_sheet = sprite_sheet((50, 75), player_scout_sorae_b_left_forged_url)
    loaded_dict["player_scout_sorae_b_left_1_forged"] = player_scout_sorae_b_left_forged_sheet[0]
    loaded_dict["player_scout_sorae_b_left_2_forged"] = player_scout_sorae_b_left_forged_sheet[1]
    loaded_dict["player_scout_sorae_b_left_3_forged"] = player_scout_sorae_b_left_forged_sheet[2]
    loaded_dict["player_scout_sorae_b_left_4_forged"] = player_scout_sorae_b_left_forged_sheet[3]
    # mythic
    player_scout_sorae_b_left_mythic_url = resource_path('resources/art/player_scout_sorae_left_b_mythic.png')
    player_scout_sorae_b_left_mythic_sheet = sprite_sheet((50, 75), player_scout_sorae_b_left_mythic_url)
    loaded_dict["player_scout_sorae_b_left_1_mythic"] = player_scout_sorae_b_left_mythic_sheet[0]
    loaded_dict["player_scout_sorae_b_left_2_mythic"] = player_scout_sorae_b_left_mythic_sheet[1]
    loaded_dict["player_scout_sorae_b_left_3_mythic"] = player_scout_sorae_b_left_mythic_sheet[2]
    loaded_dict["player_scout_sorae_b_left_4_mythic"] = player_scout_sorae_b_left_mythic_sheet[3]
    # legend
    player_scout_sorae_b_left_legend_url = resource_path('resources/art/player_scout_sorae_left_b_legend.png')
    player_scout_sorae_b_left_legend_sheet = sprite_sheet((50, 75), player_scout_sorae_b_left_legend_url)
    loaded_dict["player_scout_sorae_b_left_1_legend"] = player_scout_sorae_b_left_legend_sheet[0]
    loaded_dict["player_scout_sorae_b_left_2_legend"] = player_scout_sorae_b_left_legend_sheet[1]
    loaded_dict["player_scout_sorae_b_left_3_legend"] = player_scout_sorae_b_left_legend_sheet[2]
    loaded_dict["player_scout_sorae_b_left_4_legend"] = player_scout_sorae_b_left_legend_sheet[3]
    player_scout_sorae_b_right_url = resource_path('resources/art/player_scout_sorae_right_b.png')
    player_scout_sorae_b_right_sheet = sprite_sheet((50, 75), player_scout_sorae_b_right_url)
    loaded_dict["player_scout_sorae_b_right_1"] = player_scout_sorae_b_right_sheet[0]
    loaded_dict["player_scout_sorae_b_right_2"] = player_scout_sorae_b_right_sheet[1]
    loaded_dict["player_scout_sorae_b_right_3"] = player_scout_sorae_b_right_sheet[2]
    loaded_dict["player_scout_sorae_b_right_4"] = player_scout_sorae_b_right_sheet[3]
    # basic
    player_scout_sorae_b_right_basic_url = resource_path('resources/art/player_scout_sorae_right_b_basic.png')
    player_scout_sorae_b_right_basic_sheet = sprite_sheet((50, 75), player_scout_sorae_b_right_basic_url)
    loaded_dict["player_scout_sorae_b_right_1_basic"] = player_scout_sorae_b_right_basic_sheet[0]
    loaded_dict["player_scout_sorae_b_right_2_basic"] = player_scout_sorae_b_right_basic_sheet[1]
    loaded_dict["player_scout_sorae_b_right_3_basic"] = player_scout_sorae_b_right_basic_sheet[2]
    loaded_dict["player_scout_sorae_b_right_4_basic"] = player_scout_sorae_b_right_basic_sheet[3]
    # forged
    player_scout_sorae_b_right_forged_url = resource_path('resources/art/player_scout_sorae_right_b_forged.png')
    player_scout_sorae_b_right_forged_sheet = sprite_sheet((50, 75), player_scout_sorae_b_right_forged_url)
    loaded_dict["player_scout_sorae_b_right_1_forged"] = player_scout_sorae_b_right_forged_sheet[0]
    loaded_dict["player_scout_sorae_b_right_2_forged"] = player_scout_sorae_b_right_forged_sheet[1]
    loaded_dict["player_scout_sorae_b_right_3_forged"] = player_scout_sorae_b_right_forged_sheet[2]
    loaded_dict["player_scout_sorae_b_right_4_forged"] = player_scout_sorae_b_right_forged_sheet[3]
    # mythic
    player_scout_sorae_b_right_mythic_url = resource_path('resources/art/player_scout_sorae_right_b_mythic.png')
    player_scout_sorae_b_right_mythic_sheet = sprite_sheet((50, 75), player_scout_sorae_b_right_mythic_url)
    loaded_dict["player_scout_sorae_b_right_1_mythic"] = player_scout_sorae_b_right_mythic_sheet[0]
    loaded_dict["player_scout_sorae_b_right_2_mythic"] = player_scout_sorae_b_right_mythic_sheet[1]
    loaded_dict["player_scout_sorae_b_right_3_mythic"] = player_scout_sorae_b_right_mythic_sheet[2]
    loaded_dict["player_scout_sorae_b_right_4_mythic"] = player_scout_sorae_b_right_mythic_sheet[3]
    # legend
    player_scout_sorae_b_right_legend_url = resource_path('resources/art/player_scout_sorae_right_b_legend.png')
    player_scout_sorae_b_right_legend_sheet = sprite_sheet((50, 75), player_scout_sorae_b_right_legend_url)
    loaded_dict["player_scout_sorae_b_right_1_legend"] = player_scout_sorae_b_right_legend_sheet[0]
    loaded_dict["player_scout_sorae_b_right_2_legend"] = player_scout_sorae_b_right_legend_sheet[1]
    loaded_dict["player_scout_sorae_b_right_3_legend"] = player_scout_sorae_b_right_legend_sheet[2]
    loaded_dict["player_scout_sorae_b_right_4_legend"] = player_scout_sorae_b_right_legend_sheet[3]
    # player battle pets -----------------------------------------------------------------------------------------------
    player_battle_pets_url = resource_path('resources/art/pet_battle_sprites.png')
    player_battle_pets_sheet = sprite_sheet((500, 400), player_battle_pets_url)
    loaded_dict["kasper_battle"] = player_battle_pets_sheet[0]
    loaded_dict["kasper_attack"] = player_battle_pets_sheet[1]
    loaded_dict["torok_battle"] = player_battle_pets_sheet[2]
    loaded_dict["torok_attack"] = player_battle_pets_sheet[3]
    loaded_dict["iriana_battle"] = player_battle_pets_sheet[4]
    loaded_dict["iriana_attack"] = player_battle_pets_sheet[5]
    # player battle pets tier 2 ----------------------------------------------------------------------------------------
    player_battle_pets_tier_2_url = resource_path('resources/art/pet_battle_sprites_tier_2.png')
    player_battle_pets_tier_2_sheet = sprite_sheet((500, 400), player_battle_pets_tier_2_url)
    loaded_dict["kasper_battle_tier_2"] = player_battle_pets_tier_2_sheet[0]
    loaded_dict["kasper_attack_tier_2"] = player_battle_pets_tier_2_sheet[1]
    loaded_dict["torok_battle_tier_2"] = player_battle_pets_tier_2_sheet[2]
    loaded_dict["torok_attack_tier_2"] = player_battle_pets_tier_2_sheet[3]
    loaded_dict["iriana_battle_tier_2"] = player_battle_pets_tier_2_sheet[4]
    loaded_dict["iriana_attack_tier_2"] = player_battle_pets_tier_2_sheet[5]
    # player battle pets tier 3 ----------------------------------------------------------------------------------------
    player_battle_pets_tier_3_url = resource_path('resources/art/pet_battle_sprites_tier_3.png')
    player_battle_pets_tier_3_sheet = sprite_sheet((500, 400), player_battle_pets_tier_3_url)
    loaded_dict["kasper_battle_tier_3"] = player_battle_pets_tier_3_sheet[0]
    loaded_dict["kasper_attack_tier_3"] = player_battle_pets_tier_3_sheet[1]
    loaded_dict["torok_battle_tier_3"] = player_battle_pets_tier_3_sheet[2]
    loaded_dict["torok_attack_tier_3"] = player_battle_pets_tier_3_sheet[3]
    loaded_dict["iriana_battle_tier_3"] = player_battle_pets_tier_3_sheet[4]
    loaded_dict["iriana_attack_tier_3"] = player_battle_pets_tier_3_sheet[5]
    # battle effects ---------------------------------------------------------------------------------------------------
    battle_effects_url = resource_path('resources/art/sprites_battle_effects.png')
    battle_effects_sheet = sprite_sheet((750, 624), battle_effects_url)
    loaded_dict["burn_battle_effect"] = battle_effects_sheet[0]
    loaded_dict["poison_battle_effect"] = battle_effects_sheet[1]
    loaded_dict["bleed_battle_effect"] = battle_effects_sheet[2]
    loaded_dict["barrier_battle_effect"] = battle_effects_sheet[3]
    loaded_dict["crush_battle_effect"] = battle_effects_sheet[4]
    # player battle amuna race -----------------------------------------------------------------------------------------
    # male -------------------------------------------------------------------------------------------------------------
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
    loaded_dict["player_fighter_amuna_strike"] = player_battle_amuna_sheet[8]
    # sense ------------------------------------------------------------------------------------------------------------
    player_battle_amuna_url_sense = resource_path('resources/art/player_battle_sprites_amuna_sense.png')
    player_battle_amuna_sheet_sense = sprite_sheet((750, 624), player_battle_amuna_url_sense)
    loaded_dict["player_mage_amuna_battle_sense"] = player_battle_amuna_sheet_sense[2]
    loaded_dict["player_mage_amuna_attack_sense"] = player_battle_amuna_sheet_sense[3]
    loaded_dict["player_fighter_amuna_battle_sense"] = player_battle_amuna_sheet_sense[4]
    loaded_dict["player_fighter_amuna_attack_sense"] = player_battle_amuna_sheet_sense[5]
    loaded_dict["player_scout_amuna_battle_sense"] = player_battle_amuna_sheet_sense[6]
    loaded_dict["player_scout_amuna_attack_sense"] = player_battle_amuna_sheet_sense[7]
    loaded_dict["player_fighter_amuna_strike_sense"] = player_battle_amuna_sheet_sense[8]
    # basic
    player_battle_amuna_url_basic = resource_path('resources/art/player_battle_sprites_amuna_basic.png')
    player_battle_amuna_sheet_basic = sprite_sheet((750, 624), player_battle_amuna_url_basic)
    loaded_dict["player_mage_amuna_battle_basic"] = player_battle_amuna_sheet_basic[0]
    loaded_dict["player_mage_amuna_attack_basic"] = player_battle_amuna_sheet_basic[1]
    loaded_dict["player_fighter_amuna_battle_basic"] = player_battle_amuna_sheet_basic[2]
    loaded_dict["player_fighter_amuna_attack_basic"] = player_battle_amuna_sheet_basic[3]
    loaded_dict["player_scout_amuna_battle_basic"] = player_battle_amuna_sheet_basic[4]
    loaded_dict["player_scout_amuna_attack_basic"] = player_battle_amuna_sheet_basic[5]
    loaded_dict["player_fighter_amuna_strike_basic"] = player_battle_amuna_sheet_basic[6]
    # basic sense
    player_battle_amuna_url_basic_sense = resource_path('resources/art/player_battle_sprites_amuna_basic_sense.png')
    player_battle_amuna_sheet_basic_sense = sprite_sheet((750, 624), player_battle_amuna_url_basic_sense)
    loaded_dict["player_mage_amuna_battle_basic_sense"] = player_battle_amuna_sheet_basic_sense[0]
    loaded_dict["player_mage_amuna_attack_basic_sense"] = player_battle_amuna_sheet_basic_sense[1]
    loaded_dict["player_fighter_amuna_battle_basic_sense"] = player_battle_amuna_sheet_basic_sense[2]
    loaded_dict["player_fighter_amuna_attack_basic_sense"] = player_battle_amuna_sheet_basic_sense[3]
    loaded_dict["player_scout_amuna_battle_basic_sense"] = player_battle_amuna_sheet_basic_sense[4]
    loaded_dict["player_scout_amuna_attack_basic_sense"] = player_battle_amuna_sheet_basic_sense[5]
    loaded_dict["player_fighter_amuna_strike_basic_sense"] = player_battle_amuna_sheet_basic_sense[6]
    # forged
    player_battle_amuna_url_forged = resource_path('resources/art/player_battle_sprites_amuna_forged.png')
    player_battle_amuna_sheet_forged = sprite_sheet((750, 624), player_battle_amuna_url_forged)
    loaded_dict["player_mage_amuna_battle_forged"] = player_battle_amuna_sheet_forged[0]
    loaded_dict["player_mage_amuna_attack_forged"] = player_battle_amuna_sheet_forged[1]
    loaded_dict["player_fighter_amuna_battle_forged"] = player_battle_amuna_sheet_forged[2]
    loaded_dict["player_fighter_amuna_attack_forged"] = player_battle_amuna_sheet_forged[3]
    loaded_dict["player_scout_amuna_battle_forged"] = player_battle_amuna_sheet_forged[4]
    loaded_dict["player_scout_amuna_attack_forged"] = player_battle_amuna_sheet_forged[5]
    loaded_dict["player_fighter_amuna_strike_forged"] = player_battle_amuna_sheet_forged[6]
    # forged sense
    player_battle_amuna_url_forged_sense = resource_path('resources/art/player_battle_sprites_amuna_'
                                                         'forged_sense.png')
    player_battle_amuna_sheet_forged_sense = sprite_sheet((750, 624), player_battle_amuna_url_forged_sense)
    loaded_dict["player_mage_amuna_battle_forged_sense"] = player_battle_amuna_sheet_forged_sense[0]
    loaded_dict["player_mage_amuna_attack_forged_sense"] = player_battle_amuna_sheet_forged_sense[1]
    loaded_dict["player_fighter_amuna_battle_forged_sense"] = player_battle_amuna_sheet_forged_sense[2]
    loaded_dict["player_fighter_amuna_attack_forged_sense"] = player_battle_amuna_sheet_forged_sense[3]
    loaded_dict["player_scout_amuna_battle_forged_sense"] = player_battle_amuna_sheet_forged_sense[4]
    loaded_dict["player_scout_amuna_attack_forged_sense"] = player_battle_amuna_sheet_forged_sense[5]
    loaded_dict["player_fighter_amuna_strike_forged_sense"] = player_battle_amuna_sheet_forged_sense[6]
    # mythic
    player_battle_amuna_url_mythic = resource_path('resources/art/player_battle_sprites_amuna_mythic.png')
    player_battle_amuna_sheet_mythic = sprite_sheet((750, 624), player_battle_amuna_url_mythic)
    loaded_dict["player_mage_amuna_battle_mythic"] = player_battle_amuna_sheet_mythic[0]
    loaded_dict["player_mage_amuna_attack_mythic"] = player_battle_amuna_sheet_mythic[1]
    loaded_dict["player_fighter_amuna_battle_mythic"] = player_battle_amuna_sheet_mythic[2]
    loaded_dict["player_fighter_amuna_attack_mythic"] = player_battle_amuna_sheet_mythic[3]
    loaded_dict["player_scout_amuna_battle_mythic"] = player_battle_amuna_sheet_mythic[4]
    loaded_dict["player_scout_amuna_attack_mythic"] = player_battle_amuna_sheet_mythic[5]
    loaded_dict["player_fighter_amuna_strike_mythic"] = player_battle_amuna_sheet_mythic[6]
    # mythic sense
    player_battle_amuna_url_mythic_sense = resource_path('resources/art/player_battle_sprites_amuna_'
                                                         'mythic_sense.png')
    player_battle_amuna_sheet_mythic_sense = sprite_sheet((750, 624), player_battle_amuna_url_mythic_sense)
    loaded_dict["player_mage_amuna_battle_mythic_sense"] = player_battle_amuna_sheet_mythic_sense[0]
    loaded_dict["player_mage_amuna_attack_mythic_sense"] = player_battle_amuna_sheet_mythic_sense[1]
    loaded_dict["player_fighter_amuna_battle_mythic_sense"] = player_battle_amuna_sheet_mythic_sense[2]
    loaded_dict["player_fighter_amuna_attack_mythic_sense"] = player_battle_amuna_sheet_mythic_sense[3]
    loaded_dict["player_scout_amuna_battle_mythic_sense"] = player_battle_amuna_sheet_mythic_sense[4]
    loaded_dict["player_scout_amuna_attack_mythic_sense"] = player_battle_amuna_sheet_mythic_sense[5]
    loaded_dict["player_fighter_amuna_strike_mythic_sense"] = player_battle_amuna_sheet_mythic_sense[6]
    # legend
    player_battle_amuna_url_legend = resource_path('resources/art/player_battle_sprites_amuna_legend.png')
    player_battle_amuna_sheet_legend = sprite_sheet((750, 624), player_battle_amuna_url_legend)
    loaded_dict["player_mage_amuna_battle_legend"] = player_battle_amuna_sheet_legend[0]
    loaded_dict["player_mage_amuna_attack_legend"] = player_battle_amuna_sheet_legend[1]
    loaded_dict["player_fighter_amuna_battle_legend"] = player_battle_amuna_sheet_legend[2]
    loaded_dict["player_fighter_amuna_attack_legend"] = player_battle_amuna_sheet_legend[3]
    loaded_dict["player_scout_amuna_battle_legend"] = player_battle_amuna_sheet_legend[4]
    loaded_dict["player_scout_amuna_attack_legend"] = player_battle_amuna_sheet_legend[5]
    loaded_dict["player_fighter_amuna_strike_legend"] = player_battle_amuna_sheet_legend[6]
    # legend sense
    player_battle_amuna_url_legend_sense = resource_path('resources/art/player_battle_sprites_amuna_'
                                                         'legend_sense.png')
    player_battle_amuna_sheet_legend_sense = sprite_sheet((750, 624), player_battle_amuna_url_legend_sense)
    loaded_dict["player_mage_amuna_battle_legend_sense"] = player_battle_amuna_sheet_legend_sense[0]
    loaded_dict["player_mage_amuna_attack_legend_sense"] = player_battle_amuna_sheet_legend_sense[1]
    loaded_dict["player_fighter_amuna_battle_legend_sense"] = player_battle_amuna_sheet_legend_sense[2]
    loaded_dict["player_fighter_amuna_attack_legend_sense"] = player_battle_amuna_sheet_legend_sense[3]
    loaded_dict["player_scout_amuna_battle_legend_sense"] = player_battle_amuna_sheet_legend_sense[4]
    loaded_dict["player_scout_amuna_attack_legend_sense"] = player_battle_amuna_sheet_legend_sense[5]
    loaded_dict["player_fighter_amuna_strike_legend_sense"] = player_battle_amuna_sheet_legend_sense[6]
    # female -----------------------------------------------------------------------------------------------------------
    player_battle_amuna_female_url = resource_path('resources/art/player_battle_sprites_amuna_female.png')
    player_battle_amuna_female_sheet = sprite_sheet((750, 624), player_battle_amuna_female_url)
    loaded_dict["player_no_role_amuna_female_battle"] = player_battle_amuna_female_sheet[0]
    loaded_dict["player_no_role_amuna_female_attack"] = player_battle_amuna_female_sheet[1]
    loaded_dict["player_mage_amuna_female_battle"] = player_battle_amuna_female_sheet[2]
    loaded_dict["player_mage_amuna_female_attack"] = player_battle_amuna_female_sheet[3]
    loaded_dict["player_fighter_amuna_female_battle"] = player_battle_amuna_female_sheet[4]
    loaded_dict["player_fighter_amuna_female_attack"] = player_battle_amuna_female_sheet[5]
    loaded_dict["player_scout_amuna_female_battle"] = player_battle_amuna_female_sheet[6]
    loaded_dict["player_scout_amuna_female_attack"] = player_battle_amuna_female_sheet[7]
    loaded_dict["player_fighter_amuna_female_strike"] = player_battle_amuna_female_sheet[8]
    # sense
    player_battle_amuna_female_sense_url = resource_path('resources/art/player_battle_sprites'
                                                         '_amuna_female_sense.png')
    player_battle_amuna_female_sense_sheet = sprite_sheet((750, 624), player_battle_amuna_female_sense_url)
    loaded_dict["player_no_role_amuna_female_battle_sense"] = player_battle_amuna_female_sense_sheet[0]
    loaded_dict["player_no_role_amuna_female_attack_sense"] = player_battle_amuna_female_sense_sheet[1]
    loaded_dict["player_mage_amuna_female_battle_sense"] = player_battle_amuna_female_sense_sheet[2]
    loaded_dict["player_mage_amuna_female_attack_sense"] = player_battle_amuna_female_sense_sheet[3]
    loaded_dict["player_fighter_amuna_female_battle_sense"] = player_battle_amuna_female_sense_sheet[4]
    loaded_dict["player_fighter_amuna_female_attack_sense"] = player_battle_amuna_female_sense_sheet[5]
    loaded_dict["player_scout_amuna_female_battle_sense"] = player_battle_amuna_female_sense_sheet[6]
    loaded_dict["player_scout_amuna_female_attack_sense"] = player_battle_amuna_female_sense_sheet[7]
    loaded_dict["player_fighter_amuna_female_strike_sense"] = player_battle_amuna_female_sense_sheet[8]
    # basic ------------------------------------------------------------------------------------------------------------
    player_battle_amuna_female_url_basic = resource_path('resources/art/player_battle_sprites_amuna_female_basic.png')
    player_battle_amuna_female_sheet_basic = sprite_sheet((750, 624), player_battle_amuna_female_url_basic)
    loaded_dict["player_mage_amuna_female_battle_basic"] = player_battle_amuna_female_sheet_basic[0]
    loaded_dict["player_mage_amuna_female_attack_basic"] = player_battle_amuna_female_sheet_basic[1]
    loaded_dict["player_fighter_amuna_female_battle_basic"] = player_battle_amuna_female_sheet_basic[2]
    loaded_dict["player_fighter_amuna_female_attack_basic"] = player_battle_amuna_female_sheet_basic[3]
    loaded_dict["player_scout_amuna_female_battle_basic"] = player_battle_amuna_female_sheet_basic[4]
    loaded_dict["player_scout_amuna_female_attack_basic"] = player_battle_amuna_female_sheet_basic[5]
    loaded_dict["player_fighter_amuna_female_strike_basic"] = player_battle_amuna_female_sheet_basic[6]
    # basic sense
    player_battle_amuna_female_sense_url_basic = resource_path('resources/art/player_battle_sprites_amuna_'
                                                               'female_basic_sense.png')
    player_battle_amuna_female_sense_sheet_basic = sprite_sheet((750, 624),
                                                                player_battle_amuna_female_sense_url_basic)
    loaded_dict["player_mage_amuna_female_battle_basic_sense"] = player_battle_amuna_female_sense_sheet_basic[0]
    loaded_dict["player_mage_amuna_female_attack_basic_sense"] = player_battle_amuna_female_sense_sheet_basic[1]
    loaded_dict["player_fighter_amuna_female_battle_basic_sense"] = player_battle_amuna_female_sense_sheet_basic[2]
    loaded_dict["player_fighter_amuna_female_attack_basic_sense"] = player_battle_amuna_female_sense_sheet_basic[3]
    loaded_dict["player_scout_amuna_female_battle_basic_sense"] = player_battle_amuna_female_sense_sheet_basic[4]
    loaded_dict["player_scout_amuna_female_attack_basic_sense"] = player_battle_amuna_female_sense_sheet_basic[5]
    loaded_dict["player_fighter_amuna_female_strike_basic_sense"] = player_battle_amuna_female_sense_sheet_basic[6]
    # forged -----------------------------------------------------------------------------------------------------------
    player_battle_amuna_female_url_forged = resource_path('resources/art/player_battle_sprites_amuna_female_forged.png')
    player_battle_amuna_female_sheet_forged = sprite_sheet((750, 624), player_battle_amuna_female_url_forged)
    loaded_dict["player_mage_amuna_female_battle_forged"] = player_battle_amuna_female_sheet_forged[0]
    loaded_dict["player_mage_amuna_female_attack_forged"] = player_battle_amuna_female_sheet_forged[1]
    loaded_dict["player_fighter_amuna_female_battle_forged"] = player_battle_amuna_female_sheet_forged[2]
    loaded_dict["player_fighter_amuna_female_attack_forged"] = player_battle_amuna_female_sheet_forged[3]
    loaded_dict["player_scout_amuna_female_battle_forged"] = player_battle_amuna_female_sheet_forged[4]
    loaded_dict["player_scout_amuna_female_attack_forged"] = player_battle_amuna_female_sheet_forged[5]
    loaded_dict["player_fighter_amuna_female_strike_forged"] = player_battle_amuna_female_sheet_forged[6]
    # forged sense
    player_battle_amuna_female_sense_url_forged = resource_path('resources/art/player_battle_sprites_amuna_'
                                                                'female_forged_sense.png')
    player_battle_amuna_female_sense_sheet_forged = sprite_sheet((750, 624),
                                                                 player_battle_amuna_female_sense_url_forged)
    loaded_dict["player_mage_amuna_female_battle_forged_sense"] = player_battle_amuna_female_sense_sheet_forged[0]
    loaded_dict["player_mage_amuna_female_attack_forged_sense"] = player_battle_amuna_female_sense_sheet_forged[1]
    loaded_dict["player_fighter_amuna_female_battle_forged_sense"] = player_battle_amuna_female_sense_sheet_forged[2]
    loaded_dict["player_fighter_amuna_female_attack_forged_sense"] = player_battle_amuna_female_sense_sheet_forged[3]
    loaded_dict["player_scout_amuna_female_battle_forged_sense"] = player_battle_amuna_female_sense_sheet_forged[4]
    loaded_dict["player_scout_amuna_female_attack_forged_sense"] = player_battle_amuna_female_sense_sheet_forged[5]
    loaded_dict["player_fighter_amuna_female_strike_forged_sense"] = player_battle_amuna_female_sense_sheet_forged[6]
    # mythic -----------------------------------------------------------------------------------------------------------
    player_battle_amuna_female_url_mythic = resource_path('resources/art/player_battle_sprites_amuna_female_mythic.png')
    player_battle_amuna_female_sheet_mythic = sprite_sheet((750, 624), player_battle_amuna_female_url_mythic)
    loaded_dict["player_mage_amuna_female_battle_mythic"] = player_battle_amuna_female_sheet_mythic[0]
    loaded_dict["player_mage_amuna_female_attack_mythic"] = player_battle_amuna_female_sheet_mythic[1]
    loaded_dict["player_fighter_amuna_female_battle_mythic"] = player_battle_amuna_female_sheet_mythic[2]
    loaded_dict["player_fighter_amuna_female_attack_mythic"] = player_battle_amuna_female_sheet_mythic[3]
    loaded_dict["player_scout_amuna_female_battle_mythic"] = player_battle_amuna_female_sheet_mythic[4]
    loaded_dict["player_scout_amuna_female_attack_mythic"] = player_battle_amuna_female_sheet_mythic[5]
    loaded_dict["player_fighter_amuna_female_strike_mythic"] = player_battle_amuna_female_sheet_mythic[6]
    # mythic sense
    player_battle_amuna_female_sense_url_mythic = resource_path('resources/art/player_battle_sprites_amuna_'
                                                                'female_mythic_sense.png')
    player_battle_amuna_female_sense_sheet_mythic = sprite_sheet((750, 624),
                                                                 player_battle_amuna_female_sense_url_mythic)
    loaded_dict["player_mage_amuna_female_battle_mythic_sense"] = player_battle_amuna_female_sense_sheet_mythic[0]
    loaded_dict["player_mage_amuna_female_attack_mythic_sense"] = player_battle_amuna_female_sense_sheet_mythic[1]
    loaded_dict["player_fighter_amuna_female_battle_mythic_sense"] = player_battle_amuna_female_sense_sheet_mythic[2]
    loaded_dict["player_fighter_amuna_female_attack_mythic_sense"] = player_battle_amuna_female_sense_sheet_mythic[3]
    loaded_dict["player_scout_amuna_female_battle_mythic_sense"] = player_battle_amuna_female_sense_sheet_mythic[4]
    loaded_dict["player_scout_amuna_female_attack_mythic_sense"] = player_battle_amuna_female_sense_sheet_mythic[5]
    loaded_dict["player_fighter_amuna_female_strike_mythic_sense"] = player_battle_amuna_female_sense_sheet_mythic[6]
    # legend -----------------------------------------------------------------------------------------------------------
    player_battle_amuna_female_url_legend = resource_path('resources/art/player_battle_sprites_amuna_female_legend.png')
    player_battle_amuna_female_sheet_legend = sprite_sheet((750, 624), player_battle_amuna_female_url_legend)
    loaded_dict["player_mage_amuna_female_battle_legend"] = player_battle_amuna_female_sheet_legend[0]
    loaded_dict["player_mage_amuna_female_attack_legend"] = player_battle_amuna_female_sheet_legend[1]
    loaded_dict["player_fighter_amuna_female_battle_legend"] = player_battle_amuna_female_sheet_legend[2]
    loaded_dict["player_fighter_amuna_female_attack_legend"] = player_battle_amuna_female_sheet_legend[3]
    loaded_dict["player_scout_amuna_female_battle_legend"] = player_battle_amuna_female_sheet_legend[4]
    loaded_dict["player_scout_amuna_female_attack_legend"] = player_battle_amuna_female_sheet_legend[5]
    loaded_dict["player_fighter_amuna_female_strike_legend"] = player_battle_amuna_female_sheet_legend[6]
    # legend sense
    player_battle_amuna_female_sense_url_legend = resource_path('resources/art/player_battle_sprites_amuna_'
                                                                'female_legend_sense.png')
    player_battle_amuna_female_sense_sheet_legend = sprite_sheet((750, 624),
                                                                 player_battle_amuna_female_sense_url_legend)
    loaded_dict["player_mage_amuna_female_battle_legend_sense"] = player_battle_amuna_female_sense_sheet_legend[0]
    loaded_dict["player_mage_amuna_female_attack_legend_sense"] = player_battle_amuna_female_sense_sheet_legend[1]
    loaded_dict["player_fighter_amuna_female_battle_legend_sense"] = player_battle_amuna_female_sense_sheet_legend[2]
    loaded_dict["player_fighter_amuna_female_attack_legend_sense"] = player_battle_amuna_female_sense_sheet_legend[3]
    loaded_dict["player_scout_amuna_female_battle_legend_sense"] = player_battle_amuna_female_sense_sheet_legend[4]
    loaded_dict["player_scout_amuna_female_attack_legend_sense"] = player_battle_amuna_female_sense_sheet_legend[5]
    loaded_dict["player_fighter_amuna_female_strike_legend_sense"] = player_battle_amuna_female_sense_sheet_legend[6]
    # player battle sorae race -----------------------------------------------------------------------------------------
    # alpha ------------------------------------------------------------------------------------------------------------
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
    loaded_dict["player_fighter_sorae_strike"] = player_battle_sorae_sheet[8]
    # sense
    player_battle_sorae_url_sense = resource_path('resources/art/player_battle_sprites_sorae_sense.png')
    player_battle_sorae_sheet_sense = sprite_sheet((750, 624), player_battle_sorae_url_sense)
    loaded_dict["player_mage_sorae_battle_sense"] = player_battle_sorae_sheet_sense[2]
    loaded_dict["player_mage_sorae_attack_sense"] = player_battle_sorae_sheet_sense[3]
    loaded_dict["player_fighter_sorae_battle_sense"] = player_battle_sorae_sheet_sense[4]
    loaded_dict["player_fighter_sorae_attack_sense"] = player_battle_sorae_sheet_sense[5]
    loaded_dict["player_scout_sorae_battle_sense"] = player_battle_sorae_sheet_sense[6]
    loaded_dict["player_scout_sorae_attack_sense"] = player_battle_sorae_sheet_sense[7]
    loaded_dict["player_fighter_sorae_strike_sense"] = player_battle_sorae_sheet_sense[8]
    # basic
    player_battle_sorae_url_basic = resource_path('resources/art/player_battle_sprites_sorae_basic.png')
    player_battle_sorae_sheet_basic = sprite_sheet((750, 624), player_battle_sorae_url_basic)
    loaded_dict["player_mage_sorae_battle_basic"] = player_battle_sorae_sheet_basic[0]
    loaded_dict["player_mage_sorae_attack_basic"] = player_battle_sorae_sheet_basic[1]
    loaded_dict["player_fighter_sorae_battle_basic"] = player_battle_sorae_sheet_basic[2]
    loaded_dict["player_fighter_sorae_attack_basic"] = player_battle_sorae_sheet_basic[3]
    loaded_dict["player_scout_sorae_battle_basic"] = player_battle_sorae_sheet_basic[4]
    loaded_dict["player_scout_sorae_attack_basic"] = player_battle_sorae_sheet_basic[5]
    loaded_dict["player_fighter_sorae_strike_basic"] = player_battle_sorae_sheet_basic[6]
    # basic sense
    player_battle_sorae_url_basic_sense = resource_path('resources/art/player_battle_sprites_sorae_basic_sense.png')
    player_battle_sorae_sheet_basic_sense = sprite_sheet((750, 624), player_battle_sorae_url_basic_sense)
    loaded_dict["player_mage_sorae_battle_basic_sense"] = player_battle_sorae_sheet_basic_sense[0]
    loaded_dict["player_mage_sorae_attack_basic_sense"] = player_battle_sorae_sheet_basic_sense[1]
    loaded_dict["player_fighter_sorae_battle_basic_sense"] = player_battle_sorae_sheet_basic_sense[2]
    loaded_dict["player_fighter_sorae_attack_basic_sense"] = player_battle_sorae_sheet_basic_sense[3]
    loaded_dict["player_scout_sorae_battle_basic_sense"] = player_battle_sorae_sheet_basic_sense[4]
    loaded_dict["player_scout_sorae_attack_basic_sense"] = player_battle_sorae_sheet_basic_sense[5]
    loaded_dict["player_fighter_sorae_strike_basic_sense"] = player_battle_sorae_sheet_basic_sense[6]
    # forged
    player_battle_sorae_url_forged = resource_path('resources/art/player_battle_sprites_sorae_forged.png')
    player_battle_sorae_sheet_forged = sprite_sheet((750, 624), player_battle_sorae_url_forged)
    loaded_dict["player_mage_sorae_battle_forged"] = player_battle_sorae_sheet_forged[0]
    loaded_dict["player_mage_sorae_attack_forged"] = player_battle_sorae_sheet_forged[1]
    loaded_dict["player_fighter_sorae_battle_forged"] = player_battle_sorae_sheet_forged[2]
    loaded_dict["player_fighter_sorae_attack_forged"] = player_battle_sorae_sheet_forged[3]
    loaded_dict["player_scout_sorae_battle_forged"] = player_battle_sorae_sheet_forged[4]
    loaded_dict["player_scout_sorae_attack_forged"] = player_battle_sorae_sheet_forged[5]
    loaded_dict["player_fighter_sorae_strike_forged"] = player_battle_sorae_sheet_forged[6]
    # forged sense
    player_battle_sorae_url_forged_sense = resource_path('resources/art/player_battle_sprites_sorae_forged_sense.png')
    player_battle_sorae_sheet_forged_sense = sprite_sheet((750, 624), player_battle_sorae_url_forged_sense)
    loaded_dict["player_mage_sorae_battle_forged_sense"] = player_battle_sorae_sheet_forged_sense[0]
    loaded_dict["player_mage_sorae_attack_forged_sense"] = player_battle_sorae_sheet_forged_sense[1]
    loaded_dict["player_fighter_sorae_battle_forged_sense"] = player_battle_sorae_sheet_forged_sense[2]
    loaded_dict["player_fighter_sorae_attack_forged_sense"] = player_battle_sorae_sheet_forged_sense[3]
    loaded_dict["player_scout_sorae_battle_forged_sense"] = player_battle_sorae_sheet_forged_sense[4]
    loaded_dict["player_scout_sorae_attack_forged_sense"] = player_battle_sorae_sheet_forged_sense[5]
    loaded_dict["player_fighter_sorae_strike_forged_sense"] = player_battle_sorae_sheet_forged_sense[6]
    # mythic
    player_battle_sorae_url_mythic = resource_path('resources/art/player_battle_sprites_sorae_mythic.png')
    player_battle_sorae_sheet_mythic = sprite_sheet((750, 624), player_battle_sorae_url_mythic)
    loaded_dict["player_mage_sorae_battle_mythic"] = player_battle_sorae_sheet_mythic[0]
    loaded_dict["player_mage_sorae_attack_mythic"] = player_battle_sorae_sheet_mythic[1]
    loaded_dict["player_fighter_sorae_battle_mythic"] = player_battle_sorae_sheet_mythic[2]
    loaded_dict["player_fighter_sorae_attack_mythic"] = player_battle_sorae_sheet_mythic[3]
    loaded_dict["player_scout_sorae_battle_mythic"] = player_battle_sorae_sheet_mythic[4]
    loaded_dict["player_scout_sorae_attack_mythic"] = player_battle_sorae_sheet_mythic[5]
    loaded_dict["player_fighter_sorae_strike_mythic"] = player_battle_sorae_sheet_mythic[6]
    # mythic sense
    player_battle_sorae_url_mythic_sense = resource_path('resources/art/player_battle_sprites_sorae_mythic_sense.png')
    player_battle_sorae_sheet_mythic_sense = sprite_sheet((750, 624), player_battle_sorae_url_mythic_sense)
    loaded_dict["player_mage_sorae_battle_mythic_sense"] = player_battle_sorae_sheet_mythic_sense[0]
    loaded_dict["player_mage_sorae_attack_mythic_sense"] = player_battle_sorae_sheet_mythic_sense[1]
    loaded_dict["player_fighter_sorae_battle_mythic_sense"] = player_battle_sorae_sheet_mythic_sense[2]
    loaded_dict["player_fighter_sorae_attack_mythic_sense"] = player_battle_sorae_sheet_mythic_sense[3]
    loaded_dict["player_scout_sorae_battle_mythic_sense"] = player_battle_sorae_sheet_mythic_sense[4]
    loaded_dict["player_scout_sorae_attack_mythic_sense"] = player_battle_sorae_sheet_mythic_sense[5]
    loaded_dict["player_fighter_sorae_strike_mythic_sense"] = player_battle_sorae_sheet_mythic_sense[6]
    # legend
    player_battle_sorae_url_legend = resource_path('resources/art/player_battle_sprites_sorae_legend.png')
    player_battle_sorae_sheet_legend = sprite_sheet((750, 624), player_battle_sorae_url_legend)
    loaded_dict["player_mage_sorae_battle_legend"] = player_battle_sorae_sheet_legend[0]
    loaded_dict["player_mage_sorae_attack_legend"] = player_battle_sorae_sheet_legend[1]
    loaded_dict["player_fighter_sorae_battle_legend"] = player_battle_sorae_sheet_legend[2]
    loaded_dict["player_fighter_sorae_attack_legend"] = player_battle_sorae_sheet_legend[3]
    loaded_dict["player_scout_sorae_battle_legend"] = player_battle_sorae_sheet_legend[4]
    loaded_dict["player_scout_sorae_attack_legend"] = player_battle_sorae_sheet_legend[5]
    loaded_dict["player_fighter_sorae_strike_legend"] = player_battle_sorae_sheet_legend[6]
    # legend sense
    player_battle_sorae_url_legend_sense = resource_path('resources/art/player_battle_sprites_sorae_legend_sense.png')
    player_battle_sorae_sheet_legend_sense = sprite_sheet((750, 624), player_battle_sorae_url_legend_sense)
    loaded_dict["player_mage_sorae_battle_legend_sense"] = player_battle_sorae_sheet_legend_sense[0]
    loaded_dict["player_mage_sorae_attack_legend_sense"] = player_battle_sorae_sheet_legend_sense[1]
    loaded_dict["player_fighter_sorae_battle_legend_sense"] = player_battle_sorae_sheet_legend_sense[2]
    loaded_dict["player_fighter_sorae_attack_legend_sense"] = player_battle_sorae_sheet_legend_sense[3]
    loaded_dict["player_scout_sorae_battle_legend_sense"] = player_battle_sorae_sheet_legend_sense[4]
    loaded_dict["player_scout_sorae_attack_legend_sense"] = player_battle_sorae_sheet_legend_sense[5]
    loaded_dict["player_fighter_sorae_strike_legend_sense"] = player_battle_sorae_sheet_legend_sense[6]
    # beta -------------------------------------------------------------------------------------------------------------
    player_battle_sorae_url_b = resource_path('resources/art/player_battle_sprites_sorae_b.png')
    player_battle_sorae_sheet_b = sprite_sheet((750, 624), player_battle_sorae_url_b)
    loaded_dict["player_no_role_sorae_b_battle"] = player_battle_sorae_sheet_b[0]
    loaded_dict["player_no_role_sorae_b_attack"] = player_battle_sorae_sheet_b[1]
    loaded_dict["player_mage_sorae_b_battle"] = player_battle_sorae_sheet_b[2]
    loaded_dict["player_mage_sorae_b_attack"] = player_battle_sorae_sheet_b[3]
    loaded_dict["player_fighter_sorae_b_battle"] = player_battle_sorae_sheet_b[4]
    loaded_dict["player_fighter_sorae_b_attack"] = player_battle_sorae_sheet_b[5]
    loaded_dict["player_scout_sorae_b_battle"] = player_battle_sorae_sheet_b[6]
    loaded_dict["player_scout_sorae_b_attack"] = player_battle_sorae_sheet_b[7]
    loaded_dict["player_fighter_sorae_b_strike"] = player_battle_sorae_sheet_b[8]
    # sense
    player_battle_sorae_url_sense_b = resource_path('resources/art/player_battle_sprites_sorae_b_sense.png')
    player_battle_sorae_sheet_sense_b = sprite_sheet((750, 624), player_battle_sorae_url_sense_b)
    loaded_dict["player_mage_sorae_b_battle_sense"] = player_battle_sorae_sheet_sense_b[2]
    loaded_dict["player_mage_sorae_b_attack_sense"] = player_battle_sorae_sheet_sense_b[3]
    loaded_dict["player_fighter_sorae_b_battle_sense"] = player_battle_sorae_sheet_sense_b[4]
    loaded_dict["player_fighter_sorae_b_attack_sense"] = player_battle_sorae_sheet_sense_b[5]
    loaded_dict["player_scout_sorae_b_battle_sense"] = player_battle_sorae_sheet_sense_b[6]
    loaded_dict["player_scout_sorae_b_attack_sense"] = player_battle_sorae_sheet_sense_b[7]
    loaded_dict["player_fighter_sorae_b_strike_sense"] = player_battle_sorae_sheet_sense_b[8]
    # basic
    player_battle_sorae_url_basic_b = resource_path('resources/art/player_battle_sprites_sorae_b_basic.png')
    player_battle_sorae_sheet_basic_b = sprite_sheet((750, 624), player_battle_sorae_url_basic_b)
    loaded_dict["player_mage_sorae_b_battle_basic"] = player_battle_sorae_sheet_basic_b[0]
    loaded_dict["player_mage_sorae_b_attack_basic"] = player_battle_sorae_sheet_basic_b[1]
    loaded_dict["player_fighter_sorae_b_battle_basic"] = player_battle_sorae_sheet_basic_b[2]
    loaded_dict["player_fighter_sorae_b_attack_basic"] = player_battle_sorae_sheet_basic_b[3]
    loaded_dict["player_scout_sorae_b_battle_basic"] = player_battle_sorae_sheet_basic_b[4]
    loaded_dict["player_scout_sorae_b_attack_basic"] = player_battle_sorae_sheet_basic_b[5]
    loaded_dict["player_fighter_sorae_b_strike_basic"] = player_battle_sorae_sheet_basic_b[6]
    # basic sense
    player_battle_sorae_url_basic_sense_b = resource_path('resources/art/player_battle_sprites_sorae_b_basic_sense.png')
    player_battle_sorae_sheet_basic_sense_b = sprite_sheet((750, 624), player_battle_sorae_url_basic_sense_b)
    loaded_dict["player_mage_sorae_b_battle_basic_sense"] = player_battle_sorae_sheet_basic_sense_b[0]
    loaded_dict["player_mage_sorae_b_attack_basic_sense"] = player_battle_sorae_sheet_basic_sense_b[1]
    loaded_dict["player_fighter_sorae_b_battle_basic_sense"] = player_battle_sorae_sheet_basic_sense_b[2]
    loaded_dict["player_fighter_sorae_b_attack_basic_sense"] = player_battle_sorae_sheet_basic_sense_b[3]
    loaded_dict["player_scout_sorae_b_battle_basic_sense"] = player_battle_sorae_sheet_basic_sense_b[4]
    loaded_dict["player_scout_sorae_b_attack_basic_sense"] = player_battle_sorae_sheet_basic_sense_b[5]
    loaded_dict["player_fighter_sorae_b_strike_basic_sense"] = player_battle_sorae_sheet_basic_sense_b[6]
    # forged
    player_battle_sorae_url_forged_b = resource_path('resources/art/player_battle_sprites_sorae_b_forged.png')
    player_battle_sorae_sheet_forged_b = sprite_sheet((750, 624), player_battle_sorae_url_forged_b)
    loaded_dict["player_mage_sorae_b_battle_forged"] = player_battle_sorae_sheet_forged_b[0]
    loaded_dict["player_mage_sorae_b_attack_forged"] = player_battle_sorae_sheet_forged_b[1]
    loaded_dict["player_fighter_sorae_b_battle_forged"] = player_battle_sorae_sheet_forged_b[2]
    loaded_dict["player_fighter_sorae_b_attack_forged"] = player_battle_sorae_sheet_forged_b[3]
    loaded_dict["player_scout_sorae_b_battle_forged"] = player_battle_sorae_sheet_forged_b[4]
    loaded_dict["player_scout_sorae_b_attack_forged"] = player_battle_sorae_sheet_forged_b[5]
    loaded_dict["player_fighter_sorae_b_strike_forged"] = player_battle_sorae_sheet_forged_b[6]
    # forged sense
    player_battle_sorae_url_forged_sense_b = \
        resource_path('resources/art/player_battle_sprites_sorae_b_forged_sense.png')
    player_battle_sorae_sheet_forged_sense_b = sprite_sheet((750, 624), player_battle_sorae_url_forged_sense_b)
    loaded_dict["player_mage_sorae_b_battle_forged_sense"] = player_battle_sorae_sheet_forged_sense_b[0]
    loaded_dict["player_mage_sorae_b_attack_forged_sense"] = player_battle_sorae_sheet_forged_sense_b[1]
    loaded_dict["player_fighter_sorae_b_battle_forged_sense"] = player_battle_sorae_sheet_forged_sense_b[2]
    loaded_dict["player_fighter_sorae_b_attack_forged_sense"] = player_battle_sorae_sheet_forged_sense_b[3]
    loaded_dict["player_scout_sorae_b_battle_forged_sense"] = player_battle_sorae_sheet_forged_sense_b[4]
    loaded_dict["player_scout_sorae_b_attack_forged_sense"] = player_battle_sorae_sheet_forged_sense_b[5]
    loaded_dict["player_fighter_sorae_b_strike_forged_sense"] = player_battle_sorae_sheet_forged_sense_b[6]
    # mythic
    player_battle_sorae_url_mythic_b = resource_path('resources/art/player_battle_sprites_sorae_b_mythic.png')
    player_battle_sorae_sheet_mythic_b = sprite_sheet((750, 624), player_battle_sorae_url_mythic_b)
    loaded_dict["player_mage_sorae_b_battle_mythic"] = player_battle_sorae_sheet_mythic_b[0]
    loaded_dict["player_mage_sorae_b_attack_mythic"] = player_battle_sorae_sheet_mythic_b[1]
    loaded_dict["player_fighter_sorae_b_battle_mythic"] = player_battle_sorae_sheet_mythic_b[2]
    loaded_dict["player_fighter_sorae_b_attack_mythic"] = player_battle_sorae_sheet_mythic_b[3]
    loaded_dict["player_scout_sorae_b_battle_mythic"] = player_battle_sorae_sheet_mythic_b[4]
    loaded_dict["player_scout_sorae_b_attack_mythic"] = player_battle_sorae_sheet_mythic_b[5]
    loaded_dict["player_fighter_sorae_b_strike_mythic"] = player_battle_sorae_sheet_mythic_b[6]
    # mythic sense
    player_battle_sorae_url_mythic_sense_b = \
        resource_path('resources/art/player_battle_sprites_sorae_b_mythic_sense.png')
    player_battle_sorae_sheet_mythic_sense_b = sprite_sheet((750, 624), player_battle_sorae_url_mythic_sense_b)
    loaded_dict["player_mage_sorae_b_battle_mythic_sense"] = player_battle_sorae_sheet_mythic_sense_b[0]
    loaded_dict["player_mage_sorae_b_attack_mythic_sense"] = player_battle_sorae_sheet_mythic_sense_b[1]
    loaded_dict["player_fighter_sorae_b_battle_mythic_sense"] = player_battle_sorae_sheet_mythic_sense_b[2]
    loaded_dict["player_fighter_sorae_b_attack_mythic_sense"] = player_battle_sorae_sheet_mythic_sense_b[3]
    loaded_dict["player_scout_sorae_b_battle_mythic_sense"] = player_battle_sorae_sheet_mythic_sense_b[4]
    loaded_dict["player_scout_sorae_b_attack_mythic_sense"] = player_battle_sorae_sheet_mythic_sense_b[5]
    loaded_dict["player_fighter_sorae_b_strike_mythic_sense"] = player_battle_sorae_sheet_mythic_sense_b[6]
    # legend
    player_battle_sorae_url_legend_b = resource_path('resources/art/player_battle_sprites_sorae_b_legend.png')
    player_battle_sorae_sheet_legend_b = sprite_sheet((750, 624), player_battle_sorae_url_legend_b)
    loaded_dict["player_mage_sorae_b_battle_legend"] = player_battle_sorae_sheet_legend_b[0]
    loaded_dict["player_mage_sorae_b_attack_legend"] = player_battle_sorae_sheet_legend_b[1]
    loaded_dict["player_fighter_sorae_b_battle_legend"] = player_battle_sorae_sheet_legend_b[2]
    loaded_dict["player_fighter_sorae_b_attack_legend"] = player_battle_sorae_sheet_legend_b[3]
    loaded_dict["player_scout_sorae_b_battle_legend"] = player_battle_sorae_sheet_legend_b[4]
    loaded_dict["player_scout_sorae_b_attack_legend"] = player_battle_sorae_sheet_legend_b[5]
    loaded_dict["player_fighter_sorae_b_strike_legend"] = player_battle_sorae_sheet_legend_b[6]
    # legend sense
    player_battle_sorae_url_legend_sense_b = \
        resource_path('resources/art/player_battle_sprites_sorae_b_legend_sense.png')
    player_battle_sorae_sheet_legend_sense_b = sprite_sheet((750, 624), player_battle_sorae_url_legend_sense_b)
    loaded_dict["player_mage_sorae_b_battle_legend_sense"] = player_battle_sorae_sheet_legend_sense_b[0]
    loaded_dict["player_mage_sorae_b_attack_legend_sense"] = player_battle_sorae_sheet_legend_sense_b[1]
    loaded_dict["player_fighter_sorae_b_battle_legend_sense"] = player_battle_sorae_sheet_legend_sense_b[2]
    loaded_dict["player_fighter_sorae_b_attack_legend_sense"] = player_battle_sorae_sheet_legend_sense_b[3]
    loaded_dict["player_scout_sorae_b_battle_legend_sense"] = player_battle_sorae_sheet_legend_sense_b[4]
    loaded_dict["player_scout_sorae_b_attack_legend_sense"] = player_battle_sorae_sheet_legend_sense_b[5]
    loaded_dict["player_fighter_sorae_b_strike_legend_sense"] = player_battle_sorae_sheet_legend_sense_b[6]
    # player battle nuldar race ----------------------------------------------------------------------------------------
    # male -------------------------------------------------------------------------------------------------------------
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
    loaded_dict["player_fighter_nuldar_strike"] = player_battle_nuldar_sheet[8]
    # sense
    player_battle_nuldar_url_sense = resource_path('resources/art/player_battle_sprites_nuldar_sense.png')
    player_battle_nuldar_sheet_sense = sprite_sheet((750, 624), player_battle_nuldar_url_sense)
    loaded_dict["player_no_role_nuldar_battle_sense"] = player_battle_nuldar_sheet_sense[0]
    loaded_dict["player_no_role_nuldar_attack_sense"] = player_battle_nuldar_sheet_sense[1]
    loaded_dict["player_mage_nuldar_battle_sense"] = player_battle_nuldar_sheet_sense[2]
    loaded_dict["player_mage_nuldar_attack_sense"] = player_battle_nuldar_sheet_sense[3]
    loaded_dict["player_fighter_nuldar_battle_sense"] = player_battle_nuldar_sheet_sense[4]
    loaded_dict["player_fighter_nuldar_attack_sense"] = player_battle_nuldar_sheet_sense[5]
    loaded_dict["player_scout_nuldar_battle_sense"] = player_battle_nuldar_sheet_sense[6]
    loaded_dict["player_scout_nuldar_attack_sense"] = player_battle_nuldar_sheet_sense[7]
    loaded_dict["player_fighter_nuldar_strike_sense"] = player_battle_nuldar_sheet_sense[8]
    # basic
    player_battle_nuldar_url_basic = resource_path('resources/art/player_battle_sprites_nuldar_basic.png')
    player_battle_nuldar_sheet_basic = sprite_sheet((750, 624), player_battle_nuldar_url_basic)
    loaded_dict["player_mage_nuldar_battle_basic"] = player_battle_nuldar_sheet_basic[0]
    loaded_dict["player_mage_nuldar_attack_basic"] = player_battle_nuldar_sheet_basic[1]
    loaded_dict["player_fighter_nuldar_battle_basic"] = player_battle_nuldar_sheet_basic[2]
    loaded_dict["player_fighter_nuldar_attack_basic"] = player_battle_nuldar_sheet_basic[3]
    loaded_dict["player_scout_nuldar_battle_basic"] = player_battle_nuldar_sheet_basic[4]
    loaded_dict["player_scout_nuldar_attack_basic"] = player_battle_nuldar_sheet_basic[5]
    loaded_dict["player_fighter_nuldar_strike_basic"] = player_battle_nuldar_sheet_basic[6]
    # basic sense
    player_battle_nuldar_url_basic_sense = resource_path('resources/art/player_battle_sprites_nuldar_basic_sense.png')
    player_battle_nuldar_sheet_basic_sense = sprite_sheet((750, 624), player_battle_nuldar_url_basic_sense)
    loaded_dict["player_mage_nuldar_battle_basic_sense"] = player_battle_nuldar_sheet_basic_sense[0]
    loaded_dict["player_mage_nuldar_attack_basic_sense"] = player_battle_nuldar_sheet_basic_sense[1]
    loaded_dict["player_fighter_nuldar_battle_basic_sense"] = player_battle_nuldar_sheet_basic_sense[2]
    loaded_dict["player_fighter_nuldar_attack_basic_sense"] = player_battle_nuldar_sheet_basic_sense[3]
    loaded_dict["player_scout_nuldar_battle_basic_sense"] = player_battle_nuldar_sheet_basic_sense[4]
    loaded_dict["player_scout_nuldar_attack_basic_sense"] = player_battle_nuldar_sheet_basic_sense[5]
    loaded_dict["player_fighter_nuldar_strike_basic_sense"] = player_battle_nuldar_sheet_basic_sense[6]
    # forged
    player_battle_nuldar_url_forged = resource_path('resources/art/player_battle_sprites_nuldar_forged.png')
    player_battle_nuldar_sheet_forged = sprite_sheet((750, 624), player_battle_nuldar_url_forged)
    loaded_dict["player_mage_nuldar_battle_forged"] = player_battle_nuldar_sheet_forged[0]
    loaded_dict["player_mage_nuldar_attack_forged"] = player_battle_nuldar_sheet_forged[1]
    loaded_dict["player_fighter_nuldar_battle_forged"] = player_battle_nuldar_sheet_forged[2]
    loaded_dict["player_fighter_nuldar_attack_forged"] = player_battle_nuldar_sheet_forged[3]
    loaded_dict["player_scout_nuldar_battle_forged"] = player_battle_nuldar_sheet_forged[4]
    loaded_dict["player_scout_nuldar_attack_forged"] = player_battle_nuldar_sheet_forged[5]
    loaded_dict["player_fighter_nuldar_strike_forged"] = player_battle_nuldar_sheet_forged[6]
    # forged sense
    player_battle_nuldar_url_forged_sense = resource_path('resources/art/player_battle_sprites_nuldar_forged_sense.png')
    player_battle_nuldar_sheet_forged_sense = sprite_sheet((750, 624), player_battle_nuldar_url_forged_sense)
    loaded_dict["player_mage_nuldar_battle_forged_sense"] = player_battle_nuldar_sheet_forged_sense[0]
    loaded_dict["player_mage_nuldar_attack_forged_sense"] = player_battle_nuldar_sheet_forged_sense[1]
    loaded_dict["player_fighter_nuldar_battle_forged_sense"] = player_battle_nuldar_sheet_forged_sense[2]
    loaded_dict["player_fighter_nuldar_attack_forged_sense"] = player_battle_nuldar_sheet_forged_sense[3]
    loaded_dict["player_scout_nuldar_battle_forged_sense"] = player_battle_nuldar_sheet_forged_sense[4]
    loaded_dict["player_scout_nuldar_attack_forged_sense"] = player_battle_nuldar_sheet_forged_sense[5]
    loaded_dict["player_fighter_nuldar_strike_forged_sense"] = player_battle_nuldar_sheet_forged_sense[6]
    # mythic
    player_battle_nuldar_url_mythic = resource_path('resources/art/player_battle_sprites_nuldar_mythic.png')
    player_battle_nuldar_sheet_mythic = sprite_sheet((750, 624), player_battle_nuldar_url_mythic)
    loaded_dict["player_mage_nuldar_battle_mythic"] = player_battle_nuldar_sheet_mythic[0]
    loaded_dict["player_mage_nuldar_attack_mythic"] = player_battle_nuldar_sheet_mythic[1]
    loaded_dict["player_fighter_nuldar_battle_mythic"] = player_battle_nuldar_sheet_mythic[2]
    loaded_dict["player_fighter_nuldar_attack_mythic"] = player_battle_nuldar_sheet_mythic[3]
    loaded_dict["player_scout_nuldar_battle_mythic"] = player_battle_nuldar_sheet_mythic[4]
    loaded_dict["player_scout_nuldar_attack_mythic"] = player_battle_nuldar_sheet_mythic[5]
    loaded_dict["player_fighter_nuldar_strike_mythic"] = player_battle_nuldar_sheet_mythic[6]
    # mythic sense
    player_battle_nuldar_url_mythic_sense = resource_path('resources/art/player_battle_sprites_nuldar_mythic_sense.png')
    player_battle_nuldar_sheet_mythic_sense = sprite_sheet((750, 624), player_battle_nuldar_url_mythic_sense)
    loaded_dict["player_mage_nuldar_battle_mythic_sense"] = player_battle_nuldar_sheet_mythic_sense[0]
    loaded_dict["player_mage_nuldar_attack_mythic_sense"] = player_battle_nuldar_sheet_mythic_sense[1]
    loaded_dict["player_fighter_nuldar_battle_mythic_sense"] = player_battle_nuldar_sheet_mythic_sense[2]
    loaded_dict["player_fighter_nuldar_attack_mythic_sense"] = player_battle_nuldar_sheet_mythic_sense[3]
    loaded_dict["player_scout_nuldar_battle_mythic_sense"] = player_battle_nuldar_sheet_mythic_sense[4]
    loaded_dict["player_scout_nuldar_attack_mythic_sense"] = player_battle_nuldar_sheet_mythic_sense[5]
    loaded_dict["player_fighter_nuldar_strike_mythic_sense"] = player_battle_nuldar_sheet_mythic_sense[6]
    # legend
    player_battle_nuldar_url_legend = resource_path('resources/art/player_battle_sprites_nuldar_legend.png')
    player_battle_nuldar_sheet_legend = sprite_sheet((750, 624), player_battle_nuldar_url_legend)
    loaded_dict["player_mage_nuldar_battle_legend"] = player_battle_nuldar_sheet_legend[0]
    loaded_dict["player_mage_nuldar_attack_legend"] = player_battle_nuldar_sheet_legend[1]
    loaded_dict["player_fighter_nuldar_battle_legend"] = player_battle_nuldar_sheet_legend[2]
    loaded_dict["player_fighter_nuldar_attack_legend"] = player_battle_nuldar_sheet_legend[3]
    loaded_dict["player_scout_nuldar_battle_legend"] = player_battle_nuldar_sheet_legend[4]
    loaded_dict["player_scout_nuldar_attack_legend"] = player_battle_nuldar_sheet_legend[5]
    loaded_dict["player_fighter_nuldar_strike_legend"] = player_battle_nuldar_sheet_legend[6]
    # legend sense
    player_battle_nuldar_url_legend_sense = resource_path('resources/art/player_battle_sprites_nuldar_legend_sense.png')
    player_battle_nuldar_sheet_legend_sense = sprite_sheet((750, 624), player_battle_nuldar_url_legend_sense)
    loaded_dict["player_mage_nuldar_battle_legend_sense"] = player_battle_nuldar_sheet_legend_sense[0]
    loaded_dict["player_mage_nuldar_attack_legend_sense"] = player_battle_nuldar_sheet_legend_sense[1]
    loaded_dict["player_fighter_nuldar_battle_legend_sense"] = player_battle_nuldar_sheet_legend_sense[2]
    loaded_dict["player_fighter_nuldar_attack_legend_sense"] = player_battle_nuldar_sheet_legend_sense[3]
    loaded_dict["player_scout_nuldar_battle_legend_sense"] = player_battle_nuldar_sheet_legend_sense[4]
    loaded_dict["player_scout_nuldar_attack_legend_sense"] = player_battle_nuldar_sheet_legend_sense[5]
    loaded_dict["player_fighter_nuldar_strike_legend_sense"] = player_battle_nuldar_sheet_legend_sense[6]
    # female -----------------------------------------------------------------------------------------------------------
    player_battle_nuldar_female_url = resource_path('resources/art/player_battle_sprites_nuldar_female.png')
    player_battle_nuldar_female_sheet = sprite_sheet((750, 624), player_battle_nuldar_female_url)
    loaded_dict["player_no_role_nuldar_female_battle"] = player_battle_nuldar_female_sheet[0]
    loaded_dict["player_no_role_nuldar_female_attack"] = player_battle_nuldar_female_sheet[1]
    loaded_dict["player_mage_nuldar_female_battle"] = player_battle_nuldar_female_sheet[2]
    loaded_dict["player_mage_nuldar_female_attack"] = player_battle_nuldar_female_sheet[3]
    loaded_dict["player_fighter_nuldar_female_battle"] = player_battle_nuldar_female_sheet[4]
    loaded_dict["player_fighter_nuldar_female_attack"] = player_battle_nuldar_female_sheet[5]
    loaded_dict["player_scout_nuldar_female_battle"] = player_battle_nuldar_female_sheet[6]
    loaded_dict["player_scout_nuldar_female_attack"] = player_battle_nuldar_female_sheet[7]
    loaded_dict["player_fighter_nuldar_female_strike"] = player_battle_nuldar_female_sheet[8]
    # sense
    player_battle_nuldar_female_url_sense = resource_path('resources/art/player_battle_sprites_nuldar_female_sense.png')
    player_battle_nuldar_female_sheet_sense = sprite_sheet((750, 624), player_battle_nuldar_female_url_sense)
    loaded_dict["player_no_role_nuldar_female_battle_sense"] = player_battle_nuldar_female_sheet_sense[0]
    loaded_dict["player_no_role_nuldar_female_attack_sense"] = player_battle_nuldar_female_sheet_sense[1]
    loaded_dict["player_mage_nuldar_female_battle_sense"] = player_battle_nuldar_female_sheet_sense[2]
    loaded_dict["player_mage_nuldar_female_attack_sense"] = player_battle_nuldar_female_sheet_sense[3]
    loaded_dict["player_fighter_nuldar_female_battle_sense"] = player_battle_nuldar_female_sheet_sense[4]
    loaded_dict["player_fighter_nuldar_female_attack_sense"] = player_battle_nuldar_female_sheet_sense[5]
    loaded_dict["player_scout_nuldar_female_battle_sense"] = player_battle_nuldar_female_sheet_sense[6]
    loaded_dict["player_scout_nuldar_female_attack_sense"] = player_battle_nuldar_female_sheet_sense[7]
    loaded_dict["player_fighter_nuldar_female_strike_sense"] = player_battle_nuldar_female_sheet_sense[8]
    # basic
    player_battle_nuldar_female_url_basic = resource_path('resources/art/player_battle_sprites_nuldar_female_basic.png')
    player_battle_nuldar_female_sheet_basic = sprite_sheet((750, 624), player_battle_nuldar_female_url_basic)
    loaded_dict["player_mage_nuldar_female_battle_basic"] = player_battle_nuldar_female_sheet_basic[0]
    loaded_dict["player_mage_nuldar_female_attack_basic"] = player_battle_nuldar_female_sheet_basic[1]
    loaded_dict["player_fighter_nuldar_female_battle_basic"] = player_battle_nuldar_female_sheet_basic[2]
    loaded_dict["player_fighter_nuldar_female_attack_basic"] = player_battle_nuldar_female_sheet_basic[3]
    loaded_dict["player_scout_nuldar_female_battle_basic"] = player_battle_nuldar_female_sheet_basic[4]
    loaded_dict["player_scout_nuldar_female_attack_basic"] = player_battle_nuldar_female_sheet_basic[5]
    loaded_dict["player_fighter_nuldar_female_strike_basic"] = player_battle_nuldar_female_sheet_basic[6]
    # basic sense
    player_battle_nuldar_female_url_basic_sense = \
        resource_path('resources/art/player_battle_sprites_nuldar_female_basic_sense.png')
    player_battle_nuldar_female_sheet_basic_sense = sprite_sheet((750, 624),
                                                                 player_battle_nuldar_female_url_basic_sense)
    loaded_dict["player_mage_nuldar_female_battle_basic_sense"] = player_battle_nuldar_female_sheet_basic_sense[0]
    loaded_dict["player_mage_nuldar_female_attack_basic_sense"] = player_battle_nuldar_female_sheet_basic_sense[1]
    loaded_dict["player_fighter_nuldar_female_battle_basic_sense"] = player_battle_nuldar_female_sheet_basic_sense[2]
    loaded_dict["player_fighter_nuldar_female_attack_basic_sense"] = player_battle_nuldar_female_sheet_basic_sense[3]
    loaded_dict["player_scout_nuldar_female_battle_basic_sense"] = player_battle_nuldar_female_sheet_basic_sense[4]
    loaded_dict["player_scout_nuldar_female_attack_basic_sense"] = player_battle_nuldar_female_sheet_basic_sense[5]
    loaded_dict["player_fighter_nuldar_female_strike_basic_sense"] = player_battle_nuldar_female_sheet_basic_sense[6]
    # forged
    player_battle_nuldar_female_url_forged = resource_path('resources/art/'
                                                           'player_battle_sprites_nuldar_female_forged.png')
    player_battle_nuldar_female_sheet_forged = sprite_sheet((750, 624), player_battle_nuldar_female_url_forged)
    loaded_dict["player_mage_nuldar_female_battle_forged"] = player_battle_nuldar_female_sheet_forged[0]
    loaded_dict["player_mage_nuldar_female_attack_forged"] = player_battle_nuldar_female_sheet_forged[1]
    loaded_dict["player_fighter_nuldar_female_battle_forged"] = player_battle_nuldar_female_sheet_forged[2]
    loaded_dict["player_fighter_nuldar_female_attack_forged"] = player_battle_nuldar_female_sheet_forged[3]
    loaded_dict["player_scout_nuldar_female_battle_forged"] = player_battle_nuldar_female_sheet_forged[4]
    loaded_dict["player_scout_nuldar_female_attack_forged"] = player_battle_nuldar_female_sheet_forged[5]
    loaded_dict["player_fighter_nuldar_female_strike_forged"] = player_battle_nuldar_female_sheet_forged[6]
    # forged sense
    player_battle_nuldar_female_url_forged_sense = \
        resource_path('resources/art/player_battle_sprites_nuldar_female_forged_sense.png')
    player_battle_nuldar_female_sheet_forged_sense = \
        sprite_sheet((750, 624), player_battle_nuldar_female_url_forged_sense)
    loaded_dict["player_mage_nuldar_female_battle_forged_sense"] = player_battle_nuldar_female_sheet_forged_sense[0]
    loaded_dict["player_mage_nuldar_female_attack_forged_sense"] = player_battle_nuldar_female_sheet_forged_sense[1]
    loaded_dict["player_fighter_nuldar_female_battle_forged_sense"] = player_battle_nuldar_female_sheet_forged_sense[2]
    loaded_dict["player_fighter_nuldar_female_attack_forged_sense"] = player_battle_nuldar_female_sheet_forged_sense[3]
    loaded_dict["player_scout_nuldar_female_battle_forged_sense"] = player_battle_nuldar_female_sheet_forged_sense[4]
    loaded_dict["player_scout_nuldar_female_attack_forged_sense"] = player_battle_nuldar_female_sheet_forged_sense[5]
    loaded_dict["player_fighter_nuldar_female_strike_forged_sense"] = player_battle_nuldar_female_sheet_forged_sense[6]
    # mythic
    player_battle_nuldar_female_url_mythic = resource_path('resources/art/'
                                                           'player_battle_sprites_nuldar_female_mythic.png')
    player_battle_nuldar_female_sheet_mythic = sprite_sheet((750, 624), player_battle_nuldar_female_url_mythic)
    loaded_dict["player_mage_nuldar_female_battle_mythic"] = player_battle_nuldar_female_sheet_mythic[0]
    loaded_dict["player_mage_nuldar_female_attack_mythic"] = player_battle_nuldar_female_sheet_mythic[1]
    loaded_dict["player_fighter_nuldar_female_battle_mythic"] = player_battle_nuldar_female_sheet_mythic[2]
    loaded_dict["player_fighter_nuldar_female_attack_mythic"] = player_battle_nuldar_female_sheet_mythic[3]
    loaded_dict["player_scout_nuldar_female_battle_mythic"] = player_battle_nuldar_female_sheet_mythic[4]
    loaded_dict["player_scout_nuldar_female_attack_mythic"] = player_battle_nuldar_female_sheet_mythic[5]
    loaded_dict["player_fighter_nuldar_female_strike_mythic"] = player_battle_nuldar_female_sheet_mythic[6]
    # mythic sense
    player_battle_nuldar_female_url_mythic_sense = \
        resource_path('resources/art/player_battle_sprites_nuldar_female_mythic_sense.png')
    player_battle_nuldar_female_sheet_mythic_sense = \
        sprite_sheet((750, 624), player_battle_nuldar_female_url_mythic_sense)
    loaded_dict["player_mage_nuldar_female_battle_mythic_sense"] = player_battle_nuldar_female_sheet_mythic_sense[0]
    loaded_dict["player_mage_nuldar_female_attack_mythic_sense"] = player_battle_nuldar_female_sheet_mythic_sense[1]
    loaded_dict["player_fighter_nuldar_female_battle_mythic_sense"] = player_battle_nuldar_female_sheet_mythic_sense[2]
    loaded_dict["player_fighter_nuldar_female_attack_mythic_sense"] = player_battle_nuldar_female_sheet_mythic_sense[3]
    loaded_dict["player_scout_nuldar_female_battle_mythic_sense"] = player_battle_nuldar_female_sheet_mythic_sense[4]
    loaded_dict["player_scout_nuldar_female_attack_mythic_sense"] = player_battle_nuldar_female_sheet_mythic_sense[5]
    loaded_dict["player_fighter_nuldar_female_strike_mythic_sense"] = player_battle_nuldar_female_sheet_mythic_sense[6]
    # legend
    player_battle_nuldar_female_url_legend = resource_path('resources/art/'
                                                           'player_battle_sprites_nuldar_female_legend.png')
    player_battle_nuldar_female_sheet_legend = sprite_sheet((750, 624), player_battle_nuldar_female_url_legend)
    loaded_dict["player_mage_nuldar_female_battle_legend"] = player_battle_nuldar_female_sheet_legend[0]
    loaded_dict["player_mage_nuldar_female_attack_legend"] = player_battle_nuldar_female_sheet_legend[1]
    loaded_dict["player_fighter_nuldar_female_battle_legend"] = player_battle_nuldar_female_sheet_legend[2]
    loaded_dict["player_fighter_nuldar_female_attack_legend"] = player_battle_nuldar_female_sheet_legend[3]
    loaded_dict["player_scout_nuldar_female_battle_legend"] = player_battle_nuldar_female_sheet_legend[4]
    loaded_dict["player_scout_nuldar_female_attack_legend"] = player_battle_nuldar_female_sheet_legend[5]
    loaded_dict["player_fighter_nuldar_female_strike_legend"] = player_battle_nuldar_female_sheet_legend[6]
    # legend sense
    player_battle_nuldar_female_url_legend_sense = \
        resource_path('resources/art/player_battle_sprites_nuldar_female_legend_sense.png')
    player_battle_nuldar_female_sheet_legend_sense = \
        sprite_sheet((750, 624), player_battle_nuldar_female_url_legend_sense)
    loaded_dict["player_mage_nuldar_female_battle_legend_sense"] = player_battle_nuldar_female_sheet_legend_sense[0]
    loaded_dict["player_mage_nuldar_female_attack_legend_sense"] = player_battle_nuldar_female_sheet_legend_sense[1]
    loaded_dict["player_fighter_nuldar_female_battle_legend_sense"] = player_battle_nuldar_female_sheet_legend_sense[2]
    loaded_dict["player_fighter_nuldar_female_attack_legend_sense"] = player_battle_nuldar_female_sheet_legend_sense[3]
    loaded_dict["player_scout_nuldar_female_battle_legend_sense"] = player_battle_nuldar_female_sheet_legend_sense[4]
    loaded_dict["player_scout_nuldar_female_attack_legend_sense"] = player_battle_nuldar_female_sheet_legend_sense[5]
    loaded_dict["player_fighter_nuldar_female_strike_legend_sense"] = player_battle_nuldar_female_sheet_legend_sense[6]

    # player fishing sprites -------------------------------------------------------------------------------------------
    # amuna m ---------------------------------------------------------------------------------------------------------
    amuna_m_fishing_url = resource_path('resources/art/player_amuna_m_fishing.png')
    amuna_m_fishing_sheet = sprite_sheet((100, 100), amuna_m_fishing_url)
    loaded_dict["amuna_m_fishing_right"] = amuna_m_fishing_sheet[0]
    loaded_dict["amuna_m_fishing_down"] = amuna_m_fishing_sheet[1]
    loaded_dict["amuna_m_fishing_up"] = amuna_m_fishing_sheet[2]
    amuna_m_fishing_url_2 = resource_path('resources/art/player_amuna_m_fishing_2.png')
    amuna_m_fishing_sheet_2 = sprite_sheet((100, 100), amuna_m_fishing_url_2)
    loaded_dict["amuna_m_fishing_right_2"] = amuna_m_fishing_sheet_2[0]
    loaded_dict["amuna_m_fishing_down_2"] = amuna_m_fishing_sheet_2[1]
    loaded_dict["amuna_m_fishing_up_2"] = amuna_m_fishing_sheet_2[2]
    amuna_m_fishing_url_3 = resource_path('resources/art/player_amuna_m_fishing_3.png')
    amuna_m_fishing_sheet_3 = sprite_sheet((100, 100), amuna_m_fishing_url_3)
    loaded_dict["amuna_m_fishing_right_3"] = amuna_m_fishing_sheet_3[0]
    loaded_dict["amuna_m_fishing_down_3"] = amuna_m_fishing_sheet_3[1]
    loaded_dict["amuna_m_fishing_up_3"] = amuna_m_fishing_sheet_3[2]
    # amuna f ---------------------------------------------------------------------------------------------------------
    amuna_f_fishing_url = resource_path('resources/art/player_amuna_f_fishing.png')
    amuna_f_fishing_sheet = sprite_sheet((100, 100), amuna_f_fishing_url)
    loaded_dict["amuna_f_fishing_right"] = amuna_f_fishing_sheet[0]
    loaded_dict["amuna_f_fishing_down"] = amuna_f_fishing_sheet[1]
    loaded_dict["amuna_f_fishing_up"] = amuna_f_fishing_sheet[2]
    amuna_f_fishing_url_2 = resource_path('resources/art/player_amuna_f_fishing_2.png')
    amuna_f_fishing_sheet_2 = sprite_sheet((100, 100), amuna_f_fishing_url_2)
    loaded_dict["amuna_f_fishing_right_2"] = amuna_f_fishing_sheet_2[0]
    loaded_dict["amuna_f_fishing_down_2"] = amuna_f_fishing_sheet_2[1]
    loaded_dict["amuna_f_fishing_up_2"] = amuna_f_fishing_sheet_2[2]
    amuna_f_fishing_url_3 = resource_path('resources/art/player_amuna_f_fishing_3.png')
    amuna_f_fishing_sheet_3 = sprite_sheet((100, 100), amuna_f_fishing_url_3)
    loaded_dict["amuna_f_fishing_right_3"] = amuna_f_fishing_sheet_3[0]
    loaded_dict["amuna_f_fishing_down_3"] = amuna_f_fishing_sheet_3[1]
    loaded_dict["amuna_f_fishing_up_3"] = amuna_f_fishing_sheet_3[2]
    # nuldar m ---------------------------------------------------------------------------------------------------------
    nuldar_m_fishing_url = resource_path('resources/art/player_nuldar_m_fishing.png')
    nuldar_m_fishing_sheet = sprite_sheet((100, 100), nuldar_m_fishing_url)
    loaded_dict["nuldar_m_fishing_right"] = nuldar_m_fishing_sheet[0]
    loaded_dict["nuldar_m_fishing_down"] = nuldar_m_fishing_sheet[1]
    loaded_dict["nuldar_m_fishing_up"] = nuldar_m_fishing_sheet[2]
    nuldar_m_fishing_url_2 = resource_path('resources/art/player_nuldar_m_fishing_2.png')
    nuldar_m_fishing_sheet_2 = sprite_sheet((100, 100), nuldar_m_fishing_url_2)
    loaded_dict["nuldar_m_fishing_right_2"] = nuldar_m_fishing_sheet_2[0]
    loaded_dict["nuldar_m_fishing_down_2"] = nuldar_m_fishing_sheet_2[1]
    loaded_dict["nuldar_m_fishing_up_2"] = nuldar_m_fishing_sheet_2[2]
    nuldar_m_fishing_url_3 = resource_path('resources/art/player_nuldar_m_fishing_3.png')
    nuldar_m_fishing_sheet_3 = sprite_sheet((100, 100), nuldar_m_fishing_url_3)
    loaded_dict["nuldar_m_fishing_right_3"] = nuldar_m_fishing_sheet_3[0]
    loaded_dict["nuldar_m_fishing_down_3"] = nuldar_m_fishing_sheet_3[1]
    loaded_dict["nuldar_m_fishing_up_3"] = nuldar_m_fishing_sheet_3[2]
    # nuldar f ---------------------------------------------------------------------------------------------------------
    nuldar_f_fishing_url = resource_path('resources/art/player_nuldar_f_fishing.png')
    nuldar_f_fishing_sheet = sprite_sheet((100, 100), nuldar_f_fishing_url)
    loaded_dict["nuldar_f_fishing_right"] = nuldar_f_fishing_sheet[0]
    loaded_dict["nuldar_f_fishing_down"] = nuldar_f_fishing_sheet[1]
    loaded_dict["nuldar_f_fishing_up"] = nuldar_f_fishing_sheet[2]
    nuldar_f_fishing_url_2 = resource_path('resources/art/player_nuldar_f_fishing_2.png')
    nuldar_f_fishing_sheet_2 = sprite_sheet((100, 100), nuldar_f_fishing_url_2)
    loaded_dict["nuldar_f_fishing_right_2"] = nuldar_f_fishing_sheet_2[0]
    loaded_dict["nuldar_f_fishing_down_2"] = nuldar_f_fishing_sheet_2[1]
    loaded_dict["nuldar_f_fishing_up_2"] = nuldar_f_fishing_sheet_2[2]
    nuldar_f_fishing_url_3 = resource_path('resources/art/player_nuldar_f_fishing_3.png')
    nuldar_f_fishing_sheet_3 = sprite_sheet((100, 100), nuldar_f_fishing_url_3)
    loaded_dict["nuldar_f_fishing_right_3"] = nuldar_f_fishing_sheet_3[0]
    loaded_dict["nuldar_f_fishing_down_3"] = nuldar_f_fishing_sheet_3[1]
    loaded_dict["nuldar_f_fishing_up_3"] = nuldar_f_fishing_sheet_3[2]
    # sorae a ----------------------------------------------------------------------------------------------------------
    sorae_a_fishing_url = resource_path('resources/art/player_sorae_a_fishing.png')
    sorae_a_fishing_sheet = sprite_sheet((100, 100), sorae_a_fishing_url)
    loaded_dict["sorae_a_fishing_right"] = sorae_a_fishing_sheet[0]
    loaded_dict["sorae_a_fishing_down"] = sorae_a_fishing_sheet[1]
    loaded_dict["sorae_a_fishing_up"] = sorae_a_fishing_sheet[2]
    sorae_a_fishing_url_2 = resource_path('resources/art/player_sorae_a_fishing_2.png')
    sorae_a_fishing_sheet_2 = sprite_sheet((100, 100), sorae_a_fishing_url_2)
    loaded_dict["sorae_a_fishing_right_2"] = sorae_a_fishing_sheet_2[0]
    loaded_dict["sorae_a_fishing_down_2"] = sorae_a_fishing_sheet_2[1]
    loaded_dict["sorae_a_fishing_up_2"] = sorae_a_fishing_sheet_2[2]
    sorae_a_fishing_url_3 = resource_path('resources/art/player_sorae_a_fishing_3.png')
    sorae_a_fishing_sheet_3 = sprite_sheet((100, 100), sorae_a_fishing_url_3)
    loaded_dict["sorae_a_fishing_right_3"] = sorae_a_fishing_sheet_3[0]
    loaded_dict["sorae_a_fishing_down_3"] = sorae_a_fishing_sheet_3[1]
    loaded_dict["sorae_a_fishing_up_3"] = sorae_a_fishing_sheet_3[2]
    # sorae b ----------------------------------------------------------------------------------------------------------
    sorae_b_fishing_url = resource_path('resources/art/player_sorae_b_fishing.png')
    sorae_b_fishing_sheet = sprite_sheet((100, 100), sorae_b_fishing_url)
    loaded_dict["sorae_b_fishing_right"] = sorae_b_fishing_sheet[0]
    loaded_dict["sorae_b_fishing_down"] = sorae_b_fishing_sheet[1]
    loaded_dict["sorae_b_fishing_up"] = sorae_b_fishing_sheet[2]
    sorae_b_fishing_url_2 = resource_path('resources/art/player_sorae_b_fishing_2.png')
    sorae_b_fishing_sheet_2 = sprite_sheet((100, 100), sorae_b_fishing_url_2)
    loaded_dict["sorae_b_fishing_right_2"] = sorae_b_fishing_sheet_2[0]
    loaded_dict["sorae_b_fishing_down_2"] = sorae_b_fishing_sheet_2[1]
    loaded_dict["sorae_b_fishing_up_2"] = sorae_b_fishing_sheet_2[2]
    sorae_b_fishing_url_3 = resource_path('resources/art/player_sorae_b_fishing_3.png')
    sorae_b_fishing_sheet_3 = sprite_sheet((100, 100), sorae_b_fishing_url_3)
    loaded_dict["sorae_b_fishing_right_3"] = sorae_b_fishing_sheet_3[0]
    loaded_dict["sorae_b_fishing_down_3"] = sorae_b_fishing_sheet_3[1]
    loaded_dict["sorae_b_fishing_up_3"] = sorae_b_fishing_sheet_3[2]
    # damage overlays --------------------------------------------------------------------------------------------------
    damage_overlays_url = resource_path('resources/art/overlays_damage.png')
    damage_overlays_sheet = sprite_sheet((150, 200), damage_overlays_url)
    loaded_dict["dealt_damage_img"] = damage_overlays_sheet[0]
    loaded_dict["received_damage_img"] = damage_overlays_sheet[1]
    loaded_dict["effective_dealt_damage_img"] = damage_overlays_sheet[2]
    loaded_dict["effective_received_damage_img"] = damage_overlays_sheet[3]
    loaded_dict["non_effective_dealt_damage_img"] = damage_overlays_sheet[4]
    loaded_dict["non_effective_received_damage_img"] = damage_overlays_sheet[5]
    loaded_dict["critical_dealt"] = damage_overlays_sheet[6]
    loaded_dict["critical_received"] = damage_overlays_sheet[7]
    loaded_dict["pet_damage_img"] = damage_overlays_sheet[8]
    loaded_dict["effective_pet_damage_img"] = damage_overlays_sheet[9]
    loaded_dict["non_effective_pet_damage_img"] = damage_overlays_sheet[10]
    loaded_dict["fire_damage_img"] = damage_overlays_sheet[11]
    loaded_dict["edge_health_img"] = damage_overlays_sheet[12]
    loaded_dict["burn_damage_img"] = damage_overlays_sheet[13]
    loaded_dict["poison_damage_img"] = damage_overlays_sheet[14]
    loaded_dict["bleed_damage_img"] = damage_overlays_sheet[15]
    loaded_dict["poison_arrow_damage_img"] = damage_overlays_sheet[16]
    # worker 1 npc -----------------------------------------------------------------------------------------------------
    worker_1_url = resource_path('resources/art/sprites_worker_1.png')
    worker_1_sheet = sprite_sheet((50, 60), worker_1_url)
    loaded_dict["worker_1_a"] = worker_1_sheet[0]
    loaded_dict["worker_1_b"] = worker_1_sheet[1]
    # worker 2 npc -----------------------------------------------------------------------------------------------------
    worker_2_url = resource_path('resources/art/sprites_worker_2.png')
    worker_2_sheet = sprite_sheet((50, 60), worker_2_url)
    loaded_dict["worker_2_full"] = worker_2_sheet[0]
    loaded_dict["worker_2_empty"] = worker_2_sheet[1]
    loaded_dict["worker_2_back_a"] = worker_2_sheet[2]
    loaded_dict["worker_2_back_b"] = worker_2_sheet[3]
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
    loaded_dict["nede_sleep"] = nede_sheet[4]
    # guard npc --------------------------------------------------------------------------------------------------------
    guard_url = resource_path('resources/art/sprites_artherians.png')
    guard_sheet = sprite_sheet((50, 70), guard_url)
    loaded_dict["artherian_down"] = guard_sheet[0]
    loaded_dict["artherian_up"] = guard_sheet[1]
    loaded_dict["artherian_left"] = guard_sheet[2]
    loaded_dict["artherian_right"] = guard_sheet[3]
    # torune npc -------------------------------------------------------------------------------------------------------
    torune_url = resource_path('resources/art/sprites_torune.png')
    torune_sheet = sprite_sheet((50, 62), torune_url)
    loaded_dict["torune_down"] = torune_sheet[0]
    loaded_dict["torune_up"] = torune_sheet[1]
    loaded_dict["torune_left"] = torune_sheet[2]
    loaded_dict["torune_right"] = torune_sheet[3]
    # voruke npc -------------------------------------------------------------------------------------------------------
    voruke_url = resource_path('resources/art/sprites_voruke.png')
    voruke_sheet = sprite_sheet((50, 62), voruke_url)
    loaded_dict["voruke_down"] = voruke_sheet[0]
    loaded_dict["voruke_up"] = voruke_sheet[1]
    loaded_dict["voruke_left"] = voruke_sheet[2]
    loaded_dict["voruke_right"] = voruke_sheet[3]
    # marrow entrance npc ----------------------------------------------------------------------------------------------
    entrance_npc_url = resource_path('resources/art/sprites_entrance_nuldar.png')
    entrance_npc_sheet = sprite_sheet((50, 62), entrance_npc_url)
    loaded_dict["entrance_npc_down"] = entrance_npc_sheet[0]
    loaded_dict["entrance_npc_left"] = entrance_npc_sheet[1]
    loaded_dict["entrance_npc_right"] = entrance_npc_sheet[2]
    loaded_dict["entrance_npc_up"] = entrance_npc_sheet[3]
    # nascent npc ----------------------------------------------------------------------------------------------
    nascent_npc_url = resource_path('resources/art/sprites_nascent_nuldar.png')
    nascent_npc_sheet = sprite_sheet((50, 62), nascent_npc_url)
    loaded_dict["nascent_npc_down"] = nascent_npc_sheet[0]
    loaded_dict["nascent_npc_left"] = nascent_npc_sheet[1]
    loaded_dict["nascent_npc_right"] = nascent_npc_sheet[2]
    loaded_dict["nascent_npc_up"] = nascent_npc_sheet[3]
    # nahun npc ----------------------------------------------------------------------------------------------
    nahun_npc_url = resource_path('resources/art/sprites_nahun.png')
    nahun_npc_sheet = sprite_sheet((50, 62), nahun_npc_url)
    loaded_dict["nahun_down"] = nahun_npc_sheet[0]
    loaded_dict["nahun_left"] = nahun_npc_sheet[1]
    loaded_dict["nahun_right"] = nahun_npc_sheet[2]
    loaded_dict["nahun_up"] = nahun_npc_sheet[3]
    # illisare npc ----------------------------------------------------------------------------------------------
    illisare_npc_url = resource_path('resources/art/sprites_illisare.png')
    illisare_npc_sheet = sprite_sheet((45, 62), illisare_npc_url)
    loaded_dict["illisare_down"] = illisare_npc_sheet[0]
    loaded_dict["illisare_left"] = illisare_npc_sheet[1]
    loaded_dict["illisare_right"] = illisare_npc_sheet[2]
    loaded_dict["illisare_up"] = illisare_npc_sheet[3]
    # zerah npc -------------------------------------------------------------------------------------------------------
    zerah_url = resource_path('resources/art/sprites_zerah.png')
    zerah_sheet = sprite_sheet((50, 62), zerah_url)
    loaded_dict["zerah_down"] = zerah_sheet[0]
    loaded_dict["zerah_up"] = zerah_sheet[1]
    loaded_dict["zerah_left"] = zerah_sheet[2]
    loaded_dict["zerah_right"] = zerah_sheet[3]
    # dionte npc -------------------------------------------------------------------------------------------------------
    dionte_url = resource_path('resources/art/sprites_diontes.png')
    dionte_sheet = sprite_sheet((40, 62), dionte_url)
    loaded_dict["dionte_down"] = dionte_sheet[0]
    loaded_dict["dionte_up"] = dionte_sheet[1]
    loaded_dict["dionte_left"] = dionte_sheet[2]
    loaded_dict["dionte_right"] = dionte_sheet[3]
    # prime and jez npc ------------------------------------------------------------------------------------------------
    prime_jez_url = resource_path('resources/art/sprites_prime_jez.png')
    prime_jez_sheet = sprite_sheet((55, 68), prime_jez_url)
    loaded_dict["prime"] = prime_jez_sheet[0]
    loaded_dict["jez"] = prime_jez_sheet[1]
    loaded_dict["prime_flip"] = prime_jez_sheet[2]
    loaded_dict["jez_flip"] = prime_jez_sheet[3]
    # omoku npc --------------------------------------------------------------------------------------------------------
    omoku_url = resource_path('resources/art/sprites_omoku.png')
    omoku_sheet = sprite_sheet((50, 62), omoku_url)
    loaded_dict["omoku_down"] = omoku_sheet[0]
    loaded_dict["omoku_up"] = omoku_sheet[1]
    loaded_dict["omoku_left"] = omoku_sheet[2]
    loaded_dict["omoku_right"] = omoku_sheet[3]
    # leyre npc --------------------------------------------------------------------------------------------------------
    leyre_url = resource_path('resources/art/sprites_leyre.png')
    leyre_sheet = sprite_sheet((45, 62), leyre_url)
    loaded_dict["leyre_down"] = leyre_sheet[0]
    loaded_dict["leyre_up"] = leyre_sheet[1]
    loaded_dict["leyre_left"] = leyre_sheet[2]
    loaded_dict["leyre_right"] = leyre_sheet[3]
    # everett npc ------------------------------------------------------------------------------------------------------
    everett_url = resource_path('resources/art/sprites_everett.png')
    everett_sheet = sprite_sheet((40, 62), everett_url)
    loaded_dict["everett_down"] = everett_sheet[0]
    loaded_dict["everett_up"] = everett_sheet[1]
    loaded_dict["everett_left"] = everett_sheet[2]
    loaded_dict["everett_right"] = everett_sheet[3]
    # noren npc --------------------------------------------------------------------------------------------------------
    noren_url = resource_path('resources/art/sprites_noren.png')
    noren_sheet = sprite_sheet((50, 62), noren_url)
    loaded_dict["noren_down"] = noren_sheet[0]
    loaded_dict["noren_up"] = noren_sheet[1]
    loaded_dict["noren_left"] = noren_sheet[2]
    loaded_dict["noren_right"] = noren_sheet[3]
    loaded_dict["noren_prism"] = noren_sheet[4]
    # boro npc ---------------------------------------------------------------------------------------------------------
    boro_url = resource_path('resources/art/sprites_boro.png')
    boro_sheet = sprite_sheet((50, 62), boro_url)
    loaded_dict["boro_down"] = boro_sheet[0]
    loaded_dict["boro_up"] = boro_sheet[1]
    loaded_dict["boro_left"] = boro_sheet[2]
    loaded_dict["boro_right"] = boro_sheet[3]
    loaded_dict["boro_prism"] = boro_sheet[4]
    # adria npc --------------------------------------------------------------------------------------------------------
    adria_url = resource_path('resources/art/sprites_maydria.png')
    adria_sheet = sprite_sheet((50, 75), adria_url)
    loaded_dict["maydria_down"] = adria_sheet[0]
    loaded_dict["maydria_up"] = adria_sheet[1]
    loaded_dict["maydria_left"] = adria_sheet[2]
    loaded_dict["maydria_right"] = adria_sheet[3]
    # roroc npc --------------------------------------------------------------------------------------------------------
    roroc_url = resource_path('resources/art/sprites_roroc.png')
    roroc_sheet = sprite_sheet((50, 62), roroc_url)
    loaded_dict["roroc_down"] = roroc_sheet[0]
    loaded_dict["roroc_up"] = roroc_sheet[1]
    loaded_dict["roroc_left"] = roroc_sheet[2]
    loaded_dict["roroc_right"] = roroc_sheet[3]
    # npc interactions -------------------------------------------------------------------------------------------------
    npc_interactions_url = resource_path('resources/art/sprites_npc_interactions.png')
    npc_interactions_sheet = sprite_sheet((220, 300), npc_interactions_url)
    loaded_dict["garan_interaction"] = npc_interactions_sheet[0]
    loaded_dict["maurelle_interaction"] = npc_interactions_sheet[1]
    loaded_dict["celeste_interaction"] = npc_interactions_sheet[2]
    loaded_dict["torune_interaction"] = npc_interactions_sheet[3]
    loaded_dict["voruke_interaction"] = npc_interactions_sheet[4]
    loaded_dict["zerah_interaction"] = npc_interactions_sheet[5]
    loaded_dict["dionte_interaction"] = npc_interactions_sheet[6]
    loaded_dict["omoku_interaction"] = npc_interactions_sheet[7]
    loaded_dict["leyre_interaction"] = npc_interactions_sheet[8]
    loaded_dict["everett_interaction"] = npc_interactions_sheet[9]
    loaded_dict["artherian_interaction"] = npc_interactions_sheet[10]
    loaded_dict["maydria_interaction"] = npc_interactions_sheet[11]
    loaded_dict["kuba_interaction"] = npc_interactions_sheet[12]
    loaded_dict["nahun_interaction"] = npc_interactions_sheet[13]
    loaded_dict["illisare_interaction"] = npc_interactions_sheet[14]
    loaded_dict["roroc_interaction"] = npc_interactions_sheet[15]
    # interaction popup ------------------------------------------------------------------------------------------------
    interaction_popup_url = resource_path('resources/art/popup_interaction.png')
    interaction_popup_sheet = sprite_sheet((125, 25), interaction_popup_url)
    loaded_dict["popup_interaction"] = interaction_popup_sheet[0]
    loaded_dict["popup_interaction_red"] = interaction_popup_sheet[1]
    loaded_dict["popup_interaction_purple"] = interaction_popup_sheet[2]
    loaded_dict["popup_interaction_blue"] = interaction_popup_sheet[3]
    # pets stage 1 -----------------------------------------------------------------------------------------------------
    pets_url = resource_path('resources/art/sprites_pets.png')
    pets_sheet = sprite_sheet((100, 80), pets_url)
    loaded_dict["kasper_down_1"] = pets_sheet[0]
    loaded_dict["torok_down_1"] = pets_sheet[1]
    loaded_dict["iriana_down_1"] = pets_sheet[2]
    loaded_dict["kasper_up_1"] = pets_sheet[3]
    loaded_dict["torok_up_1"] = pets_sheet[4]
    loaded_dict["iriana_up_1"] = pets_sheet[5]
    loaded_dict["kasper_right_1"] = pets_sheet[6]
    loaded_dict["torok_right_1"] = pets_sheet[7]
    loaded_dict["iriana_right_1"] = pets_sheet[8]
    loaded_dict["kasper_left_1"] = pets_sheet[9]
    loaded_dict["torok_left_1"] = pets_sheet[10]
    loaded_dict["iriana_left_1"] = pets_sheet[11]
    loaded_dict["kasper_down_2"] = pets_sheet[12]
    loaded_dict["torok_down_2"] = pets_sheet[13]
    loaded_dict["iriana_down_2"] = pets_sheet[14]
    loaded_dict["kasper_up_2"] = pets_sheet[15]
    loaded_dict["torok_up_2"] = pets_sheet[16]
    loaded_dict["iriana_up_2"] = pets_sheet[17]
    loaded_dict["kasper_right_2"] = pets_sheet[18]
    loaded_dict["torok_right_2"] = pets_sheet[19]
    loaded_dict["iriana_right_2"] = pets_sheet[20]
    loaded_dict["kasper_left_2"] = pets_sheet[21]
    loaded_dict["torok_left_2"] = pets_sheet[22]
    loaded_dict["iriana_left_2"] = pets_sheet[23]
    loaded_dict["kasper_down"] = pets_sheet[24]
    loaded_dict["torok_down"] = pets_sheet[25]
    loaded_dict["iriana_down"] = pets_sheet[26]
    loaded_dict["kasper_up"] = pets_sheet[27]
    loaded_dict["torok_up"] = pets_sheet[28]
    loaded_dict["iriana_up"] = pets_sheet[29]
    loaded_dict["kasper_right"] = pets_sheet[30]
    loaded_dict["torok_right"] = pets_sheet[31]
    loaded_dict["iriana_right"] = pets_sheet[32]
    loaded_dict["kasper_left"] = pets_sheet[33]
    loaded_dict["torok_left"] = pets_sheet[34]
    loaded_dict["iriana_left"] = pets_sheet[35]
    # pets stage 2 -----------------------------------------------------------------------------------------------------
    stage_2_pets_url = resource_path('resources/art/sprites_pets_tier_2.png')
    stage_2_pets_sheet = sprite_sheet((100, 80), stage_2_pets_url)
    loaded_dict["stage_2_kasper_down_1"] = stage_2_pets_sheet[0]
    loaded_dict["stage_2_torok_down_1"] = stage_2_pets_sheet[1]
    loaded_dict["stage_2_iriana_down_1"] = stage_2_pets_sheet[2]
    loaded_dict["stage_2_kasper_up_1"] = stage_2_pets_sheet[3]
    loaded_dict["stage_2_torok_up_1"] = stage_2_pets_sheet[4]
    loaded_dict["stage_2_iriana_up_1"] = stage_2_pets_sheet[5]
    loaded_dict["stage_2_kasper_right_1"] = stage_2_pets_sheet[6]
    loaded_dict["stage_2_torok_right_1"] = stage_2_pets_sheet[7]
    loaded_dict["stage_2_iriana_right_1"] = stage_2_pets_sheet[8]
    loaded_dict["stage_2_kasper_left_1"] = stage_2_pets_sheet[9]
    loaded_dict["stage_2_torok_left_1"] = stage_2_pets_sheet[10]
    loaded_dict["stage_2_iriana_left_1"] = stage_2_pets_sheet[11]
    loaded_dict["stage_2_kasper_down_2"] = stage_2_pets_sheet[12]
    loaded_dict["stage_2_torok_down_2"] = stage_2_pets_sheet[13]
    loaded_dict["stage_2_iriana_down_2"] = stage_2_pets_sheet[14]
    loaded_dict["stage_2_kasper_up_2"] = stage_2_pets_sheet[15]
    loaded_dict["stage_2_torok_up_2"] = stage_2_pets_sheet[16]
    loaded_dict["stage_2_iriana_up_2"] = stage_2_pets_sheet[17]
    loaded_dict["stage_2_kasper_right_2"] = stage_2_pets_sheet[18]
    loaded_dict["stage_2_torok_right_2"] = stage_2_pets_sheet[19]
    loaded_dict["stage_2_iriana_right_2"] = stage_2_pets_sheet[20]
    loaded_dict["stage_2_kasper_left_2"] = stage_2_pets_sheet[21]
    loaded_dict["stage_2_torok_left_2"] = stage_2_pets_sheet[22]
    loaded_dict["stage_2_iriana_left_2"] = stage_2_pets_sheet[23]
    loaded_dict["stage_2_kasper_down"] = stage_2_pets_sheet[24]
    loaded_dict["stage_2_torok_down"] = stage_2_pets_sheet[25]
    loaded_dict["stage_2_iriana_down"] = stage_2_pets_sheet[26]
    loaded_dict["stage_2_kasper_up"] = stage_2_pets_sheet[27]
    loaded_dict["stage_2_torok_up"] = stage_2_pets_sheet[28]
    loaded_dict["stage_2_iriana_up"] = stage_2_pets_sheet[29]
    loaded_dict["stage_2_kasper_right"] = stage_2_pets_sheet[30]
    loaded_dict["stage_2_torok_right"] = stage_2_pets_sheet[31]
    loaded_dict["stage_2_iriana_right"] = stage_2_pets_sheet[32]
    loaded_dict["stage_2_kasper_left"] = stage_2_pets_sheet[33]
    loaded_dict["stage_2_torok_left"] = stage_2_pets_sheet[34]
    loaded_dict["stage_2_iriana_left"] = stage_2_pets_sheet[35]
    # pets stage 3 -----------------------------------------------------------------------------------------------------
    stage_3_pets_url = resource_path('resources/art/sprites_pets_tier_3.png')
    stage_3_pets_sheet = sprite_sheet((100, 80), stage_3_pets_url)
    loaded_dict["stage_3_kasper_down_1"] = stage_3_pets_sheet[0]
    loaded_dict["stage_3_torok_down_1"] = stage_3_pets_sheet[1]
    loaded_dict["stage_3_iriana_down_1"] = stage_3_pets_sheet[2]
    loaded_dict["stage_3_kasper_up_1"] = stage_3_pets_sheet[3]
    loaded_dict["stage_3_torok_up_1"] = stage_3_pets_sheet[4]
    loaded_dict["stage_3_iriana_up_1"] = stage_3_pets_sheet[5]
    loaded_dict["stage_3_kasper_right_1"] = stage_3_pets_sheet[6]
    loaded_dict["stage_3_torok_right_1"] = stage_3_pets_sheet[7]
    loaded_dict["stage_3_iriana_right_1"] = stage_3_pets_sheet[8]
    loaded_dict["stage_3_kasper_left_1"] = stage_3_pets_sheet[9]
    loaded_dict["stage_3_torok_left_1"] = stage_3_pets_sheet[10]
    loaded_dict["stage_3_iriana_left_1"] = stage_3_pets_sheet[11]
    loaded_dict["stage_3_kasper_down_2"] = stage_3_pets_sheet[12]
    loaded_dict["stage_3_torok_down_2"] = stage_3_pets_sheet[13]
    loaded_dict["stage_3_iriana_down_2"] = stage_3_pets_sheet[14]
    loaded_dict["stage_3_kasper_up_2"] = stage_3_pets_sheet[15]
    loaded_dict["stage_3_torok_up_2"] = stage_3_pets_sheet[16]
    loaded_dict["stage_3_iriana_up_2"] = stage_3_pets_sheet[17]
    loaded_dict["stage_3_kasper_right_2"] = stage_3_pets_sheet[18]
    loaded_dict["stage_3_torok_right_2"] = stage_3_pets_sheet[19]
    loaded_dict["stage_3_iriana_right_2"] = stage_3_pets_sheet[20]
    loaded_dict["stage_3_kasper_left_2"] = stage_3_pets_sheet[21]
    loaded_dict["stage_3_torok_left_2"] = stage_3_pets_sheet[22]
    loaded_dict["stage_3_iriana_left_2"] = stage_3_pets_sheet[23]
    loaded_dict["stage_3_kasper_down"] = stage_3_pets_sheet[24]
    loaded_dict["stage_3_torok_down"] = stage_3_pets_sheet[25]
    loaded_dict["stage_3_iriana_down"] = stage_3_pets_sheet[26]
    loaded_dict["stage_3_kasper_up"] = stage_3_pets_sheet[27]
    loaded_dict["stage_3_torok_up"] = stage_3_pets_sheet[28]
    loaded_dict["stage_3_iriana_up"] = stage_3_pets_sheet[29]
    loaded_dict["stage_3_kasper_right"] = stage_3_pets_sheet[30]
    loaded_dict["stage_3_torok_right"] = stage_3_pets_sheet[31]
    loaded_dict["stage_3_iriana_right"] = stage_3_pets_sheet[32]
    loaded_dict["stage_3_kasper_left"] = stage_3_pets_sheet[33]
    loaded_dict["stage_3_torok_left"] = stage_3_pets_sheet[34]
    loaded_dict["stage_3_iriana_left"] = stage_3_pets_sheet[35]
    # pets hatching ----------------------------------------------------------------------------------------------------
    pets_hatching_url = resource_path('resources/art/overlay_seed_hatching.png')
    pets_hatching_sheet = sprite_sheet((400, 400), pets_hatching_url)
    loaded_dict["seed_hatching"] = pets_hatching_sheet[0]
    loaded_dict["kasper_hatching"] = pets_hatching_sheet[1]
    loaded_dict["torok_hatching"] = pets_hatching_sheet[2]
    loaded_dict["iriana_hatching"] = pets_hatching_sheet[3]
    # pets manage window -----------------------------------------------------------------------------------------------
    pet_stages_url = resource_path('resources/art/overlay_pet_stages.png')
    pet_stages_sheet = sprite_sheet((272, 278), pet_stages_url)
    loaded_dict["pet_question"] = pet_stages_sheet[0]
    loaded_dict["pet_kasper_1"] = pet_stages_sheet[1]
    loaded_dict["pet_kasper_2"] = pet_stages_sheet[2]
    loaded_dict["pet_kasper_3"] = pet_stages_sheet[3]
    loaded_dict["pet_torok_1"] = pet_stages_sheet[4]
    loaded_dict["pet_torok_2"] = pet_stages_sheet[5]
    loaded_dict["pet_torok_3"] = pet_stages_sheet[6]
    loaded_dict["pet_iriana_1"] = pet_stages_sheet[7]
    loaded_dict["pet_iriana_2"] = pet_stages_sheet[8]
    loaded_dict["pet_iriana_3"] = pet_stages_sheet[9]
    # enemies ----------------------------------------------------------------------------------------------------------
    enemies_url = resource_path('resources/art/sprites_enemies.png')
    enemies_sheet = sprite_sheet((50, 50), enemies_url)
    loaded_dict["snake"] = enemies_sheet[0]
    loaded_dict["ghoul"] = enemies_sheet[1]
    loaded_dict["magmon"] = enemies_sheet[2]
    loaded_dict["bandile"] = enemies_sheet[3]
    loaded_dict["necrola"] = enemies_sheet[4]
    loaded_dict["osodark"] = enemies_sheet[5]
    loaded_dict["necrola_sleep"] = enemies_sheet[6]
    loaded_dict["atmon"] = enemies_sheet[7]
    loaded_dict["jumano"] = enemies_sheet[8]
    loaded_dict["jumano_red"] = enemies_sheet[9]
    # enemies night ----------------------------------------------------------------------------------------------------
    enemies_night_url = resource_path('resources/art/sprites_enemies_night.png')
    enemies_night_sheet = sprite_sheet((50, 50), enemies_night_url)
    loaded_dict["snake_night"] = enemies_night_sheet[0]
    loaded_dict["ghoul_night"] = enemies_night_sheet[1]
    loaded_dict["magmon_night"] = enemies_night_sheet[2]
    loaded_dict["bandile_night"] = enemies_night_sheet[3]
    loaded_dict["necrola_night"] = enemies_night_sheet[4]
    loaded_dict["osodark_night"] = enemies_night_sheet[5]
    loaded_dict["necrola_sleep_night"] = enemies_night_sheet[6]
    loaded_dict["atmon_night"] = enemies_night_sheet[7]
    loaded_dict["jumano_night"] = enemies_night_sheet[8]
    loaded_dict["jumano_red_night"] = enemies_night_sheet[9]
    # stelli -----------------------------------------------------------------------------------------------------------
    stelli_url = resource_path('resources/art/sprites_stelli.png')
    stelli_sheet = sprite_sheet((50, 50), stelli_url)
    loaded_dict["stelli_a"] = stelli_sheet[0]
    loaded_dict["stelli_b"] = stelli_sheet[1]
    loaded_dict["stelli_c"] = stelli_sheet[2]
    # stelli night -----------------------------------------------------------------------------------------------------
    stelli_night_url = resource_path('resources/art/sprites_stelli_night.png')
    stelli_night_sheet = sprite_sheet((50, 50), stelli_night_url)
    loaded_dict["stelli_a_night"] = stelli_night_sheet[0]
    loaded_dict["stelli_b_night"] = stelli_night_sheet[1]
    loaded_dict["stelli_c_night"] = stelli_night_sheet[2]
    # critters
    critter_url = resource_path('resources/art/sprites_critters.png')
    critter_sheet = sprite_sheet((60, 60), critter_url)
    loaded_dict["critter_front"] = critter_sheet[0]
    loaded_dict["critter_side_left"] = critter_sheet[1]
    loaded_dict["critter_side_left_walk"] = critter_sheet[2]
    loaded_dict["critter_side_right"] = critter_sheet[3]
    loaded_dict["critter_side_right_walk"] = critter_sheet[4]
    # stelli battle ----------------------------------------------------------------------------------------------------
    stelli_battle_url = resource_path('resources/art/sprites_stelli_battle.png')
    stelli_battle_sheet = sprite_sheet((300, 280), stelli_battle_url)
    loaded_dict["stelli_battle_a"] = stelli_battle_sheet[0]
    loaded_dict["stelli_attack_a"] = stelli_battle_sheet[1]
    loaded_dict["stelli_battle_b"] = stelli_battle_sheet[2]
    loaded_dict["stelli_attack_b"] = stelli_battle_sheet[3]
    loaded_dict["stelli_battle_c"] = stelli_battle_sheet[4]
    loaded_dict["stelli_attack_c"] = stelli_battle_sheet[5]
    # stelli battle night ----------------------------------------------------------------------------------------------
    stelli_battle_night_url = resource_path('resources/art/sprites_stelli_battle_night.png')
    stelli_battle_night_sheet = sprite_sheet((300, 280), stelli_battle_night_url)
    loaded_dict["stelli_battle_a_night"] = stelli_battle_night_sheet[0]
    loaded_dict["stelli_attack_a_night"] = stelli_battle_night_sheet[1]
    loaded_dict["stelli_battle_b_night"] = stelli_battle_night_sheet[2]
    loaded_dict["stelli_attack_b_night"] = stelli_battle_night_sheet[3]
    loaded_dict["stelli_battle_c_night"] = stelli_battle_night_sheet[4]
    loaded_dict["stelli_attack_c_night"] = stelli_battle_night_sheet[5]
    # boss enemies -----------------------------------------------------------------------------------------------------
    boss_enemies_url = resource_path('resources/art/sprites_bosses.png')
    boss_enemies_sheet = sprite_sheet((125, 125), boss_enemies_url)
    loaded_dict["chorizon"] = boss_enemies_sheet[0]
    loaded_dict["muchador"] = boss_enemies_sheet[1]
    loaded_dict["muchador_dark"] = boss_enemies_sheet[2]
    loaded_dict["erebyth"] = boss_enemies_sheet[3]
    # enemies highlighted ----------------------------------------------------------------------------------------------
    enemies_high_url = resource_path('resources/art/sprites_enemies_highlighted.png')
    enemies_high_sheet = sprite_sheet((50, 75), enemies_high_url)
    loaded_dict["snake_high"] = enemies_high_sheet[0]
    loaded_dict["ghoul_high"] = enemies_high_sheet[1]
    loaded_dict["magmon_high"] = enemies_high_sheet[2]
    loaded_dict["bandile_high"] = enemies_high_sheet[3]
    loaded_dict["necrola_high"] = enemies_high_sheet[4]
    loaded_dict["atmon_high"] = enemies_high_sheet[5]
    # enemies highlighted night ----------------------------------------------------------------------------------------
    enemies_high_night_url = resource_path('resources/art/sprites_enemies_highlighted_night.png')
    enemies_high_night_sheet = sprite_sheet((50, 75), enemies_high_night_url)
    loaded_dict["snake_high_night"] = enemies_high_night_sheet[0]
    loaded_dict["ghoul_high_night"] = enemies_high_night_sheet[1]
    loaded_dict["magmon_high_night"] = enemies_high_night_sheet[2]
    loaded_dict["bandile_high_night"] = enemies_high_night_sheet[3]
    loaded_dict["necrola_high_night"] = enemies_high_night_sheet[4]
    loaded_dict["atmon_high_night"] = enemies_high_night_sheet[5]
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
    loaded_dict["necrola_battle"] = enemies_battle_sheet[8]
    loaded_dict["necrola_attack"] = enemies_battle_sheet[9]
    loaded_dict["osodark_battle"] = enemies_battle_sheet[10]
    loaded_dict["osodark_attack"] = enemies_battle_sheet[11]
    loaded_dict["atmon_battle"] = enemies_battle_sheet[12]
    loaded_dict["atmon_attack"] = enemies_battle_sheet[13]
    loaded_dict["jumano_battle"] = enemies_battle_sheet[14]
    loaded_dict["jumano_attack"] = enemies_battle_sheet[15]
    # enemies battle night ---------------------------------------------------------------------------------------------
    enemies_battle_night_url = resource_path('resources/art/sprites_enemies_battle_night.png')
    enemies_battle_night_sheet = sprite_sheet((300, 280), enemies_battle_night_url)
    loaded_dict["snake_battle_night"] = enemies_battle_night_sheet[0]
    loaded_dict["snake_attack_night"] = enemies_battle_night_sheet[1]
    loaded_dict["ghoul_battle_night"] = enemies_battle_night_sheet[2]
    loaded_dict["ghoul_attack_night"] = enemies_battle_night_sheet[3]
    loaded_dict["magmon_battle_night"] = enemies_battle_night_sheet[4]
    loaded_dict["magmon_attack_night"] = enemies_battle_night_sheet[5]
    loaded_dict["bandile_battle_night"] = enemies_battle_night_sheet[6]
    loaded_dict["bandile_attack_night"] = enemies_battle_night_sheet[7]
    loaded_dict["necrola_battle_night"] = enemies_battle_night_sheet[8]
    loaded_dict["necrola_attack_night"] = enemies_battle_night_sheet[9]
    loaded_dict["osodark_battle_night"] = enemies_battle_night_sheet[10]
    loaded_dict["osodark_attack_night"] = enemies_battle_night_sheet[11]
    loaded_dict["atmon_battle_night"] = enemies_battle_night_sheet[12]
    loaded_dict["atmon_attack_night"] = enemies_battle_night_sheet[13]
    loaded_dict["jumano_battle_night"] = enemies_battle_night_sheet[14]
    loaded_dict["jumano_attack_night"] = enemies_battle_night_sheet[15]
    # enemies battle effects -------------------------------------------------------------------------------------------
    enemies_battle_effects_url = resource_path('resources/art/sprites_enemies_battle_effects.png')
    enemies_battle_effects_sheet = sprite_sheet((300, 280), enemies_battle_effects_url)
    loaded_dict["ghoul_battle_cloaked"] = enemies_battle_effects_sheet[0]
    loaded_dict["ghoul_attack_cloaked"] = enemies_battle_effects_sheet[1]
    loaded_dict["necrola_battle_cloaked"] = enemies_battle_effects_sheet[2]
    loaded_dict["necrola_attack_cloaked"] = enemies_battle_effects_sheet[3]
    # boss enemies battle ----------------------------------------------------------------------------------------------
    boss_enemies_battle_url = resource_path('resources/art/sprites_bosses_battle.png')
    boss_enemies_battle_sheet = sprite_sheet((500, 500), boss_enemies_battle_url)
    loaded_dict["chorizon_battle"] = boss_enemies_battle_sheet[0]
    loaded_dict["muchador_battle"] = boss_enemies_battle_sheet[1]
    loaded_dict["chinzilla_battle"] = boss_enemies_battle_sheet[2]
    loaded_dict["chorizon_phase"] = boss_enemies_battle_sheet[3]
    loaded_dict["erebyth_battle"] = boss_enemies_battle_sheet[4]
    # boss enemies battle night ----------------------------------------------------------------------------------------
    boss_enemies_battle_night_url = resource_path('resources/art/sprites_bosses_battle_night.png')
    boss_enemies_battle_night_sheet = sprite_sheet((500, 500), boss_enemies_battle_night_url)
    loaded_dict["chorizon_battle_night"] = boss_enemies_battle_night_sheet[0]
    loaded_dict["muchador_battle_night"] = boss_enemies_battle_night_sheet[1]
    loaded_dict["chinzilla_battle_night"] = boss_enemies_battle_night_sheet[2]
    loaded_dict["chorizon_phase_night"] = boss_enemies_battle_night_sheet[3]
    loaded_dict["erebyth_battle_night"] = boss_enemies_battle_night_sheet[4]
    # boss enemies attack ----------------------------------------------------------------------------------------------
    boss_enemies_battle_url = resource_path('resources/art/sprites_bosses_attack.png')
    boss_enemies_battle_sheet = sprite_sheet((500, 500), boss_enemies_battle_url)
    loaded_dict["chorizon_attack"] = boss_enemies_battle_sheet[0]
    loaded_dict["muchador_attack"] = boss_enemies_battle_sheet[1]
    loaded_dict["chinzilla_attack"] = boss_enemies_battle_sheet[2]
    loaded_dict["chorizon_phase_attack"] = boss_enemies_battle_sheet[3]
    loaded_dict["erebyth_phase_attack"] = boss_enemies_battle_sheet[4]
    loaded_dict["erebyth_big_attack"] = boss_enemies_battle_sheet[5]
    loaded_dict["erebyth_attack"] = boss_enemies_battle_sheet[6]
    # enemies attacking ------------------------------------------------------------------------------------------------
    type_overlay_url = resource_path('resources/art/overlay_enemy_types.png')
    type_overlay_sheet = sprite_sheet((50, 50), type_overlay_url)
    loaded_dict["mage_type_overlay"] = type_overlay_sheet[0]
    loaded_dict["fighter_type_overlay"] = type_overlay_sheet[1]
    loaded_dict["scout_type_overlay"] = type_overlay_sheet[2]
    loaded_dict["any_type_overlay"] = type_overlay_sheet[3]
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
    # weapons ----------------------------------------------------------------------------------------------------------
    weapons_url = resource_path('resources/art/overlay_weapon_tiers.png')
    weapons_sheet = sprite_sheet((50, 50), weapons_url)
    loaded_dict["staff_0"] = weapons_sheet[0]
    loaded_dict["staff_1"] = weapons_sheet[1]
    loaded_dict["staff_2"] = weapons_sheet[2]
    loaded_dict["staff_3"] = weapons_sheet[3]
    loaded_dict["staff_4"] = weapons_sheet[4]
    loaded_dict["sword_0"] = weapons_sheet[5]
    loaded_dict["sword_1"] = weapons_sheet[6]
    loaded_dict["sword_2"] = weapons_sheet[7]
    loaded_dict["sword_3"] = weapons_sheet[8]
    loaded_dict["sword_4"] = weapons_sheet[9]
    loaded_dict["bow_0"] = weapons_sheet[10]
    loaded_dict["bow_1"] = weapons_sheet[11]
    loaded_dict["bow_2"] = weapons_sheet[12]
    loaded_dict["bow_3"] = weapons_sheet[13]
    loaded_dict["bow_4"] = weapons_sheet[14]
    # weapons ----------------------------------------------------------------------------------------------------------
    weapons_apothis_url = resource_path('resources/art/overlay_weapon_tiers_apothis.png')
    weapons_apothis_sheet = sprite_sheet((50, 50), weapons_apothis_url)
    loaded_dict["staff_0_apothis"] = weapons_apothis_sheet[0]
    loaded_dict["staff_1_apothis"] = weapons_apothis_sheet[1]
    loaded_dict["staff_2_apothis"] = weapons_apothis_sheet[2]
    loaded_dict["staff_3_apothis"] = weapons_apothis_sheet[3]
    loaded_dict["staff_4_apothis"] = weapons_apothis_sheet[4]
    loaded_dict["sword_0_apothis"] = weapons_apothis_sheet[5]
    loaded_dict["sword_1_apothis"] = weapons_apothis_sheet[6]
    loaded_dict["sword_2_apothis"] = weapons_apothis_sheet[7]
    loaded_dict["sword_3_apothis"] = weapons_apothis_sheet[8]
    loaded_dict["sword_4_apothis"] = weapons_apothis_sheet[9]
    loaded_dict["bow_0_apothis"] = weapons_apothis_sheet[10]
    loaded_dict["bow_1_apothis"] = weapons_apothis_sheet[11]
    loaded_dict["bow_2_apothis"] = weapons_apothis_sheet[12]
    loaded_dict["bow_3_apothis"] = weapons_apothis_sheet[13]
    loaded_dict["bow_4_apothis"] = weapons_apothis_sheet[14]
    # armor ------------------------------------------------------------------------------------------------------------
    armor_url = resource_path('resources/art/overlay_armor_tiers.png')
    armor_sheet = sprite_sheet((50, 50), armor_url)
    loaded_dict["basic_armor"] = armor_sheet[0]
    loaded_dict["forged_armor"] = armor_sheet[1]
    loaded_dict["mythical_armor"] = armor_sheet[2]
    loaded_dict["legendary_armor"] = armor_sheet[3]
    # items ------------------------------------------------------------------------------------------------------------
    items_url = resource_path('resources/art/overlay_items.png')
    items_sheet = sprite_sheet((50, 50), items_url)
    loaded_dict["health_pot_img"] = items_sheet[0]
    loaded_dict["energy_pot_img"] = items_sheet[1]
    loaded_dict["bone_dust_img"] = items_sheet[2]
    loaded_dict["shiny_rock_img"] = items_sheet[3]
    loaded_dict["key_img"] = items_sheet[4]
    loaded_dict["gloves"] = items_sheet[5]
    loaded_dict["ember"] = items_sheet[6]
    loaded_dict["band"] = items_sheet[7]
    loaded_dict["super_pot_img"] = items_sheet[8]
    loaded_dict["seed_img"] = items_sheet[9]
    loaded_dict["seed_ready_img"] = items_sheet[10]
    loaded_dict["fins_img"] = items_sheet[11]
    loaded_dict["pluma_img"] = items_sheet[12]
    loaded_dict["boots_img"] = items_sheet[13]
    loaded_dict["whistle_kasper_img"] = items_sheet[14]
    loaded_dict["whistle_torok_img"] = items_sheet[15]
    loaded_dict["whistle_iriana_img"] = items_sheet[16]
    loaded_dict["pet_cookie_img"] = items_sheet[17]
    loaded_dict["pet_candy_img"] = items_sheet[18]
    loaded_dict["pet_tart_img"] = items_sheet[19]
    loaded_dict["small_health_pot_img"] = items_sheet[20]
    loaded_dict["small_energy_pot_img"] = items_sheet[21]
    loaded_dict["bone_shard"] = items_sheet[22]
    loaded_dict["prism"] = items_sheet[23]
    loaded_dict["casing"] = items_sheet[24]
    loaded_dict["smelted_casing"] = items_sheet[25]
    loaded_dict["enchanted_casing"] = items_sheet[26]
    loaded_dict["seldon_firework"] = items_sheet[27]
    loaded_dict["korlok_firework"] = items_sheet[28]
    loaded_dict["eldream_firework"] = items_sheet[29]
    loaded_dict["seldon_bait"] = items_sheet[30]
    loaded_dict["korlok_bait"] = items_sheet[31]
    loaded_dict["eldream_bait"] = items_sheet[32]
    loaded_dict["mage_book"] = items_sheet[33]
    loaded_dict["fighter_book"] = items_sheet[34]
    loaded_dict["scout_book"] = items_sheet[35]
    loaded_dict["marrow_bait"] = items_sheet[36]
    loaded_dict["cat_card"] = items_sheet[37]
    loaded_dict["trade_deck"] = items_sheet[38]
    loaded_dict["nera_trinket"] = items_sheet[39]
    loaded_dict["aren_trinket"] = items_sheet[40]
    loaded_dict["spirit_trinket"] = items_sheet[41]
    loaded_dict["poison_cure"] = items_sheet[42]
    loaded_dict["burn_cure"] = items_sheet[43]
    loaded_dict["big_cure_potion"] = items_sheet[44]
    loaded_dict["bandage_wrap"] = items_sheet[45]
    loaded_dict["brace"] = items_sheet[46]
    loaded_dict["big_mend_potion"] = items_sheet[47]
    loaded_dict["ore"] = items_sheet[48]
    loaded_dict["log"] = items_sheet[49]
    loaded_dict["supply"] = items_sheet[50]
    loaded_dict["part"] = items_sheet[51]
    # items info -------------------------------------------------------------------------------------------------------
    items_info_url = resource_path('resources/art/overlay_info_items.png')
    items_info_sheet = sprite_sheet((246, 240), items_info_url)
    loaded_dict["info_health_pot_img"] = items_info_sheet[0]
    loaded_dict["info_energy_pot_img"] = items_info_sheet[1]
    loaded_dict["info_basic_armor"] = items_info_sheet[2]
    loaded_dict["info_forged_armor"] = items_info_sheet[3]
    loaded_dict["info_mythical_armor"] = items_info_sheet[4]
    loaded_dict["info_legendary_armor"] = items_info_sheet[5]
    loaded_dict["info_bone_dust_img"] = items_info_sheet[6]
    loaded_dict["info_shiny_rock_img"] = items_info_sheet[7]
    loaded_dict["info_boss_key_img"] = items_info_sheet[8]
    loaded_dict["info_gloves"] = items_info_sheet[9]
    loaded_dict["info_ember"] = items_info_sheet[10]
    loaded_dict["info_band"] = items_info_sheet[11]
    loaded_dict["info_super_pot_img"] = items_info_sheet[12]
    loaded_dict["info_creature_seed"] = items_info_sheet[13]
    loaded_dict["info_creature_seed_ready"] = items_info_sheet[14]
    loaded_dict["info_dread_fins"] = items_info_sheet[15]
    loaded_dict["info_oscura_pluma"] = items_info_sheet[16]
    loaded_dict["info_chroma_boots"] = items_info_sheet[17]
    loaded_dict["info_whistle"] = items_info_sheet[18]
    loaded_dict["info_cookie_img"] = items_info_sheet[19]
    loaded_dict["info_candy_img"] = items_info_sheet[20]
    loaded_dict["info_tart_img"] = items_info_sheet[21]
    loaded_dict["info_big_health_pot_img"] = items_info_sheet[22]
    loaded_dict["info_big_energy_pot_img"] = items_info_sheet[23]
    loaded_dict["info_bone_shard"] = items_info_sheet[24]
    loaded_dict["info_prism"] = items_info_sheet[25]
    loaded_dict["info_casing"] = items_info_sheet[26]
    loaded_dict["info_smelted_casing"] = items_info_sheet[27]
    loaded_dict["info_enchanted_casing"] = items_info_sheet[28]
    loaded_dict["info_seldon_firework"] = items_info_sheet[29]
    loaded_dict["info_korlok_firework"] = items_info_sheet[30]
    loaded_dict["info_eldream_firework"] = items_info_sheet[31]
    loaded_dict["info_seldon_bait"] = items_info_sheet[32]
    loaded_dict["info_korlok_bait"] = items_info_sheet[33]
    loaded_dict["info_eldream_bait"] = items_info_sheet[34]
    loaded_dict["info_mage_book"] = items_info_sheet[35]
    loaded_dict["info_fighter_book"] = items_info_sheet[36]
    loaded_dict["info_scout_book"] = items_info_sheet[37]
    loaded_dict["info_marrow_bait"] = items_info_sheet[38]
    loaded_dict["info_cat_card"] = items_info_sheet[39]
    loaded_dict["info_trade_deck"] = items_info_sheet[40]
    loaded_dict["info_nera"] = items_info_sheet[41]
    loaded_dict["info_aren"] = items_info_sheet[42]
    loaded_dict["info_spirit"] = items_info_sheet[43]
    loaded_dict["info_poison_cure"] = items_info_sheet[44]
    loaded_dict["info_burn_cure"] = items_info_sheet[45]
    loaded_dict["info_bandage_wrap"] = items_info_sheet[46]
    loaded_dict["info_big_cure"] = items_info_sheet[47]
    loaded_dict["info_brace"] = items_info_sheet[48]
    loaded_dict["info_big_mend"] = items_info_sheet[49]
    loaded_dict["info_ore"] = items_info_sheet[50]
    loaded_dict["info_log"] = items_info_sheet[51]
    loaded_dict["info_supply"] = items_info_sheet[52]
    loaded_dict["info_part"] = items_info_sheet[53]
    # buy items info ---------------------------------------------------------------------------------------------------
    buy_items_url = resource_path('resources/art/overlay_buy_items.png')
    buy_items_sheet = sprite_sheet((246, 240), buy_items_url)
    loaded_dict["b_health_pot_img"] = buy_items_sheet[0]
    loaded_dict["b_energy_pot_img"] = buy_items_sheet[1]
    loaded_dict["b_basic_armor"] = buy_items_sheet[2]
    loaded_dict["b_forged_armor"] = buy_items_sheet[3]
    loaded_dict["b_mythical_armor"] = buy_items_sheet[4]
    loaded_dict["b_legendary_armor"] = buy_items_sheet[5]
    loaded_dict["b_cookie_img"] = buy_items_sheet[6]
    loaded_dict["b_candy_img"] = buy_items_sheet[7]
    loaded_dict["b_tart_img"] = buy_items_sheet[8]
    loaded_dict["b_seldon_firework"] = buy_items_sheet[9]
    loaded_dict["b_korlok_firework"] = buy_items_sheet[10]
    loaded_dict["b_eldream_firework"] = buy_items_sheet[11]
    loaded_dict["b_seldon_bait"] = buy_items_sheet[12]
    loaded_dict["b_korlok_bait"] = buy_items_sheet[13]
    loaded_dict["b_eldream_bait"] = buy_items_sheet[14]
    loaded_dict["b_nera"] = buy_items_sheet[15]
    loaded_dict["b_aren"] = buy_items_sheet[16]
    loaded_dict["b_spirit"] = buy_items_sheet[17]
    loaded_dict["b_poison_potion"] = buy_items_sheet[18]
    loaded_dict["b_burn_potion"] = buy_items_sheet[19]
    loaded_dict["b_bandage_wrap"] = buy_items_sheet[20]
    loaded_dict["b_brace"] = buy_items_sheet[21]
    # sell items -------------------------------------------------------------------------------------------------------
    sell_items_url = resource_path('resources/art/overlay_sell_items.png')
    sell_items_sheet = sprite_sheet((246, 240), sell_items_url)
    loaded_dict["s_health_pot_img"] = sell_items_sheet[0]
    loaded_dict["s_energy_pot_img"] = sell_items_sheet[1]
    loaded_dict["s_basic_armor"] = sell_items_sheet[2]
    loaded_dict["s_forged_armor"] = sell_items_sheet[3]
    loaded_dict["s_mythical_armor"] = sell_items_sheet[4]
    loaded_dict["s_legendary_armor"] = sell_items_sheet[5]
    loaded_dict["s_bone_dust_img"] = sell_items_sheet[6]
    loaded_dict["s_shiny_rock_img"] = sell_items_sheet[7]
    loaded_dict["s_ember_img"] = sell_items_sheet[8]
    loaded_dict["s_band_img"] = sell_items_sheet[9]
    loaded_dict["s_fins_img"] = sell_items_sheet[10]
    loaded_dict["s_pluma_img"] = sell_items_sheet[11]
    loaded_dict["s_cookie_img"] = sell_items_sheet[12]
    loaded_dict["s_candy_img"] = sell_items_sheet[13]
    loaded_dict["s_tart_img"] = sell_items_sheet[14]
    loaded_dict["s_bone_shard"] = sell_items_sheet[15]
    loaded_dict["s_seldon_firework"] = sell_items_sheet[16]
    loaded_dict["s_korlok_firework"] = sell_items_sheet[17]
    loaded_dict["s_eldream_firework"] = sell_items_sheet[18]
    loaded_dict["s_seldon_bait"] = sell_items_sheet[19]
    loaded_dict["s_korlok_bait"] = sell_items_sheet[20]
    loaded_dict["s_eldream_bait"] = sell_items_sheet[21]
    loaded_dict["s_marrow_bait"] = sell_items_sheet[22]
    loaded_dict["s_big_health"] = sell_items_sheet[23]
    loaded_dict["s_big_energy"] = sell_items_sheet[24]
    loaded_dict["s_super"] = sell_items_sheet[25]
    loaded_dict["s_cat"] = sell_items_sheet[26]
    loaded_dict["s_nera"] = sell_items_sheet[27]
    loaded_dict["s_aren"] = sell_items_sheet[28]
    loaded_dict["s_spirit"] = sell_items_sheet[29]
    loaded_dict["s_poison_potion"] = sell_items_sheet[30]
    loaded_dict["s_burn_potion"] = sell_items_sheet[31]
    loaded_dict["s_bandage_wrap"] = sell_items_sheet[32]
    loaded_dict["s_big_cure"] = sell_items_sheet[33]
    loaded_dict["s_brace"] = sell_items_sheet[34]
    loaded_dict["s_big_mend"] = sell_items_sheet[35]
    loaded_dict["s_ore"] = sell_items_sheet[36]
    loaded_dict["s_log"] = sell_items_sheet[37]
    loaded_dict["s_supply"] = sell_items_sheet[38]
    loaded_dict["s_part"] = sell_items_sheet[39]
    # apothecary potions -----------------------------------------------------------------------------------------------
    apothecary_potions_url = resource_path('resources/art/overlay_apothecary_potions.png')
    apothecary_potions_sheet = sprite_sheet((75, 75), apothecary_potions_url)
    loaded_dict["apothecary_empty_potion"] = apothecary_potions_sheet[0]
    loaded_dict["apothecary_health_potion"] = apothecary_potions_sheet[1]
    loaded_dict["apothecary_energy_potion"] = apothecary_potions_sheet[2]
    loaded_dict["apothecary_rejuv_potion"] = apothecary_potions_sheet[3]
    loaded_dict["apothecary_cure_potion"] = apothecary_potions_sheet[4]
    loaded_dict["apothecary_mend_potion"] = apothecary_potions_sheet[5]
    # player info windows ----------------------------------------------------------------------------------------------
    player_info_url = resource_path('resources/art/overlay_info_sheets.png')
    player_info_sheet = sprite_sheet((500, 562), player_info_url)
    loaded_dict["character_window_img"] = player_info_sheet[0]
    loaded_dict["journal_window_img"] = player_info_sheet[1]
    # books ------------------------------------------------------------------------------------------------------------
    books_url = resource_path('resources/art/overlay_role_books.png')
    books_sheet = sprite_sheet((700, 525), books_url)
    loaded_dict["mage_book_img"] = books_sheet[0]
    loaded_dict["fighter_book_img"] = books_sheet[1]
    loaded_dict["scout_book_img"] = books_sheet[2]
    # books level 10 ---------------------------------------------------------------------------------------------------
    books_url_10 = resource_path('resources/art/overlay_role_books_10+.png')
    books_sheet_10 = sprite_sheet((700, 525), books_url_10)
    loaded_dict["mage_book_img_10"] = books_sheet_10[0]
    loaded_dict["fighter_book_img_10"] = books_sheet_10[1]
    loaded_dict["scout_book_img_10"] = books_sheet_10[2]
    # books level 20 ---------------------------------------------------------------------------------------------------
    books_url_20 = resource_path('resources/art/overlay_role_books_20+.png')
    books_sheet_20 = sprite_sheet((700, 525), books_url_20)
    loaded_dict["mage_book_img_20"] = books_sheet_20[0]
    loaded_dict["fighter_book_img_20"] = books_sheet_20[1]
    loaded_dict["scout_book_img_20"] = books_sheet_20[2]
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
    loaded_dict["gender high"] = start_buttons_high_sheet[3]
    loaded_dict["gender select"] = start_buttons_high_sheet[4]
    loaded_dict["race select"] = start_buttons_high_sheet[5]
    # race select buttons on character screen --------------------------------------------------------------------------
    race_select_buttons_url = resource_path('resources/art/buttons_race_select.png')
    race_select_buttons_sheet = sprite_sheet((150, 75), race_select_buttons_url)
    loaded_dict["amuna_button_img"] = race_select_buttons_sheet[0]
    loaded_dict["nuldar_button_img"] = race_select_buttons_sheet[1]
    loaded_dict["sorae_button_img"] = race_select_buttons_sheet[2]
    # gender select buttons on character screen ------------------------------------------------------------------------
    gender_select_buttons_url = resource_path('resources/art/buttons_gender_select.png')
    gender_select_buttons_sheet = sprite_sheet((75, 75), gender_select_buttons_url)
    loaded_dict["male_button_img"] = gender_select_buttons_sheet[0]
    loaded_dict["female_button_img"] = gender_select_buttons_sheet[1]
    loaded_dict["alpha_button_img"] = gender_select_buttons_sheet[2]
    loaded_dict["beta_button_img"] = gender_select_buttons_sheet[3]
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
    loaded_dict["potions_button_img"] = buttons_sheet[16]
    loaded_dict["create_potion_img"] = buttons_sheet[17]
    loaded_dict["manage_pets_img"] = buttons_sheet[18]
    loaded_dict["fish_button_img"] = buttons_sheet[19]
    loaded_dict["check_button_img"] = buttons_sheet[20]
    loaded_dict["trade_button_img"] = buttons_sheet[21]
    # deck buttons -----------------------------------------------------------------------------------------------------
    buttons_deck_url = resource_path('resources/art/buttons_deck.png')
    buttons_deck_sheet = sprite_sheet((50, 50), buttons_deck_url)
    loaded_dict["card_deck_img"] = buttons_deck_sheet[0]
    loaded_dict["card_deck_high"] = buttons_deck_sheet[1]
    # fishing level overlay --------------------------------------------------------------------------------------------
    fishing_level_url = resource_path('resources/art/overlay_fishing_level.png')
    fishing_level_sheet = sprite_sheet((281, 31), fishing_level_url)
    loaded_dict["fishing_level_0"] = fishing_level_sheet[0]
    loaded_dict["fishing_level_1"] = fishing_level_sheet[1]
    loaded_dict["fishing_level_2"] = fishing_level_sheet[2]
    # music toggle button ----------------------------------------------------------------------------------------------
    buttons_url = resource_path('resources/art/button_music_toggle.png')
    buttons_sheet = sprite_sheet((50, 57), buttons_url)
    loaded_dict["music_button"] = buttons_sheet[0]
    loaded_dict["music_button_off"] = buttons_sheet[1]
    loaded_dict["music_button_high"] = buttons_sheet[2]
    # fishing spot overlay ---------------------------------------------------------------------------------------------
    fishing_spot_url = resource_path('resources/art/overlay_fishing_spot.png')
    fishing_spot_sheet = sprite_sheet((75, 75), fishing_spot_url)
    loaded_dict["fishing_spot_1"] = fishing_spot_sheet[0]
    loaded_dict["fishing_spot_2"] = fishing_spot_sheet[1]
    loaded_dict["fishing_spot_3"] = fishing_spot_sheet[2]
    loaded_dict["fishing_spot_4"] = fishing_spot_sheet[3]
    # offense/defense overlay ------------------------------------------------------------------------------------------
    offense_defense_url = resource_path('resources/art/overlay_offense_defense_level.png')
    offense_defense_sheet = sprite_sheet((82, 14), offense_defense_url)
    loaded_dict["offense_defense_0"] = offense_defense_sheet[0]
    loaded_dict["offense_defense_1"] = offense_defense_sheet[1]
    loaded_dict["offense_defense_2"] = offense_defense_sheet[2]
    loaded_dict["offense_defense_3"] = offense_defense_sheet[3]
    loaded_dict["offense_defense_4"] = offense_defense_sheet[4]
    loaded_dict["offense_defense_0_crushed"] = offense_defense_sheet[5]
    loaded_dict["offense_defense_1_crushed"] = offense_defense_sheet[6]
    loaded_dict["offense_defense_2_crushed"] = offense_defense_sheet[7]
    loaded_dict["offense_defense_3_crushed"] = offense_defense_sheet[8]
    loaded_dict["offense_defense_4_crushed"] = offense_defense_sheet[9]
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
    loaded_dict["transpose_button_img"] = skill_buttons_sheet[3]
    loaded_dict["stun_button_img"] = skill_buttons_sheet[4]
    loaded_dict["vanish_button_img"] = skill_buttons_sheet[5]
    loaded_dict["fire_button_img"] = skill_buttons_sheet[6]
    loaded_dict["edge_button_img"] = skill_buttons_sheet[7]
    loaded_dict["arrow_button_img"] = skill_buttons_sheet[8]
    loaded_dict["barrier_less_button_img"] = skill_buttons_sheet[9]
    loaded_dict["strike_less_button_img"] = skill_buttons_sheet[10]
    loaded_dict["sense_less_button_img"] = skill_buttons_sheet[11]
    loaded_dict["transpose_less_button_img"] = skill_buttons_sheet[12]
    loaded_dict["stun_less_button_img"] = skill_buttons_sheet[13]
    loaded_dict["vanish_less_button_img"] = skill_buttons_sheet[14]
    loaded_dict["fire_less_button_img"] = skill_buttons_sheet[15]
    loaded_dict["edge_less_button_img"] = skill_buttons_sheet[16]
    loaded_dict["arrow_less_button_img"] = skill_buttons_sheet[17]
    loaded_dict["consume_button_img"] = skill_buttons_sheet[18]
    loaded_dict["consume_less_button_img"] = skill_buttons_sheet[19]
    # skill two overlays -----------------------------------------------------------------------------------------------
    skill_two_url = resource_path('resources/art/overlay_skills_two.png')
    skill_two_sheet = sprite_sheet((300, 300), skill_two_url)
    loaded_dict["stun_img"] = skill_two_sheet[0]
    loaded_dict["vanish_img"] = skill_two_sheet[1]
    # function buttons -------------------------------------------------------------------------------------------------
    game_play_function_buttons_url = resource_path('resources/art/buttons_game_play_function.png')
    game_play_function_buttons_sheet = sprite_sheet((100, 25), game_play_function_buttons_url)
    loaded_dict["save_button_img"] = game_play_function_buttons_sheet[0]
    loaded_dict["map_button_img"] = game_play_function_buttons_sheet[1]
    # select buttons --------------------------------------------------------------------------------------------------
    selection_buttons_url = resource_path('resources/art/buttons_selects.png')
    selection_buttons_sheet = sprite_sheet((184, 42), selection_buttons_url)
    loaded_dict["activate_button"] = selection_buttons_sheet[0]
    loaded_dict["start_seed_button"] = selection_buttons_sheet[1]
    loaded_dict["offense_select_button_img"] = selection_buttons_sheet[2]
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
    loaded_dict["omoku_quest"] = quest_windows_sheet[8]
    loaded_dict["leyre_quest"] = quest_windows_sheet[9]
    loaded_dict["aitor_quest"] = quest_windows_sheet[10]
    loaded_dict["everett_quest"] = quest_windows_sheet[11]
    loaded_dict["artherian_quest"] = quest_windows_sheet[12]
    loaded_dict["artherian_quest_2"] = quest_windows_sheet[13]
    loaded_dict["maydria_quest"] = quest_windows_sheet[14]
    loaded_dict["jerry_quest"] = quest_windows_sheet[15]
    loaded_dict["prime_quest"] = quest_windows_sheet[16]
    loaded_dict["kuba_quest"] = quest_windows_sheet[17]
    loaded_dict["nahun_quest"] = quest_windows_sheet[18]
    loaded_dict["illisare_quest"] = quest_windows_sheet[19]
    loaded_dict["roroc_quest"] = quest_windows_sheet[20]
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
    # quest complete popups 2 ------------------------------------------------------------------------------------------
    quest_popups_2_url = resource_path('resources/art/overlay_quest_completes_2.png')
    quest_popups_2_sheet = sprite_sheet((500, 250), quest_popups_2_url)
    loaded_dict["omoku_complete"] = quest_popups_2_sheet[0]
    loaded_dict["leyre_complete"] = quest_popups_2_sheet[1]
    loaded_dict["aitor_complete"] = quest_popups_2_sheet[2]
    loaded_dict["everett_complete"] = quest_popups_2_sheet[3]
    loaded_dict["artherian_complete"] = quest_popups_2_sheet[4]
    loaded_dict["maydria_complete"] = quest_popups_2_sheet[5]
    loaded_dict["jerry_complete"] = quest_popups_2_sheet[6]
    loaded_dict["prime_complete"] = quest_popups_2_sheet[7]
    loaded_dict["kuba_complete"] = quest_popups_2_sheet[8]
    loaded_dict["nahun_complete"] = quest_popups_2_sheet[9]
    loaded_dict["illisare_complete"] = quest_popups_2_sheet[10]
    loaded_dict["roroc_complete"] = quest_popups_2_sheet[11]
    # quest stars ------------------------------------------------------------------------------------------------------
    quest_stars_url = resource_path('resources/art/overlay_quest_stars.png')
    quest_stars_sheet = sprite_sheet((50, 50), quest_stars_url)
    loaded_dict["quest_start_star"] = quest_stars_sheet[0]
    loaded_dict["quest_progress_star"] = quest_stars_sheet[1]
    loaded_dict["quest_complete_star"] = quest_stars_sheet[2]
    loaded_dict["artherian_start_star"] = quest_stars_sheet[3]
    loaded_dict["artherian_progress_star"] = quest_stars_sheet[4]
    loaded_dict["artherian_complete_star"] = quest_stars_sheet[5]
    loaded_dict["maydria_start_star"] = quest_stars_sheet[6]
    loaded_dict["maydria_progress_star"] = quest_stars_sheet[7]
    loaded_dict["maydria_complete_star"] = quest_stars_sheet[8]
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
    loaded_dict["outpost_popup"] = popups_sheet[6]
    loaded_dict["apothis_popup"] = popups_sheet[7]
    loaded_dict["cloaked_popup"] = popups_sheet[8]
    loaded_dict["condition_popup"] = popups_sheet[9]
    loaded_dict["pet_popup"] = popups_sheet[10]
    # pet advance pop up notifications ---------------------------------------------------------------------------------
    pet_advance_popups_url = resource_path('resources/art/popups_pet_advance.png')
    pet_advance_popups_sheet = sprite_sheet((400, 315), pet_advance_popups_url)
    loaded_dict["kasper_advance_2"] = pet_advance_popups_sheet[0]
    loaded_dict["kasper_advance_3"] = pet_advance_popups_sheet[1]
    loaded_dict["torok_advance_2"] = pet_advance_popups_sheet[2]
    loaded_dict["torok_advance_3"] = pet_advance_popups_sheet[3]
    loaded_dict["iriana_advance_2"] = pet_advance_popups_sheet[4]
    loaded_dict["iriana_advance_3"] = pet_advance_popups_sheet[5]
    # card pop up notifications ----------------------------------------------------------------------------------------
    card_popups_url = resource_path('resources/art/popups_cards.png')
    card_popups_sheet = sprite_sheet((270, 130), card_popups_url)
    loaded_dict["c_snake_popup"] = card_popups_sheet[0]
    loaded_dict["c_ghoul_popup"] = card_popups_sheet[1]
    loaded_dict["c_bandile_popup"] = card_popups_sheet[2]
    loaded_dict["c_magmon_popup"] = card_popups_sheet[3]
    loaded_dict["b_necrola_popup"] = card_popups_sheet[4]
    loaded_dict["b_osodark_popup"] = card_popups_sheet[5]
    loaded_dict["b_atmon_popup"] = card_popups_sheet[6]
    loaded_dict["b_jumano_popup"] = card_popups_sheet[7]
    # quest pine logs --------------------------------------------------------------------------------------------------
    quest_logs_url = resource_path('resources/art/sprite_logs.png')
    quest_logs_sheet = sprite_sheet((40, 50), quest_logs_url)
    loaded_dict["pine_logs_img"] = quest_logs_sheet[0]
    loaded_dict["pine_logs_high_img"] = quest_logs_sheet[1]
    # quest pine logs pile----------------------------------------------------------------------------------------------
    quest_logs_pile_url = resource_path('resources/art/sprite_logs_pile.png')
    quest_logs_pile_sheet = sprite_sheet((50, 50), quest_logs_pile_url)
    loaded_dict["pine_logs_pile_img"] = quest_logs_pile_sheet[0]
    loaded_dict["pine_logs_piled_img"] = quest_logs_pile_sheet[1]
    # quest logs visual ------------------------------------------------------------------------------------------------
    quest_logs_big_url = resource_path('resources/art/sprite_logs_big.png')
    quest_logs_big_sheet = sprite_sheet((300, 250), quest_logs_big_url)
    loaded_dict["pine_logs_big_img"] = quest_logs_big_sheet[0]
    loaded_dict["pine_logs_big_pile_img"] = quest_logs_big_sheet[1]
    # quest ore visual ------------------------------------------------------------------------------------------------
    quest_ore_big_url = resource_path('resources/art/sprite_ore_big.png')
    quest_ore_big_sheet = sprite_sheet((300, 250), quest_ore_big_url)
    loaded_dict["ore_big_img"] = quest_ore_big_sheet[0]
    loaded_dict["ore_big_pile_img"] = quest_ore_big_sheet[1]
    # quest supplies --------------------------------------------------------------------------------------------------
    quest_supplies_url = resource_path('resources/art/sprites_supplies.png')
    quest_supplies_sheet = sprite_sheet((50, 50), quest_supplies_url)
    loaded_dict["quest_supplies"] = quest_supplies_sheet[0]
    loaded_dict["quest_supplies_high"] = quest_supplies_sheet[1]
    # rocks ------------------------------------------------------------------------------------------------------------
    rocks_url = resource_path('resources/art/sprite_rock.png')
    rocks_sheet = sprite_sheet((125, 125), rocks_url)
    loaded_dict["rock"] = rocks_sheet[0]
    loaded_dict["rock_small"] = rocks_sheet[1]
    # flowers ----------------------------------------------------------------------------------------------------------
    flowers_url = resource_path('resources/art/sprites_flowers.png')
    flowers_sheet = sprite_sheet((40, 60), flowers_url)
    loaded_dict["flower_seldon"] = flowers_sheet[0]
    loaded_dict["flower_seldon_high"] = flowers_sheet[1]
    loaded_dict["flower_eldream"] = flowers_sheet[2]
    loaded_dict["flower_eldream_high"] = flowers_sheet[3]
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
    # cat petting animation sprites ------------------------------------------------------------------------------------
    cat_pet_url = resource_path('resources/art/sprites_cat_pet.png')
    cat_pet_sheet = sprite_sheet((125, 125), cat_pet_url)
    loaded_dict["seldon_shop_cat_pet_img"] = cat_pet_sheet[0]
    loaded_dict["academia_cat_pet_img"] = cat_pet_sheet[1]
    loaded_dict["korlok_shop_cat_pet_img"] = cat_pet_sheet[2]
    loaded_dict["apothecary_cat_pet_img"] = cat_pet_sheet[3]
    loaded_dict["eldream_shop_cat_pet_img"] = cat_pet_sheet[4]
    loaded_dict["menagerie_cat_pet_img"] = cat_pet_sheet[5]
    loaded_dict["marrow_cat_pet_img"] = cat_pet_sheet[6]
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
    loaded_dict["amuna_female"] = character_selections_sheet[1]
    loaded_dict["nuldar_location"] = character_selections_sheet[2]
    loaded_dict["nuldar_female"] = character_selections_sheet[3]
    loaded_dict["sorae_location"] = character_selections_sheet[4]
    loaded_dict["sorae_b"] = character_selections_sheet[5]
    # dungeon items ----------------------------------------------------------------------------------------------------
    dungeon_items_url = resource_path('resources/art/sprites_dungeon_items.png')
    dungeon_items_sheet = sprite_sheet((75, 100), dungeon_items_url)
    loaded_dict["dungeon_crate"] = dungeon_items_sheet[0]
    loaded_dict["dungeon_switch_inactive"] = dungeon_items_sheet[1]
    loaded_dict["dungeon_switch_active"] = dungeon_items_sheet[2]
    loaded_dict["dungeon_switch_full"] = dungeon_items_sheet[3]
    loaded_dict["item_block"] = dungeon_items_sheet[4]
    # dungeon chest closed and open ------------------------------------------------------------------------------------
    dungeon_chest_url = resource_path('resources/art/sprite_dungeon_chest.png')
    dungeon_chest_sheet = sprite_sheet((175, 150), dungeon_chest_url)
    loaded_dict["dungeon_chest"] = dungeon_chest_sheet[0]
    loaded_dict["dungeon_chest_open"] = dungeon_chest_sheet[1]
    # marrow ramparts switches
    ramps_switches_url = resource_path('resources/art/overlay_ramps_switches.png')
    ramps_switches_sheet = sprite_sheet((140, 200), ramps_switches_url)
    loaded_dict["ramp_switch_west"] = ramps_switches_sheet[0]
    loaded_dict["ramp_switch_east"] = ramps_switches_sheet[1]
    # apothis sprites
    apothis_url = resource_path('resources/art/sprites_apothis.png')
    apothis_sheet = sprite_sheet((60, 95), apothis_url)
    loaded_dict["apothis_front"] = apothis_sheet[0]
    loaded_dict["apothis_back"] = apothis_sheet[1]
    # big health bar for final cutscene --------------------------------------------------------------------------------
    hp_big_url = resource_path('resources/art/overlay_health_large.png')
    hp_big_sheet = sprite_sheet((606, 33), hp_big_url)
    loaded_dict["big_hp_1"] = hp_big_sheet[0]
    loaded_dict["big_hp_2"] = hp_big_sheet[1]
    loaded_dict["big_hp_3"] = hp_big_sheet[2]
    loaded_dict["big_hp_4"] = hp_big_sheet[3]
    loaded_dict["big_hp_5"] = hp_big_sheet[4]
    loaded_dict["big_hp_6"] = hp_big_sheet[5]
    loaded_dict["big_hp_7"] = hp_big_sheet[6]
    loaded_dict["big_hp_8"] = hp_big_sheet[7]
    loaded_dict["big_hp_9"] = hp_big_sheet[8]
    loaded_dict["big_hp_10"] = hp_big_sheet[9]
    loaded_dict["big_hp_11"] = hp_big_sheet[10]
    loaded_dict["big_hp_12"] = hp_big_sheet[11]
    loaded_dict["big_hp_13"] = hp_big_sheet[12]
    loaded_dict["big_hp_14"] = hp_big_sheet[13]
    loaded_dict["big_hp_15"] = hp_big_sheet[14]
    loaded_dict["big_hp_16"] = hp_big_sheet[15]
    loaded_dict["big_hp_17"] = hp_big_sheet[16]
    loaded_dict["big_hp_18"] = hp_big_sheet[17]
    loaded_dict["big_hp_19"] = hp_big_sheet[18]
    loaded_dict["big_hp_20"] = hp_big_sheet[19]
    loaded_dict["big_hp_21"] = hp_big_sheet[20]
    loaded_dict["big_hp_22"] = hp_big_sheet[21]
    loaded_dict["big_hp_23"] = hp_big_sheet[22]
    loaded_dict["big_hp_24"] = hp_big_sheet[23]
    loaded_dict["big_hp_25"] = hp_big_sheet[24]

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
