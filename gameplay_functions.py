import os
import random
import pickle
import time
from pygame.locals import *

import drawing_functions


def check_interaction(pygame, player, interactables_nascent, interactables_seldon, interactables_stardust,
                      fishing_spot_stardust_1, fishing_spot_stardust_2, dungeon_entrance, dungeon_items,
                      mini_boss_1, chorizon_1, mini_boss_2, chorizon_2, switch_3, dungeon_teleporter,
                      interactables_reservoir_b, interactables_reservoir_c, interactables_korlok, forge_entrance,
                      interactables_mines, interactables_terra_trail, eldream_gate_rect, fishing_hut_rect,
                      fishing_spot_korlok_1, fishing_spot_korlok_2, interactables_eldream, ectrenos_entrance_rect,
                      ectrenos_ladder_rect, npc_leyre, ectrenos_inn_entrance, ectrenos_shop_entrance,
                      ectrenos_pet_entrance, altar_entrance, npc_everett, ectrenos_front_enemies,
                      alcove_ladder_rect, ghouls_marrow, npc_artherian, marrow_hearth, npc_maydria, npc_noren,
                      npc_boro, sub_marrow_rect, interactables_marrow_entrance, marrow_switch_box, ramps_crate_1,
                      ramps_crate_2, ramps_crate_3, ramps_crate_4, overlay_marrow_ramps_west, overlay_marrow_ramps_east,
                      dungeon_chest_ramps, dungeon_switch_ramps_2, erebyth, dungeon_switch_ramps_1, ramps_crate_5,
                      forge_rect, interacted, event, ectrenos_alcove_enemies, alcove_fishing_rect,
                      alcove_fishing_rect_2, fishing_spot_eldream_1, fishing_spot_eldream_2, sub_marrow_rect_2,
                      dungeon_gate_marrow, dungeon_chest_marrow_small, atmons, castle_exit, castle_crate_1,
                      castle_crate_2, rock_9, rock_10, rope_wind_1, cell_1, cell_2, rope_wind_2, cell_3, castle_ladder,
                      castle_key, boss_door, caldera_ladder, fishing_spot_caldera, jumanos, lair_exit, dreth, cat,
                      marrow_barrier_small, seldon_barrier_small, card_cave, item_block_1, item_block_2,
                      item_block_3, item_block_4, item_block_5, item_block_6, item_block_7, item_block_8,
                      item_block_9, item_block_10, item_block_11, item_block_12, illisare, roroc, part_1, part_2,
                      part_3, part_4, ramparts_rocks):
    if event:
        if player.current_zone == "nascent":
            if pygame.sprite.spritecollideany(player, interactables_nascent):
                interacted = True
            else:
                interacted = False
        if player.current_zone == "seldon":
            if pygame.sprite.spritecollideany(player, interactables_seldon):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, seldon_barrier_small):
                interacted = True
            else:
                interacted = False
        if player.current_zone == "stardust":
            if pygame.sprite.spritecollideany(player, interactables_stardust):
                interacted = True
            elif pygame.sprite.collide_rect(player, fishing_spot_stardust_1):
                interacted = True
            elif pygame.sprite.collide_rect(player, fishing_spot_stardust_2):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, card_cave):
                interacted = True
            else:
                interacted = False
        if player.current_zone == "rohir":
            if pygame.sprite.collide_rect(player, dungeon_entrance):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, item_block_1):
                interacted = True
            else:
                interacted = False
        if player.current_zone == "reservoir a":
            if pygame.sprite.spritecollideany(player, dungeon_items):
                interacted = True
            elif mini_boss_1:
                if pygame.sprite.collide_rect(player, chorizon_1):
                    interacted = True
            elif mini_boss_2:
                if pygame.sprite.collide_rect(player, chorizon_2):
                    interacted = True
            elif switch_3:
                if pygame.sprite.collide_rect(player, dungeon_teleporter):
                    interacted = True
            else:
                interacted = False
        if player.current_zone == "reservoir b":
            if pygame.sprite.spritecollideany(player, interactables_reservoir_b):
                interacted = True
            else:
                interacted = False
        if player.current_zone == "reservoir c":
            if pygame.sprite.spritecollideany(player, interactables_reservoir_c):
                interacted = True
            else:
                interacted = False
        if player.current_zone == "korlok":
            if pygame.sprite.spritecollideany(player, interactables_korlok):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, forge_entrance):
                interacted = True
            else:
                interacted = False
        if player.current_zone == "mines":
            if pygame.sprite.spritecollideany(player, interactables_mines):
                interacted = True
            else:
                interacted = False
        if player.current_zone == "terra trail":
            if pygame.sprite.spritecollideany(player, interactables_terra_trail):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, eldream_gate_rect):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, item_block_3):
                interacted = True
            else:
                interacted = False
        if player.current_zone == "fishing hut":
            if pygame.Rect.colliderect(player.rect, fishing_hut_rect):
                interacted = True
            elif pygame.sprite.collide_rect(player, fishing_spot_korlok_1):
                interacted = True
            elif pygame.sprite.collide_rect(player, fishing_spot_korlok_2):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, item_block_2):
                interacted = True
            else:
                interacted = False
        if player.current_zone == "eldream":
            if pygame.sprite.spritecollideany(player, interactables_eldream):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, ectrenos_entrance_rect):
                interacted = True
            else:
                interacted = False
        if player.current_zone == "ectrenos":
            if pygame.Rect.colliderect(player.rect, ectrenos_ladder_rect):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, npc_leyre.rect):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, illisare.rect):
                interacted = True
            else:
                interacted = False
        if player.current_zone == "ectrenos right":
            if pygame.Rect.colliderect(player.rect, ectrenos_inn_entrance):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, ectrenos_shop_entrance):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, npc_leyre.rect):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, item_block_4):
                interacted = True
            else:
                interacted = False
        if player.current_zone == "ectrenos left":
            if pygame.Rect.colliderect(player.rect, ectrenos_pet_entrance):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, npc_leyre.rect):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, altar_entrance):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, item_block_5):
                interacted = True
            else:
                interacted = False
        if player.current_zone == "ectrenos front":
            if pygame.Rect.colliderect(player.rect, npc_everett.rect):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, npc_leyre.rect):
                interacted = True
            elif pygame.sprite.spritecollideany(player, ectrenos_front_enemies):
                interacted = True
            else:
                interacted = False
        if player.current_zone == "ectrenos alcove":
            if pygame.Rect.colliderect(player.rect, alcove_ladder_rect):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, npc_leyre.rect):
                interacted = True
            elif pygame.sprite.spritecollideany(player, ectrenos_alcove_enemies):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, alcove_fishing_rect):
                interacted = True
            else:
                interacted = False
        if player.current_zone == "fishing alcove":
            if pygame.Rect.colliderect(player.rect, alcove_fishing_rect_2):
                interacted = True
            elif pygame.sprite.collide_rect(player, fishing_spot_eldream_1):
                interacted = True
            elif pygame.sprite.collide_rect(player, fishing_spot_eldream_2):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, item_block_6):
                interacted = True
            else:
                interacted = False
        if player.current_zone == "marrow":
            if pygame.sprite.spritecollideany(player, ghouls_marrow):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, npc_artherian.rect):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, marrow_hearth.rect):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, npc_maydria.rect):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, npc_noren.rect):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, npc_boro.rect):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, sub_marrow_rect):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, marrow_barrier_small):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, roroc.rect):
                interacted = True
            else:
                interacted = False
        if player.current_zone == "sub marrow":
            if pygame.Rect.colliderect(player.rect, sub_marrow_rect_2):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, dungeon_gate_marrow):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, dungeon_chest_marrow_small):
                interacted = True
            elif pygame.sprite.spritecollideany(player, atmons):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, item_block_9):
                interacted = True
            else:
                interacted = False
        if player.current_zone == "marrow entrance":
            if pygame.sprite.spritecollideany(player, interactables_marrow_entrance):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, marrow_switch_box):
                interacted = True
            else:
                interacted = False
        if player.current_zone == "marrow tower west":
            if pygame.Rect.colliderect(player.rect, ramps_crate_1):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, ramps_crate_2):
                interacted = True
            else:
                interacted = False
        if player.current_zone == "marrow tower east":
            if pygame.Rect.colliderect(player.rect, ramps_crate_3):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, ramps_crate_4):
                interacted = True
            else:
                interacted = False
        if player.current_zone == "marrow ramps west":
            if pygame.Rect.colliderect(player.rect, overlay_marrow_ramps_west):
                interacted = True
            else:
                interacted = False
        if player.current_zone == "marrow ramps east":
            if pygame.Rect.colliderect(player.rect, overlay_marrow_ramps_east):
                interacted = True
            else:
                interacted = False
        if player.current_zone == "marrow ramps east end":
            if pygame.Rect.colliderect(player.rect, dungeon_chest_ramps):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, dungeon_switch_ramps_2):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, erebyth):
                interacted = True
            else:
                interacted = False
        if player.current_zone == "marrow ramps west end":
            if pygame.Rect.colliderect(player.rect, dungeon_switch_ramps_1):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, ramps_crate_5):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, item_block_7):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, item_block_8):
                interacted = True
            elif pygame.sprite.spritecollideany(player, ramparts_rocks):
                interacted = True
            else:
                interacted = False
        if player.current_zone == "forge":
            if pygame.Rect.colliderect(player.rect, forge_rect):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, item_block_11):
                interacted = True
            else:
                interacted = False
        if player.current_zone == "altar":
            if pygame.Rect.colliderect(player.rect, forge_rect):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, item_block_12):
                interacted = True
            else:
                interacted = False
        if player.current_zone == "castle one":
            if pygame.Rect.colliderect(player.rect, castle_exit):
                interacted = True
            elif pygame.sprite.spritecollideany(player, jumanos):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, castle_crate_1):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, castle_crate_2):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, castle_key):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, boss_door):
                interacted = True
            else:
                interacted = False
        if player.current_zone == "castle two":
            if pygame.Rect.colliderect(player.rect, rock_9):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, rock_10):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, rope_wind_1):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, cell_1):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, cell_2):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, part_1):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, part_2):
                interacted = True
            else:
                interacted = False
        if player.current_zone == "castle three":
            if pygame.Rect.colliderect(player.rect, rope_wind_2):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, cell_3):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, castle_ladder):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, part_3):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, part_4):
                interacted = True
            else:
                interacted = False
        if player.current_zone == "castle lair":
            if pygame.Rect.colliderect(player.rect, lair_exit):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, dreth):
                interacted = True
            else:
                interacted = False
        if player.current_zone == "caldera":
            if pygame.Rect.colliderect(player.rect, caldera_ladder):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, fishing_spot_caldera):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, cat):
                interacted = True
            elif pygame.Rect.colliderect(player.rect, item_block_10):
                interacted = True
            else:
                interacted = False

    # checks if player is colliding with relevant objects outside the interaction event loop
    # prevents interaction with subsequent objects if no action occurs with current object interaction
    if not event:
        if player.current_zone == "nascent":
            if not pygame.sprite.spritecollideany(player, interactables_nascent):
                interacted = False
        if player.current_zone == "seldon":
            if (not pygame.sprite.spritecollideany(player, interactables_seldon) and
                    not pygame.Rect.colliderect(player.rect, seldon_barrier_small)):
                interacted = False
        if player.current_zone == "stardust":
            if (not pygame.sprite.spritecollideany(player, interactables_stardust) and
                    not pygame.sprite.collide_rect(player, fishing_spot_stardust_1) and
                    not pygame.sprite.collide_rect(player, fishing_spot_stardust_2) and
                    not pygame.Rect.colliderect(player.rect, card_cave)):
                interacted = False

        if player.current_zone == "rohir":
            if (not pygame.sprite.collide_rect(player, dungeon_entrance) and
                    not pygame.Rect.colliderect(player.rect, item_block_1)):
                interacted = False
        if player.current_zone == "reservoir a":
            if not pygame.sprite.spritecollideany(player, dungeon_items):
                interacted = False
            elif mini_boss_1:
                if not pygame.sprite.collide_rect(player, chorizon_1):
                    interacted = False
            elif mini_boss_2:
                if not pygame.sprite.collide_rect(player, chorizon_2):
                    interacted = False
            elif switch_3:
                if not pygame.sprite.collide_rect(player, dungeon_teleporter):
                    interacted = False

        if player.current_zone == "reservoir b":
            if not pygame.sprite.spritecollideany(player, interactables_reservoir_b):
                interacted = False
        if player.current_zone == "reservoir c":
            if not pygame.sprite.spritecollideany(player, interactables_reservoir_c):
                interacted = False

        if player.current_zone == "korlok":
            if (not pygame.sprite.spritecollideany(player, interactables_korlok)
                    and not pygame.Rect.colliderect(player.rect, forge_entrance)):
                interacted = False
        if player.current_zone == "mines":
            if not pygame.sprite.spritecollideany(player, interactables_mines):
                interacted = False
        if player.current_zone == "terra trail":
            if (not pygame.sprite.spritecollideany(player, interactables_terra_trail)
                    and not pygame.Rect.colliderect(player.rect, eldream_gate_rect)
                    and not pygame.Rect.colliderect(player.rect, item_block_3)):
                interacted = False
        if player.current_zone == "fishing hut":
            if (not pygame.Rect.colliderect(player.rect, fishing_hut_rect)
                    and not pygame.sprite.collide_rect(player, fishing_spot_korlok_1)
                    and not pygame.sprite.collide_rect(player, fishing_spot_korlok_2)
                    and not pygame.Rect.colliderect(player.rect, item_block_2)):
                interacted = False
        if player.current_zone == "eldream":
            if (not pygame.sprite.spritecollideany(player, interactables_eldream)
                    and not pygame.Rect.colliderect(player.rect, ectrenos_entrance_rect)):
                interacted = False
        if player.current_zone == "ectrenos":
            if (not pygame.Rect.colliderect(player.rect, ectrenos_ladder_rect)
                    and not pygame.Rect.colliderect(player.rect, npc_leyre.rect)
                    and not pygame.Rect.colliderect(player.rect, illisare.rect)):
                interacted = False
        if player.current_zone == "ectrenos right":
            if (not pygame.Rect.colliderect(player.rect, ectrenos_inn_entrance)
                    and not pygame.Rect.colliderect(player.rect, ectrenos_shop_entrance)
                    and not pygame.Rect.colliderect(player.rect, npc_leyre.rect)
                    and not pygame.Rect.colliderect(player.rect, item_block_4)):
                interacted = False
        if player.current_zone == "ectrenos left":
            if (not pygame.Rect.colliderect(player.rect, ectrenos_pet_entrance)
                    and not pygame.Rect.colliderect(player.rect, npc_leyre.rect)
                    and not pygame.Rect.colliderect(player.rect, altar_entrance)
                    and not pygame.Rect.colliderect(player.rect, item_block_5)):
                interacted = False
        if player.current_zone == "ectrenos front":
            if (not pygame.Rect.colliderect(player.rect, npc_everett.rect)
                    and not pygame.Rect.colliderect(player.rect, npc_leyre.rect)
                    and not pygame.sprite.spritecollideany(player, ectrenos_front_enemies)):
                interacted = False
        if player.current_zone == "ectrenos alcove":
            if (not pygame.Rect.colliderect(player.rect, alcove_ladder_rect)
                    and not pygame.Rect.colliderect(player.rect, npc_leyre.rect)
                    and not pygame.sprite.spritecollideany(player, ectrenos_alcove_enemies)
                    and not pygame.Rect.colliderect(player.rect, alcove_fishing_rect)):
                interacted = False
        if player.current_zone == "fishing alcove":
            if (not pygame.Rect.colliderect(player.rect, alcove_fishing_rect_2)
                    and not pygame.sprite.collide_rect(player, fishing_spot_eldream_1)
                    and not pygame.sprite.collide_rect(player, fishing_spot_eldream_2)
                    and not pygame.Rect.colliderect(player.rect, item_block_6)):
                interacted = False
        if player.current_zone == "marrow":
            if (not pygame.sprite.spritecollideany(player, ghouls_marrow)
                    and not pygame.Rect.colliderect(player.rect, npc_artherian.rect)
                    and not pygame.Rect.colliderect(player.rect, marrow_hearth.rect)
                    and not pygame.Rect.colliderect(player.rect, npc_maydria.rect)
                    and not pygame.Rect.colliderect(player.rect, npc_noren.rect)
                    and not pygame.Rect.colliderect(player.rect, npc_boro.rect)
                    and not pygame.Rect.colliderect(player.rect, sub_marrow_rect)
                    and not pygame.Rect.colliderect(player.rect, marrow_barrier_small)
                    and not pygame.Rect.colliderect(player.rect, roroc.rect)):
                interacted = False
        if player.current_zone == "sub marrow":
            if (not pygame.Rect.colliderect(player.rect, sub_marrow_rect)
                    and not pygame.Rect.colliderect(player.rect, dungeon_gate_marrow)
                    and not pygame.Rect.colliderect(player.rect, dungeon_chest_marrow_small)
                    and not pygame.sprite.spritecollideany(player, atmons)
                    and not pygame.Rect.colliderect(player.rect, item_block_9)):
                interacted = False
        if player.current_zone == "marrow entrance":
            if (not pygame.sprite.spritecollideany(player, interactables_marrow_entrance)
                    and not pygame.Rect.colliderect(player.rect, marrow_switch_box)):
                interacted = False
        if player.current_zone == "marrow tower west":
            if (not pygame.Rect.colliderect(player.rect, ramps_crate_1)
                    and not pygame.Rect.colliderect(player.rect, ramps_crate_2)):
                interacted = False
        if player.current_zone == "marrow tower east":
            if (not pygame.Rect.colliderect(player.rect, ramps_crate_3)
                    and not pygame.Rect.colliderect(player.rect, ramps_crate_4)):
                interacted = False
        if player.current_zone == "marrow ramps west":
            if not pygame.Rect.colliderect(player.rect, overlay_marrow_ramps_west):
                interacted = False
        if player.current_zone == "marrow ramps east":
            if not pygame.Rect.colliderect(player.rect, overlay_marrow_ramps_east):
                interacted = False
        if player.current_zone == "marrow ramps east end":
            if (not pygame.Rect.colliderect(player.rect, dungeon_chest_ramps)
                    and not pygame.Rect.colliderect(player.rect, dungeon_switch_ramps_2)
                    and not pygame.Rect.colliderect(player.rect, erebyth)):
                interacted = False
        if player.current_zone == "marrow ramps west end":
            if (not pygame.Rect.colliderect(player.rect, dungeon_switch_ramps_1)
                    and not pygame.Rect.colliderect(player.rect, ramps_crate_5)
                    and not pygame.Rect.colliderect(player.rect, item_block_7)
                    and not pygame.Rect.colliderect(player.rect, item_block_8)
                    and not pygame.sprite.spritecollideany(player, ramparts_rocks)):
                interacted = False
        if player.current_zone == "forge":
            if (not pygame.Rect.colliderect(player.rect, forge_rect) and
                    not pygame.Rect.colliderect(player.rect, item_block_11)):
                interacted = False
        if player.current_zone == "altar":
            if (not pygame.Rect.colliderect(player.rect, forge_rect) and
                    not pygame.Rect.colliderect(player.rect, item_block_12)):
                interacted = False
        if player.current_zone == "castle one":
            if (not pygame.Rect.colliderect(player.rect, castle_exit)
                    and not pygame.sprite.spritecollideany(player, jumanos)
                    and not pygame.Rect.colliderect(player.rect, castle_crate_1)
                    and not pygame.Rect.colliderect(player.rect, castle_crate_2)
                    and not pygame.Rect.colliderect(player.rect, castle_key)
                    and not pygame.Rect.colliderect(player.rect, boss_door)):
                interacted = False
        if player.current_zone == "castle two":
            if (not pygame.Rect.colliderect(player.rect, rock_9) and
                    not pygame.Rect.colliderect(player.rect, rock_10) and
                    not pygame.Rect.colliderect(player.rect, rope_wind_1) and
                    not pygame.Rect.colliderect(player.rect, cell_1) and
                    not pygame.Rect.colliderect(player.rect, cell_2) and
                    not pygame.Rect.colliderect(player.rect, part_1) and
                    not pygame.Rect.colliderect(player.rect, part_2)):
                interacted = False
        if player.current_zone == "castle three":
            if (not pygame.Rect.colliderect(player.rect, rope_wind_2) and
                    not pygame.Rect.colliderect(player.rect, cell_3) and
                    not pygame.Rect.colliderect(player.rect, castle_ladder) and
                    not pygame.Rect.colliderect(player.rect, part_3) and
                    not pygame.Rect.colliderect(player.rect, part_4)):
                interacted = False
        if player.current_zone == "castle lair":
            if (not pygame.Rect.colliderect(player.rect, lair_exit) and
                    not pygame.Rect.colliderect(player.rect, dreth)):
                interacted = False
        if player.current_zone == "caldera":
            if (not pygame.Rect.colliderect(player.rect, caldera_ladder) and
                    not pygame.Rect.colliderect(player.rect, fishing_spot_caldera) and
                    not pygame.Rect.colliderect(player.rect, cat) and
                    not pygame.Rect.colliderect(player.rect, item_block_10)):
                interacted = False

    return interacted


def fishing_function(pygame, fishing_timer, player, current_zone, spot_3_img, spot_4_img, spot_1_korlok, spot_2_korlok,
                     fishing_level, basic_fish_counter, better_fish_counter, even_better_fish_counter,
                     best_fish_counter, fishing, fish_caught, amuna_m_right, amuna_m_down, amuna_m_right_2,
                     amuna_m_down_2, amuna_m_right_3, amuna_m_down_3, amuna_f_right, amuna_f_down, amuna_f_right_2,
                     amuna_f_down_2, amuna_f_right_3, amuna_f_down_3, nuldar_m_right, nuldar_m_down, nuldar_m_right_2,
                     nuldar_m_down_2, nuldar_m_right_3, nuldar_m_down_3, nuldar_f_right, nuldar_f_down,
                     nuldar_f_right_2, nuldar_f_down_2, nuldar_f_right_3, nuldar_f_down_3, sorae_a_right, sorae_a_down,
                     sorae_a_right_2, sorae_a_down_2, sorae_a_right_3, sorae_a_down_3, sorae_b_right, sorae_b_down,
                     sorae_b_right_2, sorae_b_down_2, sorae_b_right_3, sorae_b_down_3, previous_surf, spot_1_stardust,
                     spot_2_stardust, spot_1_eldream, spot_2_eldream, sorae_a_up, sorae_b_up, sorae_a_up_2,
                     sorae_b_up_2, sorae_a_up_3, sorae_b_up_3, amuna_m_up, amuna_f_up, amuna_m_up_2, amuna_f_up_2,
                     amuna_m_up_3, amuna_f_up_3, nuldar_m_up, nuldar_f_up, nuldar_m_up_2, nuldar_f_up_2, nuldar_m_up_3,
                     nuldar_f_up_3, spot_caldera):

    fishing_timer_end = time.perf_counter()
    if fishing_timer_end - fishing_timer >= 2:

        player.surf = previous_surf
        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)

        if current_zone == "fishing hut":
            if pygame.sprite.collide_rect(player, spot_1_korlok):
                spot_1_korlok.update(740, 410, spot_4_img)
            if pygame.sprite.collide_rect(player, spot_2_korlok):
                spot_2_korlok.update(575, 525, spot_4_img)

        if current_zone == "stardust":
            if pygame.sprite.collide_rect(player, spot_1_stardust):
                spot_1_stardust.update(900, 490, spot_4_img)
            if pygame.sprite.collide_rect(player, spot_2_stardust):
                spot_2_stardust.update(450, 648, spot_4_img)

        if current_zone == "fishing alcove":
            if pygame.sprite.collide_rect(player, spot_1_eldream):
                spot_1_eldream.update(250, 335, spot_4_img)
            if pygame.sprite.collide_rect(player, spot_2_eldream):
                spot_2_eldream.update(645, 335, spot_4_img)

        if current_zone == "caldera":
            if pygame.sprite.collide_rect(player, spot_caldera):
                spot_caldera.update(710, 365, spot_4_img)

        catch_chance = random.randrange(1, 10)
        if fishing_level == 1 or fishing_level == 1.5:
            if catch_chance > 3:
                if current_zone == "fishing hut":
                    basic_fish_counter += 1
                if current_zone == "stardust":
                    better_fish_counter += 1
                if current_zone == "fishing alcove":
                    even_better_fish_counter += 1
                if current_zone == "caldera":
                    best_fish_counter += 1
                fish_caught = True
            else:
                fish_caught = False
        if fishing_level == 2.0 or fishing_level == 2.5:
            if catch_chance > 2:
                if current_zone == "fishing hut":
                    basic_fish_counter += 1
                if current_zone == "stardust":
                    better_fish_counter += 1
                if current_zone == "fishing alcove":
                    even_better_fish_counter += 1
                if current_zone == "caldera":
                    best_fish_counter += 1
                fish_caught = True
            else:
                fish_caught = False
        if fishing_level == 3.0 or fishing_level == 3.5:
            if catch_chance > 1:
                if current_zone == "fishing hut":
                    basic_fish_counter += 1
                if current_zone == "stardust":
                    better_fish_counter += 1
                if current_zone == "fishing alcove":
                    even_better_fish_counter += 1
                if current_zone == "caldera":
                    best_fish_counter += 1
                fish_caught = True
            else:
                fish_caught = False
        fishing = False
        movement_able = True

    # shows if player is actively engaged with a fishing spot if they're near it while fishing
    else:
        movement_able = False
        if current_zone == "fishing hut":
            if pygame.sprite.collide_rect(player, spot_1_korlok):
                spot_1_korlok.update(740, 410, spot_3_img)
                if player.race == "amuna":
                    if player.gender == "male":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = amuna_m_right
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = amuna_m_right_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = amuna_m_right_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)
                    if player.gender == "female":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = amuna_f_right
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = amuna_f_right_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = amuna_f_right_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)
                if player.race == "nuldar":
                    if player.gender == "male":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = nuldar_m_right
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = nuldar_m_right_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = nuldar_m_right_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)
                    if player.gender == "female":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = nuldar_f_right
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = nuldar_f_right_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = nuldar_f_right_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)
                if player.race == "sorae":
                    if player.gender == "male":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = sorae_a_right
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = sorae_a_right_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = sorae_a_right_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)
                    if player.gender == "female":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = sorae_b_right
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = sorae_b_right_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = sorae_b_right_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)
            if pygame.sprite.collide_rect(player, spot_2_korlok):
                spot_2_korlok.update(575, 525, spot_3_img)
                if player.race == "amuna":
                    if player.gender == "male":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = amuna_m_down
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = amuna_m_down_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = amuna_m_down_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)
                    if player.gender == "female":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = amuna_f_down
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = amuna_f_down_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = amuna_f_down_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)
                if player.race == "nuldar":
                    if player.gender == "male":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = nuldar_m_down
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = nuldar_m_down_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = nuldar_m_down_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)
                    if player.gender == "female":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = nuldar_f_down
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = nuldar_f_down_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = nuldar_f_down_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)
                if player.race == "sorae":
                    if player.gender == "male":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = sorae_a_down
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = sorae_a_down_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = sorae_a_down_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)
                    if player.gender == "female":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = sorae_b_down
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = sorae_b_down_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = sorae_b_down_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)

        if current_zone == "stardust":
            if pygame.sprite.collide_rect(player, spot_1_stardust):
                spot_1_stardust.update(900, 490, spot_3_img)
                if player.race == "amuna":
                    if player.gender == "male":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = amuna_m_right
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = amuna_m_right_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = amuna_m_right_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)
                    if player.gender == "female":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = amuna_f_right
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = amuna_f_right_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = amuna_f_right_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)
                if player.race == "nuldar":
                    if player.gender == "male":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = nuldar_m_right
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = nuldar_m_right_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = nuldar_m_right_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)
                    if player.gender == "female":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = nuldar_f_right
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = nuldar_f_right_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = nuldar_f_right_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)
                if player.race == "sorae":
                    if player.gender == "male":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = sorae_a_right
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = sorae_a_right_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = sorae_a_right_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)
                    if player.gender == "female":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = sorae_b_right
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = sorae_b_right_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = sorae_b_right_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)
            if pygame.sprite.collide_rect(player, spot_2_stardust):
                spot_2_stardust.update(450, 648, spot_3_img)
                if player.race == "amuna":
                    if player.gender == "male":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = amuna_m_down
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = amuna_m_down_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = amuna_m_down_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)
                    if player.gender == "female":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = amuna_f_down
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = amuna_f_down_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = amuna_f_down_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)
                if player.race == "nuldar":
                    if player.gender == "male":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = nuldar_m_down
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = nuldar_m_down_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = nuldar_m_down_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)
                    if player.gender == "female":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = nuldar_f_down
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = nuldar_f_down_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = nuldar_f_down_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)
                if player.race == "sorae":
                    if player.gender == "male":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = sorae_a_down
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = sorae_a_down_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = sorae_a_down_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)
                    if player.gender == "female":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = sorae_b_down
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = sorae_b_down_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = sorae_b_down_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)

        if current_zone == "fishing alcove":
            if pygame.sprite.collide_rect(player, spot_1_eldream):
                spot_1_eldream.update(250, 335, spot_3_img)
                if player.race == "amuna":
                    if player.gender == "male":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = amuna_m_up
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = amuna_m_up_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = amuna_m_up_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)
                    if player.gender == "female":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = amuna_f_up
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = amuna_f_up_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = amuna_f_up_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)
                if player.race == "nuldar":
                    if player.gender == "male":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = nuldar_m_up
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = nuldar_m_up_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = nuldar_m_up_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)
                    if player.gender == "female":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = nuldar_f_up
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = nuldar_f_up_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = nuldar_f_up_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)
                if player.race == "sorae":
                    if player.gender == "male":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = sorae_a_up
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = sorae_a_up_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = sorae_a_up_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)
                    if player.gender == "female":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = sorae_b_up
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = sorae_b_up_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = sorae_b_up_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)
            if pygame.sprite.collide_rect(player, spot_2_eldream):
                spot_2_eldream.update(645, 335, spot_3_img)
                if player.race == "amuna":
                    if player.gender == "male":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = amuna_m_up
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = amuna_m_up_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = amuna_m_up_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)
                    if player.gender == "female":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = amuna_f_up
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = amuna_f_up_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = amuna_f_up_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)
                if player.race == "nuldar":
                    if player.gender == "male":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = nuldar_m_up
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = nuldar_m_up_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = nuldar_m_up_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)
                    if player.gender == "female":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = nuldar_f_up
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = nuldar_f_up_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = nuldar_f_up_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)
                if player.race == "sorae":
                    if player.gender == "male":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = sorae_a_up
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = sorae_a_up_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = sorae_a_up_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)
                    if player.gender == "female":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = sorae_b_up
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = sorae_b_up_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = sorae_b_up_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)

        if current_zone == "caldera":
            if pygame.sprite.collide_rect(player, spot_caldera):
                spot_caldera.update(710, 365, spot_3_img)
                if player.race == "amuna":
                    if player.gender == "male":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = amuna_m_right
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = amuna_m_right_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = amuna_m_right_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)
                    if player.gender == "female":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = amuna_f_right
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = amuna_f_right_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = amuna_f_right_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)
                if player.race == "nuldar":
                    if player.gender == "male":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = nuldar_m_right
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = nuldar_m_right_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = nuldar_m_right_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)
                    if player.gender == "female":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = nuldar_f_right
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = nuldar_f_right_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = nuldar_f_right_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)
                if player.race == "sorae":
                    if player.gender == "male":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = sorae_a_right
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = sorae_a_right_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = sorae_a_right_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)
                    if player.gender == "female":
                        if fishing_level == 1 or fishing_level == 1.5:
                            player.surf = sorae_b_right
                        if fishing_level == 2.0 or fishing_level == 2.5:
                            player.surf = sorae_b_right_2
                        if fishing_level == 3.0 or fishing_level == 3.5:
                            player.surf = sorae_b_right_3
                        player.rect.midbottom = (player.x_coordinate, player.y_coordinate)

    fishing_return = {"basic_fish_counter": basic_fish_counter, "better_fish_counter": better_fish_counter,
                      "even_better_fish_counter": even_better_fish_counter, "best_fish_counter": best_fish_counter,
                      "fish_caught": fish_caught, "fishing": fishing, "movement_able": movement_able}

    return fishing_return


def pet_call(pygame, player, kasper_called, torok_called, iriana_called, sfx_whistle, width, height):
    if kasper_called:
        pygame.mixer.find_channel(True).play(sfx_whistle)
        for pet in player.pet:
            if pet.name == "kasper":
                match pet.active:
                    case True:
                        pet.active = False
                    case False:
                        pet.active = True
                        pet.update(player.x_coordinate + 25, player.y_coordinate - 25, width, height,
                                   player.current_zone)
            # set other pets to de-active, so they don't overlap
            else:
                match pet.active:
                    case True:
                        pet.active = False
    if torok_called:
        pygame.mixer.find_channel(True).play(sfx_whistle)
        for pet in player.pet:
            if pet.name == "torok":
                match pet.active:
                    case True:
                        pet.active = False
                    case False:
                        pet.active = True
                        pet.update(player.x_coordinate + 25, player.y_coordinate - 25, width, height,
                                   player.current_zone)
            else:
                match pet.active:
                    case True:
                        pet.active = False
    if iriana_called:
        pygame.mixer.find_channel(True).play(sfx_whistle)
        for pet in player.pet:
            if pet.name == "iriana":
                match pet.active:
                    case True:
                        pet.active = False
                    case False:
                        pet.active = True
                        pet.update(player.x_coordinate + 25, player.y_coordinate - 25, width, height,
                                   player.current_zone)
            else:
                match pet.active:
                    case True:
                        pet.active = False


def role_swap(pygame, player, pos, graphic_dict, staff, sword, bow, pressed_keys, sfx_swap):
    if len(drawing_functions.item_info_window) == 0 and len(drawing_functions.sell_info_window) == 0:

        if staff.rect.collidepoint(pos):
            pygame.mixer.Sound.play(sfx_swap)
            player.role = "mage"
            if player.race == "amuna":
                try:
                    if player.equipment["armor"].name == "basic armor":
                        if player.gender == "male":
                            player.surf = graphic_dict["player_mage_amuna_male_down_1_basic"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_mage_amuna_male_right_1_basic"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_mage_amuna_male_left_1_basic"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_mage_amuna_male_up_1_basic"]
                        if player.gender == "female":
                            player.surf = graphic_dict["player_mage_amuna_female_down_1_basic"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_mage_amuna_female_right_1_basic"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_mage_amuna_female_left_1_basic"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_mage_amuna_female_up_1_basic"]
                    if player.equipment["armor"].name == "forged armor":
                        if player.gender == "male":
                            player.surf = graphic_dict["player_mage_amuna_male_down_1_forged"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_mage_amuna_male_right_1_forged"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_mage_amuna_male_left_1_forged"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_mage_amuna_male_up_1_forged"]
                        if player.gender == "female":
                            player.surf = graphic_dict["player_mage_amuna_female_down_1_forged"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_mage_amuna_female_right_1_forged"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_mage_amuna_female_left_1_forged"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_mage_amuna_female_up_1_forged"]
                    if player.equipment["armor"].name == "mythical armor":
                        if player.gender == "male":
                            player.surf = graphic_dict["player_mage_amuna_male_down_1_mythic"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_mage_amuna_male_right_1_mythic"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_mage_amuna_male_left_1_mythic"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_mage_amuna_male_up_1_mythic"]
                        if player.gender == "female":
                            player.surf = graphic_dict["player_mage_amuna_female_down_1_mythic"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_mage_amuna_female_right_1_mythic"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_mage_amuna_female_left_1_mythic"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_mage_amuna_female_up_1_mythic"]
                    if player.equipment["armor"].name == "legendary armor":
                        if player.gender == "male":
                            player.surf = graphic_dict["player_mage_amuna_male_down_1_legend"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_mage_amuna_male_right_1_legend"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_mage_amuna_male_left_1_legend"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_mage_amuna_male_up_1_legend"]
                        if player.gender == "female":
                            player.surf = graphic_dict["player_mage_amuna_female_down_1_legend"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_mage_amuna_female_right_1_legend"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_mage_amuna_female_left_1_legend"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_mage_amuna_female_up_1_legend"]
                except AttributeError:
                    if player.gender == "male":
                        player.surf = graphic_dict["player_mage_amuna_male_down_1"]
                        if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                            player.surf = graphic_dict["player_mage_amuna_male_right_1"]
                        if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                            player.surf = graphic_dict["player_mage_amuna_male_left_1"]
                        if pressed_keys[K_w] or pressed_keys[K_UP]:
                            player.surf = graphic_dict["player_mage_amuna_male_up_1"]
                    if player.gender == "female":
                        player.surf = graphic_dict["player_mage_amuna_female_down_1"]
                        if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                            player.surf = graphic_dict["player_mage_amuna_female_right_1"]
                        if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                            player.surf = graphic_dict["player_mage_amuna_female_left_1"]
                        if pressed_keys[K_w] or pressed_keys[K_UP]:
                            player.surf = graphic_dict["player_mage_amuna_female_up_1"]
            if player.race == "nuldar":
                try:
                    if player.equipment["armor"].name == "basic armor":
                        if player.gender == "male":
                            player.surf = graphic_dict["player_mage_nuldar_male_down_1_basic"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_mage_nuldar_male_right_1_basic"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_mage_nuldar_male_left_1_basic"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_mage_nuldar_male_up_1_basic"]
                        if player.gender == "female":
                            player.surf = graphic_dict["player_mage_nuldar_female_down_1_basic"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_mage_nuldar_female_right_1_basic"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_mage_nuldar_female_left_1_basic"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_mage_nuldar_female_up_1_basic"]
                    if player.equipment["armor"].name == "forged armor":
                        if player.gender == "male":
                            player.surf = graphic_dict["player_mage_nuldar_male_down_1_forged"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_mage_nuldar_male_right_1_forged"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_mage_nuldar_male_left_1_forged"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_mage_nuldar_male_up_1_forged"]
                        if player.gender == "female":
                            player.surf = graphic_dict["player_mage_nuldar_female_down_1_forged"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_mage_nuldar_female_right_1_forged"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_mage_nuldar_female_left_1_forged"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_mage_nuldar_female_up_1_forged"]
                    if player.equipment["armor"].name == "mythical armor":
                        if player.gender == "male":
                            player.surf = graphic_dict["player_mage_nuldar_male_down_1_mythic"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_mage_nuldar_male_right_1_mythic"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_mage_nuldar_male_left_1_mythic"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_mage_nuldar_male_up_1_mythic"]
                        if player.gender == "female":
                            player.surf = graphic_dict["player_mage_nuldar_female_down_1_mythic"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_mage_nuldar_female_right_1_mythic"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_mage_nuldar_female_left_1_mythic"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_mage_nuldar_female_up_1_mythic"]
                    if player.equipment["armor"].name == "legendary armor":
                        if player.gender == "male":
                            player.surf = graphic_dict["player_mage_nuldar_male_down_1_legend"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_mage_nuldar_male_right_1_legend"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_mage_nuldar_male_left_1_legend"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_mage_nuldar_male_up_1_legend"]
                        if player.gender == "female":
                            player.surf = graphic_dict["player_mage_nuldar_female_down_1_legend"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_mage_nuldar_female_right_1_legend"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_mage_nuldar_female_left_1_legend"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_mage_nuldar_female_up_1_legend"]
                except AttributeError:
                    if player.gender == "male":
                        player.surf = graphic_dict["player_mage_nuldar_male_down_1"]
                        if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                            player.surf = graphic_dict["player_mage_nuldar_male_right_1"]
                        if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                            player.surf = graphic_dict["player_mage_nuldar_male_left_1"]
                        if pressed_keys[K_w] or pressed_keys[K_UP]:
                            player.surf = graphic_dict["player_mage_nuldar_male_up_1"]
                    if player.gender == "female":
                        player.surf = graphic_dict["player_mage_nuldar_female_down_1"]
                        if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                            player.surf = graphic_dict["player_mage_nuldar_female_right_1"]
                        if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                            player.surf = graphic_dict["player_mage_nuldar_female_left_1"]
                        if pressed_keys[K_w] or pressed_keys[K_UP]:
                            player.surf = graphic_dict["player_mage_nuldar_female_up_1"]
            if player.race == "sorae":
                try:
                    if player.equipment["armor"].name == "basic armor":
                        if player.gender == "male":
                            player.surf = graphic_dict["player_mage_sorae_a_down_1_basic"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_mage_sorae_a_right_1_basic"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_mage_sorae_a_left_1_basic"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_mage_sorae_a_up_1_basic"]
                        if player.gender == "female":
                            player.surf = graphic_dict["player_mage_sorae_b_down_1_basic"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_mage_sorae_b_right_1_basic"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_mage_sorae_b_left_1_basic"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_mage_sorae_b_up_1_basic"]
                    if player.equipment["armor"].name == "forged armor":
                        if player.gender == "male":
                            player.surf = graphic_dict["player_mage_sorae_a_down_1_forged"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_mage_sorae_a_right_1_forged"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_mage_sorae_a_left_1_forged"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_mage_sorae_a_up_1_forged"]
                        if player.gender == "female":
                            player.surf = graphic_dict["player_mage_sorae_b_down_1_forged"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_mage_sorae_b_right_1_forged"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_mage_sorae_b_left_1_forged"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_mage_sorae_b_up_1_forged"]
                    if player.equipment["armor"].name == "mythical armor":
                        if player.gender == "male":
                            player.surf = graphic_dict["player_mage_sorae_a_down_1_mythic"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_mage_sorae_a_right_1_mythic"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_mage_sorae_a_left_1_mythic"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_mage_sorae_a_up_1_mythic"]
                        if player.gender == "female":
                            player.surf = graphic_dict["player_mage_sorae_b_down_1_mythic"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_mage_sorae_b_right_1_mythic"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_mage_sorae_b_left_1_mythic"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_mage_sorae_b_up_1_mythic"]
                    if player.equipment["armor"].name == "legendary armor":
                        if player.gender == "male":
                            player.surf = graphic_dict["player_mage_sorae_a_down_1_legend"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_mage_sorae_a_right_1_legend"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_mage_sorae_a_left_1_legend"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_mage_sorae_a_up_1_legend"]
                        if player.gender == "female":
                            player.surf = graphic_dict["player_mage_sorae_b_down_1_legend"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_mage_sorae_b_right_1_legend"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_mage_sorae_b_left_1_legend"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_mage_sorae_b_up_1_legend"]
                except AttributeError:
                    if player.gender == "male":
                        player.surf = graphic_dict["player_mage_sorae_a_down_1"]
                        if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                            player.surf = graphic_dict["player_mage_sorae_a_right_1"]
                        if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                            player.surf = graphic_dict["player_mage_sorae_a_left_1"]
                        if pressed_keys[K_w] or pressed_keys[K_UP]:
                            player.surf = graphic_dict["player_mage_sorae_a_up_1"]
                    if player.gender == "female":
                        player.surf = graphic_dict["player_mage_sorae_b_down_1"]
                        if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                            player.surf = graphic_dict["player_mage_sorae_b_right_1"]
                        if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                            player.surf = graphic_dict["player_mage_sorae_b_left_1"]
                        if pressed_keys[K_w] or pressed_keys[K_UP]:
                            player.surf = graphic_dict["player_mage_sorae_b_up_1"]

        if sword.rect.collidepoint(pos):
            pygame.mixer.Sound.play(sfx_swap)
            player.role = "fighter"
            if player.race == "amuna":
                try:
                    if player.equipment["armor"].name == "basic armor":
                        if player.gender == "male":
                            player.surf = graphic_dict["player_fighter_amuna_male_down_1_basic"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_fighter_amuna_male_right_1_basic"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_fighter_amuna_male_left_1_basic"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_fighter_amuna_male_up_1_basic"]
                        if player.gender == "female":
                            player.surf = graphic_dict["player_fighter_amuna_female_down_1_basic"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_fighter_amuna_female_right_1_basic"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_fighter_amuna_female_left_1_basic"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_fighter_amuna_female_up_1_basic"]
                    if player.equipment["armor"].name == "forged armor":
                        if player.gender == "male":
                            player.surf = graphic_dict["player_fighter_amuna_male_down_1_forged"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_fighter_amuna_male_right_1_forged"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_fighter_amuna_male_left_1_forged"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_fighter_amuna_male_up_1_forged"]
                        if player.gender == "female":
                            player.surf = graphic_dict["player_fighter_amuna_female_down_1_forged"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_fighter_amuna_female_right_1_forged"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_fighter_amuna_female_left_1_forged"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_fighter_amuna_female_up_1_forged"]
                    if player.equipment["armor"].name == "mythical armor":
                        if player.gender == "male":
                            player.surf = graphic_dict["player_fighter_amuna_male_down_1_mythic"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_fighter_amuna_male_right_1_mythic"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_fighter_amuna_male_left_1_mythic"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_fighter_amuna_male_up_1_mythic"]
                        if player.gender == "female":
                            player.surf = graphic_dict["player_fighter_amuna_female_down_1_mythic"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_fighter_amuna_female_right_1_mythic"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_fighter_amuna_female_left_1_mythic"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_fighter_amuna_female_up_1_mythic"]
                    if player.equipment["armor"].name == "legend armor":
                        if player.gender == "male":
                            player.surf = graphic_dict["player_fighter_amuna_male_down_1_legend"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_fighter_amuna_male_right_1_legend"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_fighter_amuna_male_left_1_legend"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_fighter_amuna_male_up_1_legend"]
                        if player.gender == "female":
                            player.surf = graphic_dict["player_fighter_amuna_female_down_1_legend"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_fighter_amuna_female_right_1_legend"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_fighter_amuna_female_left_1_legend"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_fighter_amuna_female_up_1_legend"]
                except AttributeError:
                    if player.gender == "male":
                        player.surf = graphic_dict["player_fighter_amuna_male_down_1"]
                        if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                            player.surf = graphic_dict["player_fighter_amuna_male_right_1"]
                        if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                            player.surf = graphic_dict["player_fighter_amuna_male_left_1"]
                        if pressed_keys[K_w] or pressed_keys[K_UP]:
                            player.surf = graphic_dict["player_fighter_amuna_male_up_1"]
                    if player.gender == "female":
                        player.surf = graphic_dict["player_fighter_amuna_female_down_1"]
                        if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                            player.surf = graphic_dict["player_fighter_amuna_female_right_1"]
                        if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                            player.surf = graphic_dict["player_fighter_amuna_female_left_1"]
                        if pressed_keys[K_w] or pressed_keys[K_UP]:
                            player.surf = graphic_dict["player_fighter_amuna_female_up_1"]
            if player.race == "nuldar":
                try:
                    if player.equipment["armor"].name == "basic armor":
                        if player.gender == "male":
                            player.surf = graphic_dict["player_fighter_nuldar_male_down_1_basic"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_fighter_nuldar_male_right_1_basic"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_fighter_nuldar_male_left_1_basic"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_fighter_nuldar_male_up_1_basic"]
                        if player.gender == "female":
                            player.surf = graphic_dict["player_fighter_nuldar_female_down_1_basic"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_fighter_nuldar_female_right_1_basic"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_fighter_nuldar_female_left_1_basic"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_fighter_nuldar_female_up_1_basic"]
                    if player.equipment["armor"].name == "forged armor":
                        if player.gender == "male":
                            player.surf = graphic_dict["player_fighter_nuldar_male_down_1_forged"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_fighter_nuldar_male_right_1_forged"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_fighter_nuldar_male_left_1_forged"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_fighter_nuldar_male_up_1_forged"]
                        if player.gender == "female":
                            player.surf = graphic_dict["player_fighter_nuldar_female_down_1_forged"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_fighter_nuldar_female_right_1_forged"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_fighter_nuldar_female_left_1_forged"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_fighter_nuldar_female_up_1_forged"]
                    if player.equipment["armor"].name == "mythical armor":
                        if player.gender == "male":
                            player.surf = graphic_dict["player_fighter_nuldar_male_down_1_mythic"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_fighter_nuldar_male_right_1_mythic"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_fighter_nuldar_male_left_1_mythic"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_fighter_nuldar_male_up_1_mythic"]
                        if player.gender == "female":
                            player.surf = graphic_dict["player_fighter_nuldar_female_down_1_mythic"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_fighter_nuldar_female_right_1_mythic"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_fighter_nuldar_female_left_1_mythic"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_fighter_nuldar_female_up_1_mythic"]
                    if player.equipment["armor"].name == "legendary armor":
                        if player.gender == "male":
                            player.surf = graphic_dict["player_fighter_nuldar_male_down_1_legend"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_fighter_nuldar_male_right_1_legend"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_fighter_nuldar_male_left_1_legend"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_fighter_nuldar_male_up_1_legend"]
                        if player.gender == "female":
                            player.surf = graphic_dict["player_fighter_nuldar_female_down_1_legend"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_fighter_nuldar_female_right_1_legend"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_fighter_nuldar_female_left_1_legend"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_fighter_nuldar_female_up_1_legend"]
                except AttributeError:
                    if player.gender == "male":
                        player.surf = graphic_dict["player_fighter_nuldar_male_down_1"]
                        if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                            player.surf = graphic_dict["player_fighter_nuldar_male_right_1"]
                        if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                            player.surf = graphic_dict["player_fighter_nuldar_male_left_1"]
                        if pressed_keys[K_w] or pressed_keys[K_UP]:
                            player.surf = graphic_dict["player_fighter_nuldar_male_up_1"]
                    if player.gender == "female":
                        player.surf = graphic_dict["player_fighter_nuldar_female_down_1"]
                        if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                            player.surf = graphic_dict["player_fighter_nuldar_female_right_1"]
                        if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                            player.surf = graphic_dict["player_fighter_nuldar_female_left_1"]
                        if pressed_keys[K_w] or pressed_keys[K_UP]:
                            player.surf = graphic_dict["player_fighter_nuldar_female_up_1"]
            if player.race == "sorae":
                try:
                    if player.equipment["armor"].name == "basic armor":
                        if player.gender == "male":
                            player.surf = graphic_dict["player_fighter_sorae_a_down_1_basic"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_fighter_sorae_a_right_1_basic"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_fighter_sorae_a_left_1_basic"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_fighter_sorae_a_up_1_basic"]
                        if player.gender == "female":
                            player.surf = graphic_dict["player_fighter_sorae_b_down_1_basic"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_fighter_sorae_b_right_1_basic"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_fighter_sorae_b_left_1_basic"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_fighter_sorae_b_up_1_basic"]
                    if player.equipment["armor"].name == "forged armor":
                        if player.gender == "male":
                            player.surf = graphic_dict["player_fighter_sorae_a_down_1_forged"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_fighter_sorae_a_right_1_forged"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_fighter_sorae_a_left_1_forged"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_fighter_sorae_a_up_1_forged"]
                        if player.gender == "female":
                            player.surf = graphic_dict["player_fighter_sorae_b_down_1_forged"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_fighter_sorae_b_right_1_forged"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_fighter_sorae_b_left_1_forged"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_fighter_sorae_b_up_1_forged"]
                    if player.equipment["armor"].name == "mythical armor":
                        if player.gender == "male":
                            player.surf = graphic_dict["player_fighter_sorae_a_down_1_mythic"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_fighter_sorae_a_right_1_mythic"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_fighter_sorae_a_left_1_mythic"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_fighter_sorae_a_up_1_mythic"]
                        if player.gender == "female":
                            player.surf = graphic_dict["player_fighter_sorae_b_down_1_mythic"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_fighter_sorae_b_right_1_mythic"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_fighter_sorae_b_left_1_mythic"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_fighter_sorae_b_up_1_mythic"]
                    if player.equipment["armor"].name == "legendary armor":
                        if player.gender == "male":
                            player.surf = graphic_dict["player_fighter_sorae_a_down_1_legend"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_fighter_sorae_a_right_1_legend"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_fighter_sorae_a_left_1_legend"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_fighter_sorae_a_up_1_legend"]
                        if player.gender == "female":
                            player.surf = graphic_dict["player_fighter_sorae_b_down_1_legend"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_fighter_sorae_b_right_1_legend"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_fighter_sorae_b_left_1_legend"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_fighter_sorae_b_up_1_legend"]
                except AttributeError:
                    if player.gender == "male":
                        player.surf = graphic_dict["player_fighter_sorae_a_down_1"]
                        if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                            player.surf = graphic_dict["player_fighter_sorae_a_right_1"]
                        if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                            player.surf = graphic_dict["player_fighter_sorae_a_left_1"]
                        if pressed_keys[K_w] or pressed_keys[K_UP]:
                            player.surf = graphic_dict["player_fighter_sorae_a_up_1"]
                    if player.gender == "female":
                        player.surf = graphic_dict["player_fighter_sorae_b_down_1"]
                        if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                            player.surf = graphic_dict["player_fighter_sorae_b_right_1"]
                        if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                            player.surf = graphic_dict["player_fighter_sorae_b_left_1"]
                        if pressed_keys[K_w] or pressed_keys[K_UP]:
                            player.surf = graphic_dict["player_fighter_sorae_b_up_1"]

        if bow.rect.collidepoint(pos):
            pygame.mixer.Sound.play(sfx_swap)
            player.role = "scout"
            if player.race == "amuna":
                try:
                    if player.equipment["armor"].name == "basic armor":
                        if player.gender == "male":
                            player.surf = graphic_dict["player_scout_amuna_male_down_1_basic"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_scout_amuna_male_right_1_basic"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_scout_amuna_male_left_1_basic"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_scout_amuna_male_up_1_basic"]
                        if player.gender == "female":
                            player.surf = graphic_dict["player_scout_amuna_female_down_1_basic"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_scout_amuna_female_right_1_basic"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_scout_amuna_female_left_1_basic"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_scout_amuna_female_up_1_basic"]
                    if player.equipment["armor"].name == "forged armor":
                        if player.gender == "male":
                            player.surf = graphic_dict["player_scout_amuna_male_down_1_forged"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_scout_amuna_male_right_1_forged"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_scout_amuna_male_left_1_forged"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_scout_amuna_male_up_1_forged"]
                        if player.gender == "female":
                            player.surf = graphic_dict["player_scout_amuna_female_down_1_forged"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_scout_amuna_female_right_1_forged"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_scout_amuna_female_left_1_forged"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_scout_amuna_female_up_1_forged"]
                    if player.equipment["armor"].name == "mythical armor":
                        if player.gender == "male":
                            player.surf = graphic_dict["player_scout_amuna_male_down_1_mythic"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_scout_amuna_male_right_1_mythic"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_scout_amuna_male_left_1_mythic"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_scout_amuna_male_up_1_mythic"]
                        if player.gender == "female":
                            player.surf = graphic_dict["player_scout_amuna_female_down_1_mythic"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_scout_amuna_female_right_1_mythic"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_scout_amuna_female_left_1_mythic"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_scout_amuna_female_up_1_mythic"]
                    if player.equipment["armor"].name == "legendary armor":
                        if player.gender == "male":
                            player.surf = graphic_dict["player_scout_amuna_male_down_1_legend"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_scout_amuna_male_right_1_legend"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_scout_amuna_male_left_1_legend"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_scout_amuna_male_up_1_legend"]
                        if player.gender == "female":
                            player.surf = graphic_dict["player_scout_amuna_female_down_1_legend"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_scout_amuna_female_right_1_legend"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_scout_amuna_female_left_1_legend"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_scout_amuna_female_up_1_legend"]
                except AttributeError:
                    if player.gender == "male":
                        player.surf = graphic_dict["player_scout_amuna_male_down_1"]
                        if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                            player.surf = graphic_dict["player_scout_amuna_male_right_1"]
                        if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                            player.surf = graphic_dict["player_scout_amuna_male_left_1"]
                        if pressed_keys[K_w] or pressed_keys[K_UP]:
                            player.surf = graphic_dict["player_scout_amuna_male_up_1"]
                    if player.gender == "female":
                        player.surf = graphic_dict["player_scout_amuna_female_down_1"]
                        if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                            player.surf = graphic_dict["player_scout_amuna_female_right_1"]
                        if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                            player.surf = graphic_dict["player_scout_amuna_female_left_1"]
                        if pressed_keys[K_w] or pressed_keys[K_UP]:
                            player.surf = graphic_dict["player_scout_amuna_female_up_1"]
            if player.race == "nuldar":
                try:
                    if player.equipment["armor"].name == "basic armor":
                        if player.gender == "male":
                            player.surf = graphic_dict["player_scout_nuldar_male_down_1_basic"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_scout_nuldar_male_right_1_basic"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_scout_nuldar_male_left_1_basic"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_scout_nuldar_male_up_1_basic"]
                        if player.gender == "female":
                            player.surf = graphic_dict["player_scout_nuldar_female_down_1_basic"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_scout_nuldar_female_right_1_basic"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_scout_nuldar_female_left_1_basic"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_scout_nuldar_female_up_1_basic"]
                    if player.equipment["armor"].name == "forged armor":
                        if player.gender == "male":
                            player.surf = graphic_dict["player_scout_nuldar_male_down_1_forged"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_scout_nuldar_male_right_1_forged"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_scout_nuldar_male_left_1_forged"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_scout_nuldar_male_up_1_forged"]
                        if player.gender == "female":
                            player.surf = graphic_dict["player_scout_nuldar_female_down_1_forged"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_scout_nuldar_female_right_1_forged"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_scout_nuldar_female_left_1_forged"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_scout_nuldar_female_up_1_forged"]
                    if player.equipment["armor"].name == "mythical armor":
                        if player.gender == "male":
                            player.surf = graphic_dict["player_scout_nuldar_male_down_1_mythic"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_scout_nuldar_male_right_1_mythic"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_scout_nuldar_male_left_1_mythic"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_scout_nuldar_male_up_1_mythic"]
                        if player.gender == "female":
                            player.surf = graphic_dict["player_scout_nuldar_female_down_1_mythic"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_scout_nuldar_female_right_1_mythic"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_scout_nuldar_female_left_1_mythic"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_scout_nuldar_female_up_1_mythic"]
                    if player.equipment["armor"].name == "legendary armor":
                        if player.gender == "male":
                            player.surf = graphic_dict["player_scout_nuldar_male_down_1_legend"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_scout_nuldar_male_right_1_legend"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_scout_nuldar_male_left_1_legend"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_scout_nuldar_male_up_1_legend"]
                        if player.gender == "female":
                            player.surf = graphic_dict["player_scout_nuldar_female_down_1_legend"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_scout_nuldar_female_right_1_legend"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_scout_nuldar_female_left_1_legend"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_scout_nuldar_female_up_1_legend"]
                except AttributeError:
                    if player.gender == "male":
                        player.surf = graphic_dict["player_scout_nuldar_male_down_1"]
                        if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                            player.surf = graphic_dict["player_scout_nuldar_male_right_1"]
                        if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                            player.surf = graphic_dict["player_scout_nuldar_male_left_1"]
                        if pressed_keys[K_w] or pressed_keys[K_UP]:
                            player.surf = graphic_dict["player_scout_nuldar_male_up_1"]
                    if player.gender == "female":
                        player.surf = graphic_dict["player_scout_nuldar_female_down_1"]
                        if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                            player.surf = graphic_dict["player_scout_nuldar_female_right_1"]
                        if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                            player.surf = graphic_dict["player_scout_nuldar_female_left_1"]
                        if pressed_keys[K_w] or pressed_keys[K_UP]:
                            player.surf = graphic_dict["player_scout_nuldar_female_up_1"]
            if player.race == "sorae":
                try:
                    if player.equipment["armor"].name == "basic armor":
                        if player.gender == "male":
                            player.surf = graphic_dict["player_scout_sorae_a_down_1_basic"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_scout_sorae_a_right_1_basic"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_scout_sorae_a_left_1_basic"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_scout_sorae_a_up_1_basic"]
                        if player.gender == "female":
                            player.surf = graphic_dict["player_scout_sorae_b_down_1_basic"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_scout_sorae_b_right_1_basic"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_scout_sorae_b_left_1_basic"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_scout_sorae_b_up_1_basic"]
                    if player.equipment["armor"].name == "forged armor":
                        if player.gender == "male":
                            player.surf = graphic_dict["player_scout_sorae_a_down_1_forged"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_scout_sorae_a_right_1_forged"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_scout_sorae_a_left_1_forged"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_scout_sorae_a_up_1_forged"]
                        if player.gender == "female":
                            player.surf = graphic_dict["player_scout_sorae_b_down_1_forged"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_scout_sorae_b_right_1_forged"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_scout_sorae_b_left_1_forged"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_scout_sorae_b_up_1_forged"]
                    if player.equipment["armor"].name == "mythical armor":
                        if player.gender == "male":
                            player.surf = graphic_dict["player_scout_sorae_a_down_1_mythic"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_scout_sorae_a_right_1_mythic"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_scout_sorae_a_left_1_mythic"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_scout_sorae_a_up_1_mythic"]
                        if player.gender == "female":
                            player.surf = graphic_dict["player_scout_sorae_b_down_1_mythic"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_scout_sorae_b_right_1_mythic"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_scout_sorae_b_left_1_mythic"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_scout_sorae_b_up_1_mythic"]
                    if player.equipment["armor"].name == "legendary armor":
                        if player.gender == "male":
                            player.surf = graphic_dict["player_scout_sorae_a_down_1_legend"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_scout_sorae_a_right_1_legend"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_scout_sorae_a_left_1_legend"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_scout_sorae_a_up_1_legend"]
                        if player.gender == "female":
                            player.surf = graphic_dict["player_scout_sorae_b_down_1_legend"]
                            if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                                player.surf = graphic_dict["player_scout_sorae_b_right_1_legend"]
                            if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                                player.surf = graphic_dict["player_scout_sorae_b_left_1_legend"]
                            if pressed_keys[K_w] or pressed_keys[K_UP]:
                                player.surf = graphic_dict["player_scout_sorae_b_up_1_legend"]
                except AttributeError:
                    if player.gender == "male":
                        player.surf = graphic_dict["player_scout_sorae_a_down_1"]
                        if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                            player.surf = graphic_dict["player_scout_sorae_a_right_1"]
                        if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                            player.surf = graphic_dict["player_scout_sorae_a_left_1"]
                        if pressed_keys[K_w] or pressed_keys[K_UP]:
                            player.surf = graphic_dict["player_scout_sorae_a_up_1"]
                    if player.gender == "female":
                        player.surf = graphic_dict["player_scout_sorae_b_down_1"]
                        if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
                            player.surf = graphic_dict["player_scout_sorae_b_right_1"]
                        if pressed_keys[K_a] or pressed_keys[K_LEFT]:
                            player.surf = graphic_dict["player_scout_sorae_b_left_1"]
                        if pressed_keys[K_w] or pressed_keys[K_UP]:
                            player.surf = graphic_dict["player_scout_sorae_b_up_1"]


# quest stars for npcs that update based on player quest progress
def npc_quest_star_updates(player, star_garan, star_maurelle, star_celeste, star_torune, quest_start_star,
                           quest_progress_star, quest_complete_star, star_voruke, star_zerah,
                           star_dionte, star_omoku, star_leyre, star_everett, star_artherian,
                           artherian_progress_star, artherian_complete_star, artherian_2,
                           npc_maydria, star_maydria, maydria_progress_star, maydria_complete_star, npc_boro,
                           npc_noren, artherian_task_start, star_kuba, star_nahun, star_illisare,
                           maydria_start_star, star_roroc):

    if player.current_zone == "nascent":
        if player.quest_status["welcome to consona"] and not player.quest_complete["welcome to consona"]:
            star_kuba.update(624, 80, quest_progress_star)

    if player.current_zone == "seldon":
        if player.quest_progress["sneaky snakes"] == 4:
            star_garan.update(209, 390, quest_complete_star)
        elif player.quest_status["sneaky snakes"] and player.quest_progress["sneaky snakes"] != 4:
            star_garan.update(209, 390, quest_progress_star)
        if player.quest_progress["where's nede?"] == 1:
            star_celeste.update(760, 373, quest_complete_star)
        elif player.quest_status["where's nede?"] and player.quest_progress["where's nede?"] != 1:
            star_celeste.update(760, 373, quest_progress_star)
        if player.quest_progress["village repairs"] == 4:
            star_maurelle.update(744, 575, quest_complete_star)
        elif player.quest_status["village repairs"] and player.quest_progress["village repairs"] != 4:
            star_maurelle.update(744, 575, quest_progress_star)
        if player.quest_progress["ghouled again"] == 4:
            star_torune.update(430, 75, quest_complete_star)
        elif player.quest_status["ghouled again"] and player.quest_progress["ghouled again"] != 4:
            star_torune.update(430, 75, quest_progress_star)

    if player.current_zone == "korlok":
        if player.quest_progress["band hammer"] == 4:
            star_voruke.update(262, 385, quest_complete_star)
        elif player.quest_status["band hammer"] and player.quest_progress["band hammer"] != 4:
            star_voruke.update(262, 385, quest_progress_star)
        if player.quest_progress["elementary elementals"] == 4:
            star_zerah.update(651, 50, quest_complete_star)
        elif player.quest_status["elementary elementals"] and player.quest_progress["elementary elementals"] != 4:
            star_zerah.update(651, 50, quest_progress_star)
        if player.quest_progress["welcome to consona"] == 1 and not player.quest_complete["welcome to consona"]:
            star_nahun.update(791, 410, quest_complete_star)
        elif player.quest_complete["welcome to consona"] and not player.quest_status["disenchanted"]:
            star_nahun.update(791, 410, quest_start_star)
        elif player.quest_status["disenchanted"] and not player.quest_complete["disenchanted"]:
            star_nahun.update(791, 410, quest_progress_star)

    if player.current_zone == "terra trail":
        if player.quest_progress["it's dangerous to go alone"] == 1:
            star_dionte.update(585, 60, quest_complete_star)
        elif player.quest_status["it's dangerous to go alone"] and \
                player.quest_progress["it's dangerous to go alone"] != 1:
            star_dionte.update(585, 60, quest_progress_star)

    if player.current_zone == "eldream":
        if player.quest_progress["kart troubles"] == 4:
            star_omoku.update(460, 610, quest_complete_star)
        elif player.quest_status["kart troubles"] and player.quest_progress["kart troubles"] != 4:
            star_omoku.update(460, 610, quest_progress_star)
    if player.current_zone == "ectrenos":
        if player.quest_progress["las escondidas"] == 4:
            star_leyre.update(682, 375, quest_complete_star)
        elif player.quest_status["las escondidas"] and player.quest_progress["las escondidas"] != 4:
            star_leyre.update(682, 375, quest_progress_star)
        if player.quest_progress["disenchanted"] == 1 and not player.quest_complete["disenchanted"]:
            star_illisare.update(515, 60, quest_complete_star)
        elif player.quest_complete["disenchanted"] and not player.quest_status["madness in marrow"]:
            star_illisare.update(515, 60, quest_start_star)
        elif player.quest_status["madness in marrow"]:
            star_illisare.update(515, 60, quest_progress_star)
    if player.current_zone == "ectrenos front":
        if player.quest_progress["shades of fear"] == 4:
            star_everett.update(749, 278, quest_complete_star)
        elif player.quest_status["shades of fear"] and player.quest_progress["shades of fear"] != 4:
            star_everett.update(749, 278, quest_progress_star)

    if player.current_zone == "marrow":
        if artherian_task_start and not artherian_2:
            star_artherian.update(210, 400, artherian_progress_star)
        elif artherian_2:
            star_artherian.update(210, 400, artherian_complete_star)
        if player.quest_complete["madness in marrow"] and not npc_maydria.gift:
            star_maydria.update(825, 132, maydria_start_star)
        elif npc_maydria.gift and not npc_boro.quest_complete and not npc_noren.quest_complete:
            star_maydria.update(825, 132, maydria_progress_star)
        elif npc_boro.quest_complete and npc_noren.quest_complete:
            star_maydria.update(825, 132, maydria_complete_star)
        elif player.quest_status["madness in marrow"] and not player.quest_complete["madness in marrow"]:
            star_maydria.update(825, 132, quest_complete_star)
        if player.quest_progress["re recycling"] == 4:
            star_roroc.update(960, 132, quest_complete_star)
        elif player.quest_status["re recycling"] and player.quest_progress["re recycling"] != 4:
            star_roroc.update(960, 132, quest_progress_star)


def load_game(player, Item, graphics, Pet):
    load_return = {"barrier learned": False, "strike learned": False, "sensed learned": False,
                   "saved": False, "start": False, "continue": False, "not found": False, "garan gift": False,
                   "offense upgrade": 0, "defense upgrade": 0}

    if os.path.getsize("save") > 0:
        with open("save", "rb") as ff:
            player_load_info = pickle.load(ff)
            player.name = player_load_info["name"]
            player.level = player_load_info["level"]
            player.health = player_load_info["hp"]
            player.energy = player_load_info["en"]
            player.offense = player_load_info["offense"]
            player.defense = player_load_info["defense"]
            player.experience = player_load_info["xp"]
            player.race = player_load_info["race"]
            player.gender = player_load_info["gender"]
            player.role = player_load_info["role"]
            player.star_power = player_load_info["star power"]
            player.flowers_amuna = player_load_info["flowers amuna"]
            player.flowers_sorae = player_load_info["flowers sorae"]
            if player_load_info["pets"]["kasper_got"]:
                player.pet.append(Pet("kasper", "scout", player_load_info["pets"]["kasper_stage"],
                                      player_load_info["pets"]["kasper_energy"],
                                      graphics["kasper_down_1"], False, player_load_info["pets"]["kasper_experience"]))
            if player_load_info["pets"]["torok_got"]:
                player.pet.append(Pet("torok", "fighter", player_load_info["pets"]["torok_stage"],
                                      player_load_info["pets"]["torok_energy"],
                                      graphics["torok_down_1"], False, player_load_info["pets"]["torok_experience"]))
            if player_load_info["pets"]["iriana_got"]:
                player.pet.append(Pet("iriana", "mage", player_load_info["pets"]["iriana_stage"],
                                      player_load_info["pets"]["iriana_energy"],
                                      graphics["iriana_down_1"], False, player_load_info["pets"]["iriana_experience"]))
            if player.race == "amuna":
                if player.gender == "male":
                    if player.role == "mage":
                        player.surf = graphics["player_mage_amuna_male_down_1"]
                    if player.role == "fighter":
                        player.surf = graphics["player_fighter_amuna_male_down_1"]
                    if player.role == "scout":
                        player.surf = graphics["player_scout_amuna_male_down_1"]
                    else:
                        player.surf = graphics["player_no_role_amuna_male_down_1"]
            if player.race == "nuldar":
                if player.gender == "male":
                    if player.role == "mage":
                        player.surf = graphics["player_mage_nuldar_male_down_1"]
                    if player.role == "fighter":
                        player.surf = graphics["player_fighter_nuldar_male_down_1"]
                    if player.role == "scout":
                        player.surf = graphics["player_scout_nuldar_male_down_1"]
                    else:
                        player.surf = graphics["player_no_role_nuldar_male_down_1"]
            if player.race == "sorae":
                if player.gender == "male":
                    if player.role == "mage":
                        player.surf = graphics["player_mage_sorae_a_down_1"]
                    if player.role == "fighter":
                        player.surf = graphics["player_fighter_sorae_a_down_1"]
                    if player.role == "scout":
                        player.surf = graphics["player_scout_sorae_a_down_1"]
                    else:
                        player.surf = graphics["player_no_role_sorae_a_down_1"]
            # clear default starting items and load personal player items from save file
            player.items.clear()
            for item in player_load_info["inventory"]:
                if item == "small health potion":
                    player.items.append(Item("small health potion", "potion", 200, 200, graphics["health_pot_img"], 0))
                if item == "small energy potion":
                    player.items.append(Item("small energy potion", "potion", 200, 200, graphics["energy_pot_img"], 0))
                if item == "big health potion":
                    player.items.append(Item("big health potion", "potion", 200, 200, graphics["health_pot_img"], 0))
                if item == "big energy potion":
                    player.items.append(Item("big energy potion", "potion", 200, 200, graphics["energy_pot_img"], 0))
                if item == "super potion":
                    player.items.append(Item("super potion", "potion", 200, 200, graphics["super_pot_img"], 0))
                if item == "pet cookie":
                    player.items.append(Item("pet cookie", "cookie", 1078, 197, graphics["pet_cookie_img"], 1))
                if item == "pet candy":
                    player.items.append(Item("pet candy", "candy", 1078, 197, graphics["pet_candy_img"], 1))
                if item == "pet tart":
                    player.items.append(Item("pet tart", "tart", 1078, 197, graphics["pet_tart_img"], 1))
                if item == "shiny rock":
                    player.items.append(Item("shiny rock", "rock", 200, 200, graphics["shiny_rock_img"], 0))
                if item == "bone dust":
                    player.items.append(Item("bone dust", "dust", 200, 200, graphics["bone_dust_img"], 0))
                if item == "cracked ember":
                    player.items.append(Item("cracked ember", "ember", 200, 200, graphics["ember"], 0))
                if item == "broken band":
                    player.items.append(Item("broken band", "band", 200, 200, graphics["band"], 0))
                if item == "dried fins":
                    player.items.append(Item("dried fins", "fins", 200, 200, graphics["fins_img"], 0))
                if item == "oscura pluma":
                    player.items.append(Item("oscura pluma", "pluma", 200, 200, graphics["pluma_img"], 0))
                if item == "boss key":
                    player.items.append(Item("boss key", "key", 200, 200, graphics["key_img"], 0))
                if item == "ramps key":
                    player.items.append(Item("ramps key", "key", 200, 200, graphics["key_img"], 0))
                if item == "power gloves":
                    player.items.append(Item("power gloves", "gloves", 200, 200, graphics["gloves"], 0))
                if item == "chroma boots":
                    player.items.append(Item("chroma boots", "boots", 200, 200, graphics["boots_img"], 0))
                if item == "basic armor":
                    player.items.append(Item("basic armor", "armor", 200, 200, graphics["basic_armor"], 1))
                if item == "forged armor":
                    player.items.append(Item("forged armor", "armor", 200, 200, graphics["forged_armor"], 2))
                if item == "mythical armor":
                    player.items.append(Item("mythical armor", "armor", 200, 200, graphics["mythical_armor"], 3))
                if item == "legendary armor":
                    player.items.append(Item("legendary armor", "armor", 200, 200, graphics["legendary_armor"], 4))
                if item == "pet seed":
                    player.items.append(Item("pet seed", "seed", 200, 200, graphics["seed_img"], 1))
                if item == "pet whistle kasper":
                    player.items.append(Item("pet whistle kasper", "whistle", 200, 200,
                                             graphics["whistle_kasper_img"], 1))
                if item == "pet whistle torok":
                    player.items.append(Item("pet whistle torok", "whistle", 200, 200,
                                             graphics["whistle_torok_img"], 1))
                if item == "pet whistle iriana":
                    player.items.append(Item("pet whistle iriana", "whistle", 200, 200,
                                             graphics["whistle_iriana_img"], 1))
                if item == "bone shard":
                    player.items.append(Item("bone shard", "shard", 200, 200, graphics["bone_shard"], 0))
                if item == "prism":
                    player.items.append(Item("prism", "prism", 200, 200, graphics["prism"], 0))
                if item == "casing":
                    player.items.append(Item("casing", "casing", 200, 200, graphics["casing"], 0))
                if item == "smelted casing":
                    player.items.append(Item("smelted casing", "casing", 200, 200, graphics["smelted_casing"], 0))
                if item == "enchanted casing":
                    player.items.append(Item("enchanted casing", "casing", 200, 200, graphics["enchanted_casing"], 0))
                if item == "seldon firework":
                    player.items.append(Item("seldon firework", "firework", 200, 200, graphics["seldon_firework"], 0))
                if item == "korlok firework":
                    player.items.append(Item("korlok firework", "firework", 200, 200, graphics["korlok_firework"], 0))
                if item == "eldream firework":
                    player.items.append(Item("eldream firework", "firework", 200, 200, graphics["eldream_firework"], 0))
                if item == "seldon bait":
                    player.items.append(Item("seldon bait", "bait", 200, 200, graphics["seldon_bait"], 0))
                if item == "korlok bait":
                    player.items.append(Item("korlok bait", "bait", 200, 200, graphics["korlok_bait"], 0))
                if item == "eldream bait":
                    player.items.append(Item("eldream bait", "bait", 200, 200, graphics["eldream_bait"], 0))
                if item == "marrow bait":
                    player.items.append(Item("marrow bait", "bait", 200, 200, graphics["marrow_bait"], 0))
                if item == "mage book":
                    player.items.append(Item("mage book", "book", 200, 200, graphics["mage_book"], 0))
                if item == "fighter book":
                    player.items.append(Item("fighter book", "book", 200, 200, graphics["fighter_book"], 0))
                if item == "scout book":
                    player.items.append(Item("scout book", "book", 200, 200, graphics["scout_book"], 0))
                if item == "cat card":
                    player.items.append(Item("cat card", "card", 200, 200, graphics["cat_card"], 0))
                if item == "trade deck":
                    player.items.append(Item("trade deck", "deck", 200, 200, graphics["trade_deck"], 0))
                if item == "nera trinket":
                    player.items.append(Item("nera trinket", "trinket", 200, 200, graphics["nera's_grace"], 0))
                if item == "aren trinket":
                    player.items.append(Item("aren trinket", "trinket", 200, 200, graphics["aren's_strength"], 0))
                if item == "spirit trinket":
                    player.items.append(Item("spirit trinket", "trinket", 200, 200, graphics["wisdom's_spirit"], 0))
                if item == "cure poison potion":
                    player.items.append(Item("cure poison potion", "potion", 200, 200, graphics["poison_cure"], 0))
                if item == "cure burn potion":
                    player.items.append(Item("cure burn potion", "potion", 200, 200, graphics["burn_cure"], 0))
                if item == "bandage wrap":
                    player.items.append(Item("bandage wrap", "wrap", 200, 200, graphics["bandage_wrap"], 0))
                if item == "big cure potion":
                    player.items.append(Item("big cure potion", "potion", 200, 200, graphics["big_cure_potion"], 0))
                if item == "brace":
                    player.items.append(Item("brace", "brace", 200, 200, graphics["brace"], 0))
                if item == "big mend potion":
                    player.items.append(Item("big mend potion", "potion", 200, 200, graphics["big_mend_potion"], 0))
                if item == "korlok ore":
                    player.items.append(Item("korlok ore", "ore", 200, 200, graphics["ore"], 0))
                if item == "pine log":
                    player.items.append(Item("pine log", "log", 200, 200, graphics["log"], 0))
                if item == "supplies":
                    player.items.append(Item("supplies", "item", 200, 200, graphics["supply"], 0))
                if item == "construct part":
                    player.items.append(Item("construct part", "part", 200, 200, graphics["part"], 0))

            for equipped_item in player_load_info["equipment"]:
                if equipped_item == "chroma boots":
                    player.equipment["boots"] = Item("chroma boots", "boots", 200, 200, graphics["boots_img"], 0)
                if equipped_item == "power gloves":
                    player.equipment["gloves"] = Item("power gloves", "gloves", 200, 200, graphics["gloves"], 0)
                if equipped_item == "basic armor":
                    player.equipment["armor"] = Item("basic armor", "armor", 200, 200, graphics["basic_armor"], 1)
                if equipped_item == "forged armor":
                    player.equipment["armor"] = Item("forged armor", "armor", 200, 200, graphics["forged_armor"], 2)
                if equipped_item == "mythical armor":
                    player.equipment["armor"] = Item("mythical armor", "armor", 200, 200, graphics["mythical_armor"], 3)
                if equipped_item == "legendary armor":
                    player.equipment["armor"] = Item("legendary armor", "armor", 200, 200, graphics["legendary_armor"],
                                                     4)
                if equipped_item == "nera trinket":
                    player.equipment["trinket 1"] = Item("nera trinket", "trinket", 200, 200,
                                                         graphics["nera's_grace"], 0)
                if equipped_item == "aren trinket":
                    player.equipment["trinket 2"] = Item("aren trinket", "trinket", 200, 200,
                                                         graphics["aren's_strength"], 0)
                if equipped_item == "spirit trinket":
                    player.equipment["trinket 3"] = Item("spirit trinket", "trinket", 200, 200,
                                                         graphics["wisdom's_spirit"], 0)

            player.current_quests = player_load_info["quests"]
            player.quest_progress = player_load_info["quest progress"]
            player.quest_status = player_load_info["quest status"]
            player.quest_complete = player_load_info["quest complete"]
            player.knowledge = player_load_info["knowledge"]
            player.skills_mage = player_load_info["mage skills"]
            player.skills_fighter = player_load_info["fighter skills"]
            player.skills_scout = player_load_info["scout skills"]
            player.mage_level = player_load_info["mage_level"]
            player.fighter_level = player_load_info["fighter_level"]
            player.scout_level = player_load_info["scout_level"]
            load_return["barrier learned"] = player_load_info["learned"]["barrier"]
            load_return["strike learned"] = player_load_info["learned"]["strike"]
            load_return["sense learned"] = player_load_info["learned"]["sense"]
            load_return["mirror learned"] = player_load_info["learned"]["mirror"]
            load_return["stun learned"] = player_load_info["learned"]["stun"]
            load_return["vanish learned"] = player_load_info["learned"]["vanish"]
            player.rupees = player_load_info["rupees"]
            player.reputation = player_load_info["reputation"]
            player.current_zone = player_load_info["zone"]
            player.velocity = player_load_info["velocity"]
            if player.current_zone == "nascent":
                player.x_coordinate = 760
                player.y_coordinate = 510
                player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))
            if player.current_zone == "seldon":
                player.x_coordinate = 425
                player.y_coordinate = 690
                player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))
            if player.current_zone == "korlok":
                player.x_coordinate = 500
                player.y_coordinate = 500
                player.rect = player.surf.get_rect(midbottom=(player.x_coordinate, player.y_coordinate))
            load_return["saved"] = player_load_info["saved"]
            load_return["garan gift"] = player_load_info["garan gift"]
            load_return["artherian gift"] = player_load_info["artherian gift"]
            load_return["artherian_complete"] = player_load_info["artherian_complete"]
            load_return["artherian_2"] = player_load_info["artherian_2"]
            load_return["rest popup"] = player_load_info["rest popup"]
            load_return["knowledge popup"] = player_load_info["knowledge popup"]
            load_return["quest guide"] = player_load_info["quest guide"]
            load_return["battle guide"] = player_load_info["battle guide"]
            load_return["rest shown before"] = player_load_info["rest shown before"]
            load_return["quest highlight popup"] = player_load_info["quest highlight popup"]
            load_return["bridge not repaired"] = player_load_info["bridge not repaired"]
            load_return["nede ghoul defeated"] = player_load_info["nede ghoul defeated"]
            load_return["bridge_cutscenes_not_viewed"] = player_load_info["bridge_cutscenes_not_viewed"]
            load_return["dreth_cutscenes_not_viewed"] = player_load_info["dreth_cutscenes_not_viewed"]
            load_return["crate_1"] = player_load_info["crate_1"]
            load_return["crate_2"] = player_load_info["crate_2"]
            load_return["crate_3"] = player_load_info["crate_3"]
            load_return["crate_4"] = player_load_info["crate_4"]
            load_return["crate_5"] = player_load_info["crate_5"]
            load_return["ramps_crate_1"] = player_load_info["ramps_crate_1"]
            load_return["ramps_crate_2"] = player_load_info["ramps_crate_2"]
            load_return["ramps_crate_3"] = player_load_info["ramps_crate_3"]
            load_return["ramps_crate_4"] = player_load_info["ramps_crate_4"]
            load_return["ramps_crate_5"] = player_load_info["ramps_crate_5"]
            load_return["switch_1"] = player_load_info["switch_1"]
            load_return["switch_2"] = player_load_info["switch_2"]
            load_return["switch_3"] = player_load_info["switch_3"]
            load_return["rock_3_con"] = player_load_info["rock_3_con"]
            load_return["rock_4_con"] = player_load_info["rock_4_con"]
            load_return["rock_5_con"] = player_load_info["rock_5_con"]
            load_return["rock_6_con"] = player_load_info["rock_6_con"]
            load_return["rock_7_con"] = player_load_info["rock_7_con"]
            load_return["rock_8_con"] = player_load_info["rock_8_con"]
            load_return["apothecary_access"] = player_load_info["apothecary_access"]
            load_return["muchador_defeated"] = player_load_info["muchador_defeated"]
            load_return["mini_boss_1_defeated"] = player_load_info["mini_boss_1_defeated"]
            load_return["mini_boss_2_defeated"] = player_load_info["mini_boss_2_defeated"]
            load_return["chinzilla_defeated"] = player_load_info["chinzilla_defeated"]
            load_return["has_key"] = player_load_info["has_key"]
            load_return["gloves_obtained"] = player_load_info["gloves_obtained"]
            load_return["boots_obtained"] = player_load_info["boots_obtained"]
            load_return["korlok_attuned"] = player_load_info["korlok_attuned"]
            load_return["eldream_attuned"] = player_load_info["eldream_attuned"]
            load_return["marrow_attuned"] = player_load_info["marrow_attuned"]
            load_return["beyond seldon"] = player_load_info["beyond seldon"]
            load_return["seed given"] = player_load_info["seed given"]
            load_return["hatch ready"] = player_load_info["hatch ready"]
            load_return["menagerie access"] = player_load_info["menagerie access"]
            load_return["kasper unlocked"] = player_load_info["kasper unlocked"]
            load_return["torok unlocked"] = player_load_info["torok unlocked"]
            load_return["iriana unlocked"] = player_load_info["iriana unlocked"]
            load_return["seed scout"] = player_load_info["seed scout"]
            load_return["seed fighter"] = player_load_info["seed fighter"]
            load_return["seed mage"] = player_load_info["seed mage"]
            load_return["start"] = True
            load_return["continue"] = False
            load_return["marrow switch phase"] = player_load_info["marrow switch phase"]
            load_return["erebyth defeated"] = player_load_info["erebyth defeated"]
            load_return["fishing_unlocked"] = player_load_info["fishing_unlocked"]
            load_return["fishing_journal_unlocked"] = player_load_info["fishing_journal_unlocked"]
            load_return["bait_given"] = player_load_info["bait_given"]
            load_return["basic_fish_counter"] = player_load_info["basic_fish_counter"]
            load_return["better_fish_counter"] = player_load_info["better_fish_counter"]
            load_return["even_better_fish_counter"] = player_load_info["even_better_fish_counter"]
            load_return["best_fish_counter"] = player_load_info["best_fish_counter"]
            load_return["fishing_level"] = player_load_info["fishing_level"]
            load_return["basic_fish_reward"] = player_load_info["basic_fish_reward"]
            load_return["better_fish_reward"] = player_load_info["better_fish_reward"]
            load_return["even_better_fish_reward"] = player_load_info["even_better_fish_reward"]
            load_return["best_fish_reward"] = player_load_info["best_fish_reward"]
            load_return["marrow_small_chest_got"] = player_load_info["marrow_small_chest_got"]
            load_return["noren_complete"] = player_load_info["noren_complete"]
            load_return["boro_complete"] = player_load_info["boro_complete"]
            load_return["vanguard_start"] = player_load_info["vanguard_start"]
            load_return["vanguard_complete"] = player_load_info["vanguard_complete"]
            load_return["artherian_start"] = player_load_info["artherian_start"]
            load_return["prism_received"] = player_load_info["prism_received"]
            load_return["castle_crate_1"] = player_load_info["castle_crate_1"]
            load_return["castle_crate_2"] = player_load_info["castle_crate_2"]
            load_return["castle_chest_1"] = player_load_info["castle_chest_1"]
            load_return["castle_chest_2"] = player_load_info["castle_chest_2"]
            load_return["dreth_taunt_1"] = player_load_info["dreth_taunt_1"]
            load_return["dreth_taunt_2"] = player_load_info["dreth_taunt_2"]
            load_return["dreth_taunt_3"] = player_load_info["dreth_taunt_3"]
            load_return["dreth_taunt_4"] = player_load_info["dreth_taunt_4"]
            load_return["mirage_updated"] = player_load_info["mirage_updated"]
            load_return["mirage_2_updated"] = player_load_info["mirage_2_updated"]
            load_return["mirage_saved"] = player_load_info["mirage_saved"]
            load_return["mirage_2_saved"] = player_load_info["mirage_2_saved"]
            load_return["rope_phase"] = player_load_info["rope_phase"]
            load_return["mirage_alive"] = player_load_info["mirage_alive"]
            load_return["thanked"] = player_load_info["thanked"]
            load_return["dreth_defeated"] = player_load_info["dreth_defeated"]
            load_return["apothis_gift"] = player_load_info["apothis_gift"]
            load_return["cat_rewarded"] = player_load_info["cat_rewarded"]
            load_return["seldon_shop_cat"] = player_load_info["seldon_shop_cat"]
            load_return["seldon_academia_cat"] = player_load_info["seldon_academia_cat"]
            load_return["korlok_shop_cat"] = player_load_info["korlok_shop_cat"]
            load_return["korlok_apothecary_cat"] = player_load_info["korlok_apothecary_cat"]
            load_return["eldream_shop_cat"] = player_load_info["eldream_shop_cat"]
            load_return["eldream_menagerie_cat"] = player_load_info["eldream_menagerie_cat"]
            load_return["marrow_cat"] = player_load_info["marrow_cat"]
            load_return["sub_marrow_opened"] = player_load_info["sub_marrow_opened"]
            load_return["credits_shown"] = player_load_info["credits_shown"]
            load_return["trading_deck"] = player_load_info["trading_deck"]
            load_return["trading_task_complete"] = player_load_info["trading_task_complete"]
            load_return["any_card_counter"] = player_load_info["any_card_counter"]
            load_return["basic_snake"] = player_load_info["basic_snake"]
            load_return["better_snake"] = player_load_info["better_snake"]
            load_return["basic_ghoul"] = player_load_info["basic_ghoul"]
            load_return["better_ghoul"] = player_load_info["better_ghoul"]
            load_return["basic_bandile"] = player_load_info["basic_bandile"]
            load_return["better_bandile"] = player_load_info["better_bandile"]
            load_return["basic_magmon"] = player_load_info["basic_magmon"]
            load_return["better_magmon"] = player_load_info["better_magmon"]
            load_return["better_necrola"] = player_load_info["better_necrola"]
            load_return["best_necrola"] = player_load_info["best_necrola"]
            load_return["better_osodark"] = player_load_info["better_osodark"]
            load_return["best_osodark"] = player_load_info["best_osodark"]
            load_return["better_atmon"] = player_load_info["better_atmon"]
            load_return["best_atmon"] = player_load_info["best_atmon"]
            load_return["better_jumano"] = player_load_info["better_jumano"]
            load_return["best_jumano"] = player_load_info["best_jumano"]
            load_return["chorizon"] = player_load_info["chorizon"]
            load_return["muchador"] = player_load_info["muchador"]
            load_return["chinzilla"] = player_load_info["chinzilla"]
            load_return["erebyth"] = player_load_info["erebyth"]
            load_return["fire_learned"] = player_load_info["fire_learned"]
            load_return["edge_learned"] = player_load_info["edge_learned"]
            load_return["arrow_learned"] = player_load_info["arrow_learned"]
            load_return["on_card_quest"] = player_load_info["on_card_quest"]
            load_return["item_block_1_got"] = player_load_info["item_block_1_got"]
            load_return["item_block_2_got"] = player_load_info["item_block_2_got"]
            load_return["item_block_3_got"] = player_load_info["item_block_3_got"]
            load_return["item_block_4_got"] = player_load_info["item_block_4_got"]
            load_return["item_block_5_got"] = player_load_info["item_block_5_got"]
            load_return["item_block_6_got"] = player_load_info["item_block_6_got"]
            load_return["item_block_7_got"] = player_load_info["item_block_7_got"]
            load_return["item_block_8_got"] = player_load_info["item_block_8_got"]
            load_return["item_block_9_got"] = player_load_info["item_block_9_got"]
            load_return["item_block_10_got"] = player_load_info["item_block_10_got"]
            load_return["item_block_11_got"] = player_load_info["item_block_11_got"]
            load_return["item_block_12_got"] = player_load_info["item_block_12_got"]
            load_return["cloaked_popup_shown"] = player_load_info["cloaked_popup_shown"]
            load_return["time_of_day"] = player_load_info["time_of_day"]
            load_return["poisoned"] = player_load_info["poisoned"]
            load_return["burned"] = player_load_info["burned"]
            load_return["bleeding"] = player_load_info["bleeding"]
            load_return["condition_popup_shown"] = player_load_info["condition_popup_shown"]
            load_return["crushed"] = player_load_info["crushed"]
            load_return["music_toggle"] = player_load_info["music_toggle"]
            load_return["apothis_upgrade"] = player_load_info["apothis_upgrade"]
            load_return["apothis_popup_shown"] = player_load_info["apothis_popup_shown"]
            load_return["pet_popup_shown"] = player_load_info["pet_popup_shown"]
            load_return["smelted_casing"] = player_load_info["smelted_casing"]

    # no save found, show a notification to player and reset condition
    else:
        load_return["continue"] = False
        load_return["not found"] = True

    return load_return


# save game function. stores player info in a dictionary that's serialized and saved to save_game file
def save_game(player, barrier_learned, hard_strike_learned, sharp_sense_learned, saved, garan_gift,
              rest_popup, knowledge_popup, quest_guide_shown, battle_guide_shown, rest_shown_before,
              quest_highlight_popup, bridge_not_repaired, nede_ghoul_defeated, bridge_cutscenes_not_viewed,
              crate_1, crate_2, crate_3, crate_4, crate_5, switch_1, switch_2, switch_3, muchador_defeated, has_key,
              mini_boss_1_defeated, mini_boss_2_defeated, gloves_obtained, korlok_attuned, eldream_attuned,
              rock_4_con, rock_5_con, rock_6_con, rock_7_con, chinzilla_defeated, apothecary_access, beyond_seldon,
              seed_given, hatch_ready, menagerie_access, kasper_unlocked, torok_unlocked, iriana_unlocked,
              rock_8_con, rock_3_con, seed_scout_count, seed_fighter_count, seed_mage_count, dreth_cutscenes,
              mirror_learned, stun_learned, vanish_learned, boots_obtained, marrow_switch_phase, erebyth_defeated,
              ramps_crate_1, ramps_crate_2, ramps_crate_3, ramps_crate_4, ramps_crate_5, marrow_attuned,
              artherian_gift, artherian_2, artherian_complete, fishing_unlocked, fishing_journal_unlocked,
              bait_given, basic_fish_counter, better_fish_counter, even_better_fish_counter, best_fish_counter,
              fishing_level, basic_fish_reward, better_fish_reward, even_better_fish_reward, best_fish_reward,
              marrow_small_chest_got, noren_complete, boro_complete, npc_maydria, artherian_task_start,
              prism_received, castle_crate_1, castle_crate_2, castle_chest_1, castle_chest_2, dreth_taunt_1,
              dreth_taunt_2, dreth_taunt_3, mirage_updated, mirage_2_updated, mirage_saved, mirage_2_saved,
              rope_phase, mirage_alive, thanked, dreth_taunt_4, dreth_defeated, apothis_gift, sub_marrow_opened,
              cat_rewarded, cats_pet, credits_shown, trading_deck, trading_task_complete, any_card_counter,
              card_deck, fire_learned, edge_learned, arrow_learned, on_card_quest, item_block_1_got, item_block_2_got,
              item_block_3_got, item_block_4_got, item_block_5_got, item_block_6_got, item_block_7_got,
              item_block_8_got, item_block_9_got, item_block_10_got, item_block_11_got, item_block_12_got,
              cloaked_popup_shown, time_of_day, poisoned, burned, bleeding, condition_popup_shown, crushed,
              music_toggle, apothis_upgrade, apothis_popup_shown, pet_popup_shown, smelted_casing):

    inventory_save = []
    equipment_save = []
    # a sprite surface object cannot be serialized, so save the string item name instead

    for item_x in player.items:
        inventory_save.append(item_x.name)

    if player.equipment["armor"] != "":
        equipment_save.append(player.equipment["armor"].name)
    if player.equipment["gloves"] != "":
        equipment_save.append(player.equipment["gloves"].name)
    if player.equipment["boots"] != "":
        equipment_save.append(player.equipment["boots"].name)
    if player.equipment["trinket 1"] != "":
        equipment_save.append(player.equipment["trinket 1"].name)
    if player.equipment["trinket 2"] != "":
        equipment_save.append(player.equipment["trinket 2"].name)
    if player.equipment["trinket 3"] != "":
        equipment_save.append(player.equipment["trinket 3"].name)

    pets = {"kasper_got": False, "torok_got": False, "iriana_got": False, "kasper_energy": 0, "torok_energy": 0,
            "iriana_energy": 0}
    try:
        for pet in player.pet:
            if pet.name == "kasper":
                pets["kasper_got"] = True
                pets["kasper_energy"] = pet.energy
                pets["kasper_experience"] = pet.experience
                pets["kasper_stage"] = pet.stage
            if pet.name == "torok":
                pets["torok_got"] = True
                pets["torok_energy"] = pet.energy
                pets["torok_experience"] = pet.experience
                pets["torok_stage"] = pet.stage
            if pet.name == "iriana":
                pets["iriana_got"] = True
                pets["iriana_energy"] = pet.energy
                pets["iriana_experience"] = pet.experience
                pets["iriana_stage"] = pet.stage
    except AttributeError:
        pass

    player_save_info = {"name": str(player.name), "race": str(player.race), "gender": str(player.gender),
                        "level": int(player.level), "role": str(player.role), "inventory": inventory_save,
                        "equipment": equipment_save, "hp": int(player.health), "en": int(player.energy),
                        "xp": int(player.experience), "offense": int(player.offense), "defense": int(player.defense),
                        "quests": dict(player.current_quests), "garan gift": garan_gift,
                        "artherian gift": artherian_gift, "artherian_2": artherian_2,
                        "artherian_complete": artherian_complete,
                        "quest progress": dict(player.quest_progress), "quest status": dict(player.quest_status),
                        "quest complete": dict(player.quest_complete), "knowledge": dict(player.knowledge),
                        "mage skills": dict(player.skills_mage), "fighter skills": dict(player.skills_fighter),
                        "scout skills": dict(player.skills_scout),
                        "learned":
                            {"barrier": barrier_learned, "strike": hard_strike_learned, "sense": sharp_sense_learned,
                             "mirror": mirror_learned, "stun": stun_learned, "vanish": vanish_learned},
                        "rupees": int(player.rupees), "reputation": dict(player.reputation),
                        "zone": str(player.current_zone), "saved": saved,
                        "rest popup": rest_popup, "knowledge popup": knowledge_popup,
                        "star power": int(player.star_power),
                        "quest guide": quest_guide_shown, "battle guide": battle_guide_shown,
                        "rest shown before": rest_shown_before, "quest highlight popup": quest_highlight_popup,
                        "bridge not repaired": bridge_not_repaired, "nede ghoul defeated": nede_ghoul_defeated,
                        "bridge_cutscenes_not_viewed": bridge_cutscenes_not_viewed,
                        "dreth_cutscenes_not_viewed": dreth_cutscenes,
                        "crate_1": crate_1, "crate_2": crate_2, "crate_3": crate_3, "crate_4": crate_4,
                        "crate_5": crate_5, "switch_1": switch_1, "switch_2": switch_2, "switch_3": switch_3,
                        "muchador_defeated": muchador_defeated, "has_key": has_key,
                        "mini_boss_1_defeated": mini_boss_1_defeated, "mini_boss_2_defeated": mini_boss_2_defeated,
                        "gloves_obtained": gloves_obtained, "korlok_attuned": korlok_attuned,
                        "marrow_attuned": marrow_attuned, "eldream_attuned": eldream_attuned,
                        "rock_3_con": rock_3_con, "rock_4_con": rock_4_con,
                        "rock_5_con": rock_5_con, "rock_6_con": rock_6_con, "rock_7_con": rock_7_con,
                        "rock_8_con": rock_8_con, "chinzilla_defeated": chinzilla_defeated,
                        "apothecary_access": apothecary_access, "flowers amuna": int(player.flowers_amuna),
                        "flowers sorae": int(player.flowers_sorae), "beyond seldon": beyond_seldon,
                        "seed given": seed_given, "hatch ready": hatch_ready, "pets": pets,
                        "menagerie access": menagerie_access, "kasper unlocked": kasper_unlocked,
                        "torok unlocked": torok_unlocked, "iriana unlocked": iriana_unlocked,
                        "seed scout": seed_scout_count, "seed fighter": seed_fighter_count,
                        "seed mage": seed_mage_count, "boots_obtained": boots_obtained,
                        "marrow switch phase": marrow_switch_phase, "erebyth defeated": erebyth_defeated,
                        "ramps_crate_1": ramps_crate_1, "ramps_crate_2": ramps_crate_2, "ramps_crate_3": ramps_crate_3,
                        "ramps_crate_4": ramps_crate_4, "ramps_crate_5": ramps_crate_5,
                        "fishing_unlocked": fishing_unlocked, "fishing_journal_unlocked": fishing_journal_unlocked,
                        "bait_given": bait_given, "basic_fish_counter": basic_fish_counter,
                        "better_fish_counter": better_fish_counter,
                        "even_better_fish_counter": even_better_fish_counter, "best_fish_counter": best_fish_counter,
                        "fishing_level": fishing_level, "basic_fish_reward": basic_fish_reward,
                        "better_fish_reward": better_fish_reward, "even_better_fish_reward": even_better_fish_reward,
                        "best_fish_reward": best_fish_reward, "marrow_small_chest_got": marrow_small_chest_got,
                        "noren_complete": noren_complete, "boro_complete": boro_complete,
                        "vanguard_start": npc_maydria.gift, "vanguard_complete": npc_maydria.quest_complete,
                        "artherian_start": artherian_task_start, "prism_received": prism_received,
                        "castle_crate_1": castle_crate_1, "castle_crate_2": castle_crate_2,
                        "castle_chest_1": castle_chest_1, "castle_chest_2": castle_chest_2,
                        "dreth_taunt_1": dreth_taunt_1, "dreth_taunt_2": dreth_taunt_2, "dreth_taunt_3": dreth_taunt_3,
                        "mirage_updated": mirage_updated, "mirage_2_updated": mirage_2_updated,
                        "mirage_saved": mirage_saved, "mirage_2_saved": mirage_2_saved, "rope_phase": rope_phase,
                        "mirage_alive": mirage_alive, "thanked": thanked, "dreth_taunt_4": dreth_taunt_4,
                        "dreth_defeated": dreth_defeated, "apothis_gift": apothis_gift,
                        "sub_marrow_opened": sub_marrow_opened, "cat_rewarded": cat_rewarded,
                        "seldon_shop_cat": cats_pet["seldon_shop"], "seldon_academia_cat": cats_pet["seldon_academia"],
                        "korlok_shop_cat": cats_pet["korlok_shop"],
                        "korlok_apothecary_cat": cats_pet["korlok_apothecary"],
                        "eldream_shop_cat": cats_pet["eldream_shop"],
                        "eldream_menagerie_cat": cats_pet["eldream_menagerie"],
                        "marrow_cat": cats_pet["marrow"], "credits_shown": credits_shown, "trading_deck": trading_deck,
                        "trading_task_complete": trading_task_complete, "any_card_counter": any_card_counter,
                        "basic_snake": card_deck["basic_snake"], "better_snake": card_deck["better_snake"],
                        "basic_ghoul": card_deck["basic_ghoul"], "better_ghoul": card_deck["better_ghoul"],
                        "basic_bandile": card_deck["basic_bandile"], "better_bandile": card_deck["better_bandile"],
                        "basic_magmon": card_deck["basic_magmon"], "better_magmon": card_deck["better_magmon"],
                        "better_necrola": card_deck["better_necrola"], "best_necrola": card_deck["best_necrola"],
                        "better_osodark": card_deck["better_osodark"], "best_osodark": card_deck["best_osodark"],
                        "better_atmon": card_deck["better_atmon"], "best_atmon": card_deck["best_atmon"],
                        "better_jumano": card_deck["better_jumano"], "best_jumano": card_deck["best_jumano"],
                        "chorizon": card_deck["chorizon"], "muchador": card_deck["muchador"],
                        "chinzilla": card_deck["chinzilla"], "erebyth": card_deck["erebyth"],
                        "fire_learned": fire_learned, "edge_learned": edge_learned, "arrow_learned": arrow_learned,
                        "on_card_quest": on_card_quest, "velocity": player.velocity,
                        "item_block_1_got": item_block_1_got, "item_block_2_got": item_block_2_got,
                        "item_block_3_got": item_block_3_got, "item_block_4_got": item_block_4_got,
                        "item_block_5_got": item_block_5_got, "item_block_6_got": item_block_6_got,
                        "item_block_7_got": item_block_7_got, "item_block_8_got": item_block_8_got,
                        "item_block_9_got": item_block_9_got, "item_block_10_got": item_block_10_got,
                        "item_block_11_got": item_block_11_got, "item_block_12_got": item_block_12_got,
                        "cloaked_popup_shown": cloaked_popup_shown, "time_of_day": time_of_day, "poisoned": poisoned,
                        "burned": burned, "bleeding": bleeding, "condition_popup_shown": condition_popup_shown,
                        "crushed": crushed, "music_toggle": music_toggle, "apothis_upgrade": apothis_upgrade,
                        "apothis_popup_shown": apothis_popup_shown, "mage_level": player.mage_level,
                        "fighter_level": player.fighter_level, "scout_level": player.scout_level,
                        "pet_popup_shown": pet_popup_shown, "smelted_casing": smelted_casing}

    try:
        with open("save", "wb") as ff:
            pickle.dump(player_save_info, ff)
        return "You saved your game. "
    except PermissionError:
        return "Could not save. "


# function to handle player walking animation with time values
def walk_time(tic):
    walk_dict = {"total time": 0, "reset": False}
    toc = time.perf_counter()
    walk_dict["total time"] = toc - tic
    if walk_dict["total time"] > 0.8:
        walk_dict["reset"] = True

    return walk_dict


def creature_update(player, seed_scout_count, seed_fighter_count, seed_mage_count, hatch_ready, seed_ready_img):
    if seed_scout_count == 4:
        for item in player.items:
            if item.name == "pet seed":
                item.update_level(item.name, 2, seed_ready_img)
                hatch_ready = True
                if not player.quest_complete["hatch 'em all"]:
                    player.quest_progress["hatch 'em all"] = 1
    if seed_fighter_count == 4:
        for item in player.items:
            if item.name == "pet seed":
                item.update_level(item.name, 2, seed_ready_img)
                hatch_ready = True
                if not player.quest_complete["hatch 'em all"]:
                    player.quest_progress["hatch 'em all"] = 1
    if seed_mage_count == 4:
        for item in player.items:
            if item.name == "pet seed":
                item.update_level(item.name, 2, seed_ready_img)
                hatch_ready = True
                if not player.quest_complete["hatch 'em all"]:
                    player.quest_progress["hatch 'em all"] = 1
    return hatch_ready


# function that updates players info, status, role, inventory, equipment, etc
def player_info_and_ui_updates(player, hp_bar, en_bar, xp_bar, star_power_meter, offense_meter, defense_meter,
                               graphics, basic_armor, forged_armor, mythical_armor, legendary_armor, power_gloves,
                               chroma_boots, neras_grace, arens_strength, spirit_of_wisdom, crushed):
    # update players status bars
    hp_bar.update(hp_bar.x_coordinate, hp_bar.y_coordinate, health_bar_update(player, graphics))
    en_bar.update(en_bar.x_coordinate, en_bar.y_coordinate, energy_bar_update(player, graphics))
    xp_bar.update(xp_bar.x_coordinate, xp_bar.y_coordinate, xp_bar_update(player, graphics))

    if crushed:
        if player.offense < 0:
            offense_meter.update(1200, 81, graphics["offense_defense_0"])
        if player.offense == 0:
            offense_meter.update(1200, 81, graphics["offense_defense_0_crushed"])
        if player.offense == 1:
            offense_meter.update(1200, 81, graphics["offense_defense_1_crushed"])
        if player.offense == 2:
            offense_meter.update(1200, 81, graphics["offense_defense_2_crushed"])
        if player.offense == 3:
            offense_meter.update(1200, 81, graphics["offense_defense_3_crushed"])
        if player.offense == 4:
            offense_meter.update(1200, 81, graphics["offense_defense_4_crushed"])
        if player.defense < 0:
            defense_meter.update(1200, 117, graphics["offense_defense_0"])
        if player.defense == 0:
            defense_meter.update(1200, 117, graphics["offense_defense_0_crushed"])
        if player.defense == 1:
            defense_meter.update(1200, 117, graphics["offense_defense_1_crushed"])
        if player.defense == 2:
            defense_meter.update(1200, 117, graphics["offense_defense_2_crushed"])
        if player.defense == 3:
            defense_meter.update(1200, 117, graphics["offense_defense_3_crushed"])
        if player.defense == 4:
            defense_meter.update(1200, 117, graphics["offense_defense_4_crushed"])
    else:
        if player.offense == 0:
            offense_meter.update(1200, 81, graphics["offense_defense_0"])
        if player.offense == 1:
            offense_meter.update(1200, 81, graphics["offense_defense_1"])
        if player.offense == 2:
            offense_meter.update(1200, 81, graphics["offense_defense_2"])
        if player.offense == 3:
            offense_meter.update(1200, 81, graphics["offense_defense_3"])
        if player.offense == 4:
            offense_meter.update(1200, 81, graphics["offense_defense_4"])
        if player.defense == 0:
            defense_meter.update(1200, 117, graphics["offense_defense_0"])
        if player.defense == 1:
            defense_meter.update(1200, 117, graphics["offense_defense_1"])
        if player.defense == 2:
            defense_meter.update(1200, 117, graphics["offense_defense_2"])
        if player.defense == 3:
            defense_meter.update(1200, 117, graphics["offense_defense_3"])
        if player.defense == 4:
            defense_meter.update(1200, 117, graphics["offense_defense_4"])

    if player.star_power == 0:
        star_power_meter.update(star_power_meter.x_coordinate, star_power_meter.y_coordinate, graphics["star_00"])
    if player.star_power == 1:
        star_power_meter.update(star_power_meter.x_coordinate, star_power_meter.y_coordinate, graphics["star_01"])
    if player.star_power == 2:
        star_power_meter.update(star_power_meter.x_coordinate, star_power_meter.y_coordinate, graphics["star_02"])
    if player.star_power == 3:
        star_power_meter.update(star_power_meter.x_coordinate, star_power_meter.y_coordinate, graphics["star_03"])
    if player.star_power >= 4:
        star_power_meter.update(star_power_meter.x_coordinate, star_power_meter.y_coordinate, graphics["star_04"])

    # update players current equipment
    drawing_functions.equipment_updates(player, graphics, basic_armor, forged_armor, mythical_armor, legendary_armor,
                                        power_gloves, chroma_boots, neras_grace, arens_strength, spirit_of_wisdom)
    # update players current inventory
    drawing_functions.item_updates(player, graphics)


# player attacks enemy, gets damage to enemy done based on player's role and offense
def attack_enemy(player, mob, sharp_sense_active, arrow_active, apothis_gift, cloaked, crushed):

    damage = 0

    level_difference = mob.level - player.level

    attack_dict = {"damage": 0, "effective": False, "non effective": False, "critical": False,
                   "pet damage": 0, "pet effective": False, "pet non effective": False}

    critical = random.randrange(1, 10)
    if critical > 5 or sharp_sense_active:
        attack_dict["critical"] = True
        # base critical damage
        if player.offense == 0:
            damage = 8
        if player.offense == 1:
            damage = 10
        if player.offense == 2:
            damage = 12
        if player.offense == 3:
            damage = 14
        if player.offense == 4:
            damage = 16
    else:
        attack_dict["critical"] = False
        # base damage
        if player.offense == 0:
            damage = 6
        if player.offense == 1:
            damage = 8
        if player.offense == 2:
            damage = 10
        if player.offense == 3:
            damage = 12
        if player.offense == 4:
            damage = 14

    # increase or decrease damage based on type advantage/disadvantage
    if player.role == "mage":
        # super effective
        if mob.type == "scout":
            damage = int(damage * 1.50)
            attack_dict["effective"] = True
        # not effective
        if mob.type == "fighter":
            damage = int(damage // 1.50)
            attack_dict["non effective"] = True
    if player.role == "scout":
        # super effective
        if mob.type == "fighter":
            damage = int(damage * 1.50)
            attack_dict["effective"] = True
        # not effective
        if mob.type == "mage":
            damage = int(damage // 1.50)
            attack_dict["non effective"] = True
    if player.role == "fighter":
        # super effective
        if mob.type == "mage":
            damage = int(damage * 1.50)
            attack_dict["effective"] = True
        # not effective
        if mob.type == "scout":
            damage = int(damage // 1.50)
            attack_dict["non effective"] = True
    # if player doesn't have a role, either do no damage or just 1
    if player.role == "":
        damage = 1
        attack_dict["non effective"] = True
        attack_dict["critical"] = False

    # level scaling final damage output
    if level_difference == 1:
        damage -= 2
    if level_difference == 2:
        damage -= 4
    if level_difference == 3:
        damage -= 6
    if level_difference == 4:
        damage -= 8
    if level_difference >= 5:
        damage -= 10

    if sharp_sense_active:
        damage += damage - int(damage * 0.80)

    if player.equipment["trinket 2"] != "":
        damage += 5

    if mob.name == "Dreth":
        if apothis_gift:
            damage = damage - 5
        else:
            damage = random.randint(1, 5)

    if mob.name == "Ghoul" or mob.name == "Necrola":
        if cloaked:
            if not sharp_sense_active:
                damage = random.randint(0, 2)

    if damage >= 0:
        attack_dict["damage"] = damage
    else:
        attack_dict["damage"] = 0

    # calculate pet damage based on its type and enemies
    for pet in player.pet:
        if pet.active:
            if pet.energy > 0:
                # pet uses energy to do damage
                pet.energy -= 1
                if pet.energy < 0:
                    pet.energy = 0
                else:
                    if pet.name == "iriana":
                        if mob.name == "Dreth":
                            if not apothis_gift:
                                attack_dict["pet damage"] = 0
                            else:
                                if pet.stage == 1:
                                    attack_dict["pet damage"] = 1
                                if pet.stage == 2:
                                    attack_dict["pet damage"] = 2
                                if pet.stage == 3:
                                    attack_dict["pet damage"] = 3
                        else:
                            if cloaked:
                                attack_dict["pet damage"] = 0
                                attack_dict["pet effective"] = False
                            else:
                                if pet.stage == 1:
                                    attack_dict["pet damage"] = 2
                                if pet.stage == 2:
                                    attack_dict["pet damage"] = 3
                                if pet.stage == 3:
                                    attack_dict["pet damage"] = 4
                                # super effective
                                if mob.type == "scout":
                                    if pet.stage == 1:
                                        attack_dict["pet damage"] = 4
                                        attack_dict["pet effective"] = True
                                    if pet.stage == 2:
                                        attack_dict["pet damage"] = 5
                                        attack_dict["pet effective"] = True
                                    if pet.stage == 3:
                                        attack_dict["pet damage"] = 6
                                        attack_dict["pet effective"] = True
                                # not effective
                                if mob.type == "fighter":
                                    if pet.stage == 1:
                                        attack_dict["pet damage"] = 1
                                        attack_dict["pet non effective"] = True
                                    if pet.stage == 2:
                                        attack_dict["pet damage"] = 2
                                        attack_dict["pet non effective"] = True
                                    if pet.stage == 3:
                                        attack_dict["pet damage"] = 3
                                        attack_dict["pet non effective"] = True
                    if pet.name == "kasper":
                        if mob.name == "Dreth":
                            if not apothis_gift:
                                attack_dict["pet damage"] = 0
                                attack_dict["pet non effective"] = True
                            else:
                                if pet.stage == 1:
                                    attack_dict["pet damage"] = 0
                                    attack_dict["pet non effective"] = True
                                if pet.stage == 2:
                                    attack_dict["pet damage"] = 0
                                    attack_dict["pet non effective"] = True
                                if pet.stage == 3:
                                    attack_dict["pet damage"] = 1
                                    attack_dict["pet non effective"] = True
                        else:
                            if cloaked:
                                attack_dict["pet damage"] = 0
                                attack_dict["pet effective"] = False
                            else:
                                if pet.stage == 1:
                                    attack_dict["pet damage"] = 2
                                if pet.stage == 2:
                                    attack_dict["pet damage"] = 3
                                if pet.stage == 3:
                                    attack_dict["pet damage"] = 4
                                # super effective
                                if mob.type == "fighter":
                                    if pet.stage == 1:
                                        attack_dict["pet damage"] = 4
                                        attack_dict["pet effective"] = True
                                    if pet.stage == 2:
                                        attack_dict["pet damage"] = 5
                                        attack_dict["pet effective"] = True
                                    if pet.stage == 3:
                                        attack_dict["pet damage"] = 6
                                        attack_dict["pet effective"] = True
                                # not effective
                                if mob.type == "mage":
                                    if pet.stage == 1:
                                        attack_dict["pet damage"] = 1
                                        attack_dict["pet non effective"] = True
                                    if pet.stage == 2:
                                        attack_dict["pet damage"] = 2
                                        attack_dict["pet non effective"] = True
                                    if pet.stage == 3:
                                        attack_dict["pet damage"] = 3
                                        attack_dict["pet non effective"] = True
                    if pet.name == "torok":
                        if mob.name == "Dreth":
                            if not apothis_gift:
                                attack_dict["pet damage"] = 1
                                attack_dict["pet effective"] = True
                            else:
                                if pet.stage == 1:
                                    attack_dict["pet damage"] = 3
                                    attack_dict["pet effective"] = True
                                if pet.stage == 2:
                                    attack_dict["pet damage"] = 4
                                    attack_dict["pet effective"] = True
                                if pet.stage == 5:
                                    attack_dict["pet damage"] = 5
                                    attack_dict["pet effective"] = True
                        else:
                            if cloaked:
                                attack_dict["pet damage"] = 0
                                attack_dict["pet effective"] = False
                            else:
                                if pet.stage == 1:
                                    attack_dict["pet damage"] = 2
                                if pet.stage == 2:
                                    attack_dict["pet damage"] = 3
                                if pet.stage == 3:
                                    attack_dict["pet damage"] = 4
                                # super effective
                                if mob.type == "mage":
                                    if pet.stage == 1:
                                        attack_dict["pet damage"] = 4
                                        attack_dict["pet effective"] = True
                                    if pet.stage == 2:
                                        attack_dict["pet damage"] = 5
                                        attack_dict["pet effective"] = True
                                    if pet.stage == 3:
                                        attack_dict["pet damage"] = 6
                                        attack_dict["pet effective"] = True
                                # not effective
                                if mob.type == "scout":
                                    if pet.stage == 1:
                                        attack_dict["pet damage"] = 1
                                        attack_dict["pet non effective"] = True
                                    if pet.stage == 2:
                                        attack_dict["pet damage"] = 2
                                        attack_dict["pet non effective"] = True
                                    if pet.stage == 3:
                                        attack_dict["pet damage"] = 3
                                        attack_dict["pet non effective"] = True

    return attack_dict


# enemy attacks player, gets damage to player done, subtract players defense level
def attack_player(player, mob, barrier_active, arrow_active, crushed, strike_active):

    damage = 0

    level_difference = mob.level - player.level

    attack_dict = {"damage": 0, "effective": False, "non effective": False, "critical": False}

    critical = random.randrange(1, 10)
    if critical > 5 and not barrier_active:
        attack_dict["critical"] = True
        # base critical damage
        if player.level < 8:
            if player.defense <= 0:
                damage = 8
            if player.defense == 1:
                damage = 6
            if player.defense == 2:
                damage = 4
            if player.defense == 3:
                damage = 2
            if player.defense == 4:
                damage = 1
        if 16 > player.level >= 8:
            if player.defense <= 0:
                damage = 10
            if player.defense == 1:
                damage = 8
            if player.defense == 2:
                damage = 6
            if player.defense == 3:
                damage = 4
            if player.defense == 4:
                damage = 2
        if player.level >= 16:
            if player.defense <= 0:
                damage = 12
            if player.defense == 1:
                damage = 10
            if player.defense == 2:
                damage = 8
            if player.defense == 3:
                damage = 6
            if player.defense == 4:
                damage = 4
    else:
        attack_dict["critical"] = False
        # base damage
        if player.level < 8:
            if player.defense <= 0:
                damage = 6
            if player.defense == 1:
                damage = 4
            if player.defense == 2:
                damage = 2
            if player.defense == 3:
                damage = 1
            if player.defense == 4:
                damage = 0
        if 16 > player.level >= 8:
            if player.defense <= 0:
                damage = 8
            if player.defense == 1:
                damage = 6
            if player.defense == 2:
                damage = 4
            if player.defense == 3:
                damage = 2
            if player.defense == 4:
                damage = 1
        if player.level >= 16:
            if player.defense <= 0:
                damage = 10
            if player.defense == 1:
                damage = 8
            if player.defense == 2:
                damage = 6
            if player.defense == 3:
                damage = 4
            if player.defense == 4:
                damage = 2

    # increase or decrease damage based on type advantage/disadvantage
    if mob.type == "mage":
        # super effective
        if player.role == "scout":
            damage = int(damage * 1.50)
            attack_dict["effective"] = True
        # not effective
        if player.role == "fighter":
            damage = int(damage // 1.50)
            attack_dict["non effective"] = True
    if mob.type == "scout":
        # super effective
        if player.role == "fighter":
            damage = int(damage * 1.50)
            attack_dict["effective"] = True
        # not effective
        if player.role == "mage":
            damage = int(damage // 1.50)
            attack_dict["non effective"] = True
    if mob.type == "fighter":
        # super effective
        if player.role == "mage":
            damage = int(damage * 1.50)
            attack_dict["effective"] = True
        # not effective
        if player.role == "scout":
            damage = int(damage // 1.50)
            attack_dict["non effective"] = True

    # level scaling final damage output
    if level_difference == 1:
        damage += 1
    if level_difference == 2:
        damage += 3
    if level_difference == 3:
        damage += 6
    if level_difference == 4:
        damage += 9
    if level_difference >= 5:
        damage += 12

    if barrier_active:
        damage -= damage - int(damage * 0.80)

    if strike_active:
        damage -= 3

    if damage >= 0:
        attack_dict["damage"] = damage
    else:
        attack_dict["damage"] = 0

    return attack_dict


# level up function. increase player level by 1 if not at cap and return info in dictionary
def level_up(player, level_up_win, level_up_font):
    level_up_dictionary = {"new level": 0, "player stats": []}

    if player.level < 30:
        player.level = player.level + 1
        player.health = 100
        player.energy = 100
        player.experience = player.experience - 100
        drawing_functions.level_up_draw(level_up_win, player, level_up_font, True)
    else:
        level_up_dictionary["new level"] = "You are already max level. "
        return level_up_dictionary


# function to respawn enemies if they are less than a specified amount active in game. spawns with random coord. and lvl
def enemy_respawn(player, seldon_enemies, korlok_enemies, snakes, ghouls, magmons, bandiles, interactables_seldon,
                  interactables_korlok, interactables_mines, Enemy, Item, graphic_dict, UiElement, seldon_flowers,
                  eldream_flowers, interactables_eldream, ectrenos_front_enemies, marrow_ghouls,
                  ectrenos_alcove_enemies, atmons, jumanos, artherian_task_start, artherian_gift, maydria_gift,
                  prism_received, time_of_day):
    if player.current_zone == "seldon":
        snake_counter = 0
        ghoul_counter = 0
        flower_counter = 0

        flower_coords_list = [(190, 185), (390, 185), (150, 425), (400, 500), (590, 380)]

        # generate random coordinates and level for new enemy to spawn within boundaries and level range
        # if not scaled, coordinates set to default boundaries
        random_snake_x = random.randrange(100, 300)
        random_snake_y = random.randrange(150, 300)
        random_snake_level = random.randrange(1, 4)
        random_ghoul_x = random.randrange(650, 900)
        random_ghoul_y = random.randrange(150, 300)
        random_ghoul_level = random.randrange(4, 7)

        random_flower_coord = random.choice(flower_coords_list)

        # count current enemies active in game
        for mob in seldon_enemies:
            if mob.name == "Snake":
                snake_counter += 1
            if mob.name == "Ghoul":
                ghoul_counter += 1

        # if there are less than 3 snakes in game, create another snake with random level and coordinates. add to groups
        if snake_counter < 3:
            if player.quest_status["sneaky snakes"] and not player.quest_complete["sneaky snakes"]:
                if time_of_day == 0 or time_of_day == 7:
                    new_snake = Enemy("Snake", "snake", 100, 100, random_snake_level, random_snake_x, random_snake_y,
                                      True, Item("shiny rock", "rock", 200, 200, graphic_dict["shiny_rock_img"], 0),
                                      graphic_dict["snake_high_night"],
                                      UiElement("snake hp bar", 700, 90, graphic_dict["hp_100"]), "fighter")
                else:
                    new_snake = Enemy("Snake", "snake", 100, 100, random_snake_level, random_snake_x, random_snake_y,
                                      True, Item("shiny rock", "rock", 200, 200, graphic_dict["shiny_rock_img"], 0),
                                      graphic_dict["snake_high"],
                                      UiElement("snake hp bar", 700, 90, graphic_dict["hp_100"]), "fighter")

            else:
                if time_of_day == 0 or time_of_day == 7:
                    new_snake = Enemy("Snake", "snake", 100, 100, random_snake_level, random_snake_x, random_snake_y,
                                      True, Item("shiny rock", "rock", 200, 200, graphic_dict["shiny_rock_img"], 0),
                                      graphic_dict["snake_night"],
                                      UiElement("snake hp bar", 700, 90, graphic_dict["hp_100"]), "fighter")
                else:
                    new_snake = Enemy("Snake", "snake", 100, 100, random_snake_level, random_snake_x, random_snake_y,
                                      True, Item("shiny rock", "rock", 200, 200, graphic_dict["shiny_rock_img"], 0),
                                      graphic_dict["snake"],
                                      UiElement("snake hp bar", 700, 90, graphic_dict["hp_100"]), "fighter")
            snakes.add(new_snake)
            seldon_enemies.add(new_snake)
            interactables_seldon.add(new_snake)
        # if there are less than 3 ghouls in game, create another ghoul with random level and coordinates. add to groups
        if ghoul_counter < 3:
            if player.quest_status["ghouled again"] and not player.quest_complete["ghouled again"]:
                new_ghoul = Enemy("Ghoul", "ghoul", 100, 100, random_ghoul_level, random_ghoul_x, random_ghoul_y, True,
                                  Item("bone dust", "dust", 200, 200, graphic_dict["bone_dust_img"], 0),
                                  graphic_dict["ghoul_high"],
                                  UiElement("ghoul hp bar", 700, 90, graphic_dict["hp_100"]), "scout")
            else:
                new_ghoul = Enemy("Ghoul", "ghoul", 100, 100, random_ghoul_level, random_ghoul_x, random_ghoul_y, True,
                                  Item("bone dust", "dust", 200, 200, graphic_dict["bone_dust_img"], 0),
                                  graphic_dict["ghoul"],
                                  UiElement("ghoul hp bar", 700, 90, graphic_dict["hp_100"]), "scout")
            ghouls.add(new_ghoul)
            seldon_enemies.add(new_ghoul)
            interactables_seldon.add(new_ghoul)

        for flower in seldon_flowers:
            if flower:
                flower_counter += 1
        if flower_counter < 3:
            new_flower = Item("flower seldon", "flower", random_flower_coord[0], random_flower_coord[1],
                              graphic_dict["flower_seldon"], 0)
            seldon_flowers.add(new_flower)
            interactables_seldon.add(new_flower)

    if player.current_zone == "korlok":
        magmon_counter = 0
        # generate random coordinates and level for new enemy to spawn within boundaries and level range
        # if not scaled, coordinates set to default boundaries
        random_magmon_x = random.randrange(100, 375)
        random_magmon_y = random.randrange(125, 225)
        random_magmon_level = random.randrange(10, 12)

        # count current enemies active in game
        for mob in magmons:
            if mob.name == "Magmon":
                magmon_counter += 1

        # if there are less than 3 in game, create another with random level and coordinates. add to groups
        if magmon_counter < 3:
            if time_of_day == 0 or time_of_day == 7:
                if player.quest_status["elementary elementals"] and not player.quest_complete["elementary elementals"]:
                    new_magmon = Enemy("Magmon", "magmon", 100, 100, random_magmon_level, random_magmon_x,
                                       random_magmon_y,
                                       True, Item("cracked ember", "ember", 200, 200, graphic_dict["ember"], 0),
                                       graphic_dict["magmon_high_night"],
                                       UiElement("magmon hp bar", 700, 90, graphic_dict["hp_100"]), "mage")
                else:
                    new_magmon = Enemy("Magmon", "magmon", 100, 100, random_magmon_level, random_magmon_x,
                                       random_magmon_y,
                                       True, Item("cracked ember", "ember", 200, 200, graphic_dict["ember"], 0),
                                       graphic_dict["magmon_night"],
                                       UiElement("magmon hp bar", 700, 90, graphic_dict["hp_100"]), "mage")
            else:
                if player.quest_status["elementary elementals"] and not player.quest_complete["elementary elementals"]:
                    new_magmon = Enemy("Magmon", "magmon", 100, 100, random_magmon_level, random_magmon_x,
                                       random_magmon_y,
                                       True, Item("cracked ember", "ember", 200, 200, graphic_dict["ember"], 0),
                                       graphic_dict["magmon_high"],
                                       UiElement("magmon hp bar", 700, 90, graphic_dict["hp_100"]), "mage")
                else:
                    new_magmon = Enemy("Magmon", "magmon", 100, 100, random_magmon_level, random_magmon_x,
                                       random_magmon_y,
                                       True, Item("cracked ember", "ember", 200, 200, graphic_dict["ember"], 0),
                                       graphic_dict["magmon"],
                                       UiElement("magmon hp bar", 700, 90, graphic_dict["hp_100"]), "mage")
            magmons.add(new_magmon)
            korlok_enemies.add(new_magmon)
            interactables_korlok.add(new_magmon)

    if player.current_zone == "mines":
        bandile_counter = 0
        # generate random coordinates and level for new enemy to spawn within boundaries and level range
        # if not scaled, coordinates set to default boundaries
        random_bandile_x = random.randrange(655, 880)
        random_bandile_y = random.randrange(165, 335)
        random_bandile_level = random.randrange(6, 9)

        # count current enemies active in game
        for mob in bandiles:
            if mob.name == "Bandile":
                bandile_counter += 1

        # if there are less than 3 in game, create another with random level and coordinates. add to groups
        if bandile_counter < 3:
            if time_of_day == 0 or time_of_day == 7:
                if player.quest_status["band hammer"] and not player.quest_complete["band hammer"]:
                    new_bandile = Enemy("Bandile", "bandile", 100, 100, random_bandile_level, random_bandile_x,
                                        random_bandile_y, True,
                                        Item("broken band", "band", 200, 200, graphic_dict["band"], 0),
                                        graphic_dict["bandile_high_night"],
                                        UiElement("bandile hp bar", 700, 90, graphic_dict["hp_100"]), "fighter")
                else:
                    new_bandile = Enemy("Bandile", "bandile", 100, 100, random_bandile_level, random_bandile_x,
                                        random_bandile_y, True,
                                        Item("broken band", "band", 200, 200, graphic_dict["band"], 0),
                                        graphic_dict["bandile_night"],
                                        UiElement("bandile hp bar", 700, 90, graphic_dict["hp_100"]), "fighter")
            else:
                if player.quest_status["band hammer"] and not player.quest_complete["band hammer"]:
                    new_bandile = Enemy("Bandile", "bandile", 100, 100, random_bandile_level, random_bandile_x,
                                        random_bandile_y, True,
                                        Item("broken band", "band", 200, 200, graphic_dict["band"], 0),
                                        graphic_dict["bandile_high"],
                                        UiElement("bandile hp bar", 700, 90, graphic_dict["hp_100"]), "fighter")
                else:
                    new_bandile = Enemy("Bandile", "bandile", 100, 100, random_bandile_level, random_bandile_x,
                                        random_bandile_y, True,
                                        Item("broken band", "band", 200, 200, graphic_dict["band"], 0),
                                        graphic_dict["bandile"],
                                        UiElement("bandile hp bar", 700, 90, graphic_dict["hp_100"]), "fighter")
            bandiles.add(new_bandile)
            interactables_mines.add(new_bandile)

    if player.current_zone == "eldream":
        flower_coords_list = [(355, 530), (722, 530), (850, 120), (985, 450), (775, 670)]
        flower_counter = 0
        random_flower_coord = random.choice(flower_coords_list)

        for flower in eldream_flowers:
            if flower:
                flower_counter += 1

        if flower_counter < 3:
            new_flower = Item("flower eldream", "flower", random_flower_coord[0], random_flower_coord[1],
                              graphic_dict["flower_eldream"], 0)
            eldream_flowers.add(new_flower)
            interactables_eldream.add(new_flower)

    if player.current_zone == "ectrenos front":
        necrola_counter = 0
        # generate random coordinates and level for new enemy to spawn within boundaries and level range
        # if not scaled, coordinates set to default boundaries
        random_necrola_x = random.randrange(200, 600)
        random_necrola_y = random.randrange(350, 500)
        random_necrola_level = random.randrange(14, 16)

        # count current enemies active in game
        for mob in ectrenos_front_enemies:
            if mob.name == "Necrola":
                necrola_counter += 1

        # if there are less than 3 in game, create another with random level and coordinates. add to groups
        if necrola_counter < 3:
            if player.quest_status["shades of fear"] and not player.quest_complete["shades of fear"]:
                new_necrola = Enemy("Necrola", "necrola", 100, 100, random_necrola_level, random_necrola_x,
                                    random_necrola_y, True, Item("oscura pluma", "pluma", 200, 200,
                                                                 graphic_dict["pluma_img"], 0),
                                    graphic_dict["necrola_high"],
                                    UiElement("necrola hp bar", 700, 90, graphic_dict["hp_100"]), "scout")
            else:
                new_necrola = Enemy("Necrola", "necrola", 100, 100, random_necrola_level, random_necrola_x,
                                    random_necrola_y, True, Item("oscura pluma", "pluma", 200, 200,
                                                                 graphic_dict["pluma_img"], 0),
                                    graphic_dict["necrola"],
                                    UiElement("necrola hp bar", 700, 90, graphic_dict["hp_100"]), "scout")
            ectrenos_front_enemies.add(new_necrola)

    if player.current_zone == "ectrenos alcove":
        osodark_counter = 0
        # generate random coordinates and level for new enemy to spawn within boundaries and level range
        # if not scaled, coordinates set to default boundaries
        random_osodark_x = random.randrange(250, 700)
        random_osodark_y = random.randrange(200, 300)
        random_osodark_level = random.randrange(15, 20)

        # count current enemies active in game
        for mob in ectrenos_alcove_enemies:
            if mob.name == "Osodark":
                osodark_counter += 1

        # if there are less than 3 in game, create another with random level and coordinates. add to groups
        if osodark_counter < 3:
            if time_of_day == 0 or time_of_day == 7:
                new_osodark = Enemy("Osodark", "osodark", 100, 100, random_osodark_level, random_osodark_x,
                                    random_osodark_y, True,
                                    Item("dried fins", "fins", 200, 200, graphic_dict["fins_img"], 0),
                                    graphic_dict["osodark_night"],
                                    UiElement("osodark hp bar", 700, 90, graphic_dict["hp_100"]), "fighter")
            else:
                new_osodark = Enemy("Osodark", "osodark", 100, 100, random_osodark_level, random_osodark_x,
                                    random_osodark_y, True,
                                    Item("dried fins", "fins", 200, 200, graphic_dict["fins_img"], 0),
                                    graphic_dict["osodark"],
                                    UiElement("osodark hp bar", 700, 90, graphic_dict["hp_100"]), "fighter")
            ectrenos_alcove_enemies.add(new_osodark)

    if player.current_zone == "marrow":
        marrow_ghoul_counter = 0
        # generate random coordinates and level for new enemy to spawn within boundaries and level range
        # if not scaled, coordinates set to default boundaries
        random_marrow_ghoul_x = random.randrange(125, 600)
        random_marrow_ghoul_y = random.randrange(100, 300)
        random_marrow_ghoul_level = random.randrange(20, 24)

        # count current enemies active in game
        for mob in marrow_ghouls:
            if mob.name == "Ghoul":
                marrow_ghoul_counter += 1

        # if there are less than 3 in game, create another with random level and coordinates. add to groups
        if marrow_ghoul_counter < 3:
            if artherian_task_start and not artherian_gift:
                new_marrow_ghoul = Enemy("Ghoul", "ghoul", 100, 100, random_marrow_ghoul_level, random_marrow_ghoul_x,
                                         random_marrow_ghoul_y, True, Item("bone shard", "shard", 200, 200,
                                                                           graphic_dict["bone_shard"], 0),
                                         graphic_dict["ghoul_high"],
                                         UiElement("ghoul hp bar", 700, 90, graphic_dict["hp_100"]), "scout")
            else:
                new_marrow_ghoul = Enemy("Ghoul", "ghoul", 100, 100, random_marrow_ghoul_level, random_marrow_ghoul_x,
                                         random_marrow_ghoul_y, True, Item("bone shard", "shard", 200, 200,
                                                                           graphic_dict["bone_shard"], 0),
                                         graphic_dict["ghoul"],
                                         UiElement("ghoul hp bar", 700, 90, graphic_dict["hp_100"]), "scout")
            marrow_ghouls.add(new_marrow_ghoul)

    if player.current_zone == "sub marrow":
        marrow_atmon_counter = 0
        # generate random coordinates and level for new enemy to spawn within boundaries and level range
        # if not scaled, coordinates set to default boundaries
        random_marrow_atmon_x = random.randrange(75, 400)
        random_marrow_atmon_y = random.randrange(150, 400)
        random_marrow_atmon_level = random.choice([22, 24])

        # count current enemies active in game
        for mob in atmons:
            if mob.name == "Atmon":
                marrow_atmon_counter += 1

        # if there are less than 3 in game, create another with random level and coordinates. add to groups
        if marrow_atmon_counter < 3:
            if time_of_day == 0 or time_of_day == 7:
                if maydria_gift and not prism_received:
                    new_marrow_atmon = Enemy("Atmon", "atmon", 100, 100, random_marrow_atmon_level,
                                             random_marrow_atmon_x, random_marrow_atmon_y, True,
                                             Item("prism", "prism", 200, 200, graphic_dict["prism"], 0),
                                             graphic_dict["atmon_high_night"],
                                             UiElement("atmon hp bar", 700, 90, graphic_dict["hp_100"]), "mage")
                    if random_marrow_atmon_level == 24:
                        new_marrow_atmon.surf.set_alpha(50)
                else:
                    new_marrow_atmon = Enemy("Atmon", "atmon", 100, 100, random_marrow_atmon_level,
                                             random_marrow_atmon_x, random_marrow_atmon_y, True,
                                             Item("prism", "prism", 200, 200, graphic_dict["prism"], 0),
                                             graphic_dict["atmon_night"],
                                             UiElement("atmon hp bar", 700, 90, graphic_dict["hp_100"]), "mage")
                    if random_marrow_atmon_level == 24:
                        new_marrow_atmon.surf.set_alpha(50)
            else:
                if maydria_gift and not prism_received:
                    new_marrow_atmon = Enemy("Atmon", "atmon", 100, 100, random_marrow_atmon_level,
                                             random_marrow_atmon_x, random_marrow_atmon_y, True,
                                             Item("prism", "prism", 200, 200, graphic_dict["prism"], 0),
                                             graphic_dict["atmon_high"],
                                             UiElement("atmon hp bar", 700, 90, graphic_dict["hp_100"]), "mage")
                    if random_marrow_atmon_level == 24:
                        new_marrow_atmon.surf.set_alpha(50)
                else:
                    new_marrow_atmon = Enemy("Atmon", "atmon", 100, 100, random_marrow_atmon_level,
                                             random_marrow_atmon_x, random_marrow_atmon_y, True,
                                             Item("prism", "prism", 200, 200, graphic_dict["prism"], 0),
                                             graphic_dict["atmon"],
                                             UiElement("atmon hp bar", 700, 90, graphic_dict["hp_100"]), "mage")
                    if random_marrow_atmon_level == 24:
                        new_marrow_atmon.surf.set_alpha(50)
            atmons.add(new_marrow_atmon)

    if player.current_zone == "castle one":
        jumano_counter = 0
        # generate random coordinates and level for new enemy to spawn within boundaries and level range
        # if not scaled, coordinates set to default boundaries
        random_jumano_x = random.randrange(100, 800)
        random_jumano_y = random.randrange(100, 300)
        random_jumano_level = random.randrange(25, 28)
        # count current enemies active in game
        for mob in jumanos:
            if mob.name == "Jumano":
                jumano_counter += 1
        # if there are less than 3  in game, create another with random level and coordinates. add to groups
        if jumano_counter < 3:
            new_jumano = Enemy("Jumano", "jumano", 100, 100, random_jumano_level, random_jumano_x,
                               random_jumano_y, True,
                               Item("marrow bait", "bait", 200, 200, graphic_dict["marrow_bait"], 0),
                               graphic_dict["jumano"],
                               UiElement("jumano hp bar", 700, 90, graphic_dict["hp_100"]), "fighter")
            jumanos.add(new_jumano)

    respawn_dict = {"seldon_enemies": seldon_enemies, "snakes": snakes, "ghouls": ghouls,
                    "interactables_seldon": interactables_seldon, "interactables_korlok": interactables_korlok,
                    "korlok_enemies": korlok_enemies, "magmons": magmons, "bandiles": bandiles, "seldon_flowers":
                        seldon_flowers, "eldream_flowers": eldream_flowers,
                    "interactables_eldream": interactables_eldream,
                    "ectrenos_front_enemies": ectrenos_front_enemies, "marrow_ghouls": marrow_ghouls,
                    "ectrenos_alcove_enemies": ectrenos_alcove_enemies, "atmons": atmons, "jumanos": jumanos}

    return respawn_dict


# player bar update functions. return image representing amount
def health_bar_update(character, graphics):
    if character.health == 100:
        return graphics["hp_100"]
    if character.health == 99:
        return graphics["hp_99"]
    if character.health == 98:
        return graphics["hp_98"]
    if character.health == 97:
        return graphics["hp_97"]
    if character.health == 96:
        return graphics["hp_96"]
    if character.health == 95:
        return graphics["hp_95"]
    if character.health == 94:
        return graphics["hp_94"]
    if character.health == 93:
        return graphics["hp_93"]
    if character.health == 92:
        return graphics["hp_92"]
    if character.health == 91:
        return graphics["hp_91"]
    if character.health == 90:
        return graphics["hp_90"]
    if character.health == 89:
        return graphics["hp_89"]
    if character.health == 88:
        return graphics["hp_88"]
    if character.health == 87:
        return graphics["hp_87"]
    if character.health == 86:
        return graphics["hp_86"]
    if character.health == 85:
        return graphics["hp_85"]
    if character.health == 84:
        return graphics["hp_84"]
    if character.health == 83:
        return graphics["hp_83"]
    if character.health == 82:
        return graphics["hp_82"]
    if character.health == 81:
        return graphics["hp_81"]
    if character.health == 80:
        return graphics["hp_80"]
    if character.health == 79:
        return graphics["hp_79"]
    if character.health == 78:
        return graphics["hp_78"]
    if character.health == 77:
        return graphics["hp_77"]
    if character.health == 76:
        return graphics["hp_76"]
    if character.health == 75:
        return graphics["hp_75"]
    if character.health == 74:
        return graphics["hp_74"]
    if character.health == 73:
        return graphics["hp_73"]
    if character.health == 72:
        return graphics["hp_72"]
    if character.health == 71:
        return graphics["hp_71"]
    if character.health == 70:
        return graphics["hp_70"]
    if character.health == 69:
        return graphics["hp_69"]
    if character.health == 68:
        return graphics["hp_68"]
    if character.health == 67:
        return graphics["hp_67"]
    if character.health == 66:
        return graphics["hp_66"]
    if character.health == 65:
        return graphics["hp_65"]
    if character.health == 64:
        return graphics["hp_64"]
    if character.health == 63:
        return graphics["hp_63"]
    if character.health == 62:
        return graphics["hp_62"]
    if character.health == 61:
        return graphics["hp_61"]
    if character.health == 60:
        return graphics["hp_60"]
    if character.health == 59:
        return graphics["hp_59"]
    if character.health == 58:
        return graphics["hp_58"]
    if character.health == 57:
        return graphics["hp_57"]
    if character.health == 56:
        return graphics["hp_56"]
    if character.health == 55:
        return graphics["hp_55"]
    if character.health == 54:
        return graphics["hp_54"]
    if character.health == 53:
        return graphics["hp_53"]
    if character.health == 52:
        return graphics["hp_52"]
    if character.health == 51:
        return graphics["hp_51"]
    if character.health == 50:
        return graphics["hp_50"]
    if character.health == 49:
        return graphics["hp_49"]
    if character.health == 48:
        return graphics["hp_48"]
    if character.health == 47:
        return graphics["hp_47"]
    if character.health == 46:
        return graphics["hp_46"]
    if character.health == 45:
        return graphics["hp_45"]
    if character.health == 44:
        return graphics["hp_44"]
    if character.health == 43:
        return graphics["hp_43"]
    if character.health == 42:
        return graphics["hp_42"]
    if character.health == 41:
        return graphics["hp_41"]
    if character.health == 40:
        return graphics["hp_40"]
    if character.health == 39:
        return graphics["hp_39"]
    if character.health == 38:
        return graphics["hp_38"]
    if character.health == 37:
        return graphics["hp_37"]
    if character.health == 36:
        return graphics["hp_36"]
    if character.health == 35:
        return graphics["hp_35"]
    if character.health == 34:
        return graphics["hp_34"]
    if character.health == 33:
        return graphics["hp_33"]
    if character.health == 32:
        return graphics["hp_32"]
    if character.health == 31:
        return graphics["hp_31"]
    if character.health == 30:
        return graphics["hp_30"]
    if character.health == 29:
        return graphics["hp_29"]
    if character.health == 28:
        return graphics["hp_28"]
    if character.health == 27:
        return graphics["hp_27"]
    if character.health == 26:
        return graphics["hp_26"]
    if character.health == 25:
        return graphics["hp_25"]
    if character.health == 24:
        return graphics["hp_24"]
    if character.health == 23:
        return graphics["hp_23"]
    if character.health == 22:
        return graphics["hp_22"]
    if character.health == 21:
        return graphics["hp_21"]
    if character.health == 20:
        return graphics["hp_20"]
    if character.health == 19:
        return graphics["hp_19"]
    if character.health == 18:
        return graphics["hp_18"]
    if character.health == 17:
        return graphics["hp_17"]
    if character.health == 16:
        return graphics["hp_16"]
    if character.health == 15:
        return graphics["hp_15"]
    if character.health == 14:
        return graphics["hp_14"]
    if character.health == 13:
        return graphics["hp_13"]
    if character.health == 12:
        return graphics["hp_12"]
    if character.health == 11:
        return graphics["hp_11"]
    if character.health == 10:
        return graphics["hp_10"]
    if character.health == 9:
        return graphics["hp_9"]
    if character.health == 8:
        return graphics["hp_8"]
    if character.health == 7:
        return graphics["hp_7"]
    if character.health == 6:
        return graphics["hp_6"]
    if character.health == 5:
        return graphics["hp_5"]
    if character.health == 4:
        return graphics["hp_4"]
    if character.health == 3:
        return graphics["hp_3"]
    if character.health == 2:
        return graphics["hp_2"]
    if character.health == 1:
        return graphics["hp_1"]
    if character.health == 0:
        return graphics["hp_0"]


def energy_bar_update(character, graphics):
    if character.energy == 100:
        return graphics["en_100"]
    if character.energy == 99:
        return graphics["en_99"]
    if character.energy == 98:
        return graphics["en_98"]
    if character.energy == 97:
        return graphics["en_97"]
    if character.energy == 96:
        return graphics["en_96"]
    if character.energy == 95:
        return graphics["en_95"]
    if character.energy == 94:
        return graphics["en_94"]
    if character.energy == 93:
        return graphics["en_93"]
    if character.energy == 92:
        return graphics["en_92"]
    if character.energy == 91:
        return graphics["en_91"]
    if character.energy == 90:
        return graphics["en_90"]
    if character.energy == 89:
        return graphics["en_89"]
    if character.energy == 88:
        return graphics["en_88"]
    if character.energy == 87:
        return graphics["en_87"]
    if character.energy == 86:
        return graphics["en_86"]
    if character.energy == 85:
        return graphics["en_85"]
    if character.energy == 84:
        return graphics["en_84"]
    if character.energy == 83:
        return graphics["en_83"]
    if character.energy == 82:
        return graphics["en_82"]
    if character.energy == 81:
        return graphics["en_81"]
    if character.energy == 80:
        return graphics["en_80"]
    if character.energy == 79:
        return graphics["en_79"]
    if character.energy == 78:
        return graphics["en_78"]
    if character.energy == 77:
        return graphics["en_77"]
    if character.energy == 76:
        return graphics["en_76"]
    if character.energy == 75:
        return graphics["en_75"]
    if character.energy == 74:
        return graphics["en_74"]
    if character.energy == 73:
        return graphics["en_73"]
    if character.energy == 72:
        return graphics["en_72"]
    if character.energy == 71:
        return graphics["en_71"]
    if character.energy == 70:
        return graphics["en_70"]
    if character.energy == 69:
        return graphics["en_69"]
    if character.energy == 68:
        return graphics["en_68"]
    if character.energy == 67:
        return graphics["en_67"]
    if character.energy == 66:
        return graphics["en_66"]
    if character.energy == 65:
        return graphics["en_65"]
    if character.energy == 64:
        return graphics["en_64"]
    if character.energy == 63:
        return graphics["en_63"]
    if character.energy == 62:
        return graphics["en_62"]
    if character.energy == 61:
        return graphics["en_61"]
    if character.energy == 60:
        return graphics["en_60"]
    if character.energy == 59:
        return graphics["en_59"]
    if character.energy == 58:
        return graphics["en_58"]
    if character.energy == 57:
        return graphics["en_57"]
    if character.energy == 56:
        return graphics["en_56"]
    if character.energy == 55:
        return graphics["en_55"]
    if character.energy == 54:
        return graphics["en_54"]
    if character.energy == 53:
        return graphics["en_53"]
    if character.energy == 52:
        return graphics["en_52"]
    if character.energy == 51:
        return graphics["en_51"]
    if character.energy == 50:
        return graphics["en_50"]
    if character.energy == 49:
        return graphics["en_49"]
    if character.energy == 48:
        return graphics["en_48"]
    if character.energy == 47:
        return graphics["en_47"]
    if character.energy == 46:
        return graphics["en_46"]
    if character.energy == 45:
        return graphics["en_45"]
    if character.energy == 44:
        return graphics["en_44"]
    if character.energy == 43:
        return graphics["en_43"]
    if character.energy == 42:
        return graphics["en_42"]
    if character.energy == 41:
        return graphics["en_41"]
    if character.energy == 40:
        return graphics["en_40"]
    if character.energy == 39:
        return graphics["en_39"]
    if character.energy == 38:
        return graphics["en_38"]
    if character.energy == 37:
        return graphics["en_37"]
    if character.energy == 36:
        return graphics["en_36"]
    if character.energy == 35:
        return graphics["en_35"]
    if character.energy == 34:
        return graphics["en_34"]
    if character.energy == 33:
        return graphics["en_33"]
    if character.energy == 32:
        return graphics["en_32"]
    if character.energy == 31:
        return graphics["en_31"]
    if character.energy == 30:
        return graphics["en_30"]
    if character.energy == 29:
        return graphics["en_29"]
    if character.energy == 28:
        return graphics["en_28"]
    if character.energy == 27:
        return graphics["en_27"]
    if character.energy == 26:
        return graphics["en_26"]
    if character.energy == 25:
        return graphics["en_25"]
    if character.energy == 24:
        return graphics["en_24"]
    if character.energy == 23:
        return graphics["en_23"]
    if character.energy == 22:
        return graphics["en_22"]
    if character.energy == 21:
        return graphics["en_21"]
    if character.energy == 20:
        return graphics["en_20"]
    if character.energy == 19:
        return graphics["en_19"]
    if character.energy == 18:
        return graphics["en_18"]
    if character.energy == 17:
        return graphics["en_17"]
    if character.energy == 16:
        return graphics["en_16"]
    if character.energy == 15:
        return graphics["en_15"]
    if character.energy == 14:
        return graphics["en_14"]
    if character.energy == 13:
        return graphics["en_13"]
    if character.energy == 12:
        return graphics["en_12"]
    if character.energy == 11:
        return graphics["en_11"]
    if character.energy == 10:
        return graphics["en_10"]
    if character.energy == 9:
        return graphics["en_9"]
    if character.energy == 8:
        return graphics["en_8"]
    if character.energy == 7:
        return graphics["en_7"]
    if character.energy == 6:
        return graphics["en_6"]
    if character.energy == 5:
        return graphics["en_5"]
    if character.energy == 4:
        return graphics["en_4"]
    if character.energy == 3:
        return graphics["en_3"]
    if character.energy == 2:
        return graphics["en_2"]
    if character.energy == 1:
        return graphics["en_1"]
    if character.energy == 0:
        return graphics["en_0"]


def xp_bar_update(character, graphics):
    if character.experience >= 100:
        return graphics["xp_100"]
    if character.experience == 99:
        return graphics["xp_99"]
    if character.experience == 98:
        return graphics["xp_98"]
    if character.experience == 97:
        return graphics["xp_97"]
    if character.experience == 96:
        return graphics["xp_96"]
    if character.experience == 95:
        return graphics["xp_95"]
    if character.experience == 94:
        return graphics["xp_94"]
    if character.experience == 93:
        return graphics["xp_93"]
    if character.experience == 92:
        return graphics["xp_92"]
    if character.experience == 91:
        return graphics["xp_91"]
    if character.experience == 90:
        return graphics["xp_90"]
    if character.experience == 89:
        return graphics["xp_89"]
    if character.experience == 88:
        return graphics["xp_88"]
    if character.experience == 87:
        return graphics["xp_87"]
    if character.experience == 86:
        return graphics["xp_86"]
    if character.experience == 85:
        return graphics["xp_85"]
    if character.experience == 84:
        return graphics["xp_84"]
    if character.experience == 83:
        return graphics["xp_83"]
    if character.experience == 82:
        return graphics["xp_82"]
    if character.experience == 81:
        return graphics["xp_81"]
    if character.experience == 80:
        return graphics["xp_80"]
    if character.experience == 79:
        return graphics["xp_79"]
    if character.experience == 78:
        return graphics["xp_78"]
    if character.experience == 77:
        return graphics["xp_77"]
    if character.experience == 76:
        return graphics["xp_76"]
    if character.experience == 75:
        return graphics["xp_75"]
    if character.experience == 74:
        return graphics["xp_74"]
    if character.experience == 73:
        return graphics["xp_73"]
    if character.experience == 72:
        return graphics["xp_72"]
    if character.experience == 71:
        return graphics["xp_71"]
    if character.experience == 70:
        return graphics["xp_70"]
    if character.experience == 69:
        return graphics["xp_69"]
    if character.experience == 68:
        return graphics["xp_68"]
    if character.experience == 67:
        return graphics["xp_67"]
    if character.experience == 66:
        return graphics["xp_66"]
    if character.experience == 65:
        return graphics["xp_65"]
    if character.experience == 64:
        return graphics["xp_64"]
    if character.experience == 63:
        return graphics["xp_63"]
    if character.experience == 62:
        return graphics["xp_62"]
    if character.experience == 61:
        return graphics["xp_61"]
    if character.experience == 60:
        return graphics["xp_60"]
    if character.experience == 59:
        return graphics["xp_59"]
    if character.experience == 58:
        return graphics["xp_58"]
    if character.experience == 57:
        return graphics["xp_57"]
    if character.experience == 56:
        return graphics["xp_56"]
    if character.experience == 55:
        return graphics["xp_55"]
    if character.experience == 54:
        return graphics["xp_54"]
    if character.experience == 53:
        return graphics["xp_53"]
    if character.experience == 52:
        return graphics["xp_52"]
    if character.experience == 51:
        return graphics["xp_51"]
    if character.experience == 50:
        return graphics["xp_50"]
    if character.experience == 49:
        return graphics["xp_49"]
    if character.experience == 48:
        return graphics["xp_48"]
    if character.experience == 47:
        return graphics["xp_47"]
    if character.experience == 46:
        return graphics["xp_46"]
    if character.experience == 45:
        return graphics["xp_45"]
    if character.experience == 44:
        return graphics["xp_44"]
    if character.experience == 43:
        return graphics["xp_43"]
    if character.experience == 42:
        return graphics["xp_42"]
    if character.experience == 41:
        return graphics["xp_41"]
    if character.experience == 40:
        return graphics["xp_40"]
    if character.experience == 39:
        return graphics["xp_39"]
    if character.experience == 38:
        return graphics["xp_38"]
    if character.experience == 37:
        return graphics["xp_37"]
    if character.experience == 36:
        return graphics["xp_36"]
    if character.experience == 35:
        return graphics["xp_35"]
    if character.experience == 34:
        return graphics["xp_34"]
    if character.experience == 33:
        return graphics["xp_33"]
    if character.experience == 32:
        return graphics["xp_32"]
    if character.experience == 31:
        return graphics["xp_31"]
    if character.experience == 30:
        return graphics["xp_30"]
    if character.experience == 29:
        return graphics["xp_29"]
    if character.experience == 28:
        return graphics["xp_28"]
    if character.experience == 27:
        return graphics["xp_27"]
    if character.experience == 26:
        return graphics["xp_26"]
    if character.experience == 25:
        return graphics["xp_25"]
    if character.experience == 24:
        return graphics["xp_24"]
    if character.experience == 23:
        return graphics["xp_23"]
    if character.experience == 22:
        return graphics["xp_22"]
    if character.experience == 21:
        return graphics["xp_21"]
    if character.experience == 20:
        return graphics["xp_20"]
    if character.experience == 19:
        return graphics["xp_19"]
    if character.experience == 18:
        return graphics["xp_18"]
    if character.experience == 17:
        return graphics["xp_17"]
    if character.experience == 16:
        return graphics["xp_16"]
    if character.experience == 15:
        return graphics["xp_15"]
    if character.experience == 14:
        return graphics["xp_14"]
    if character.experience == 13:
        return graphics["xp_13"]
    if character.experience == 12:
        return graphics["xp_12"]
    if character.experience == 11:
        return graphics["xp_11"]
    if character.experience == 10:
        return graphics["xp_10"]
    if character.experience == 9:
        return graphics["xp_9"]
    if character.experience == 8:
        return graphics["xp_8"]
    if character.experience == 7:
        return graphics["xp_7"]
    if character.experience == 6:
        return graphics["xp_6"]
    if character.experience == 5:
        return graphics["xp_5"]
    if character.experience == 4:
        return graphics["xp_4"]
    if character.experience == 3:
        return graphics["xp_3"]
    if character.experience == 2:
        return graphics["xp_2"]
    if character.experience == 1:
        return graphics["xp_1"]
    if character.experience <= 0:
        return graphics["xp_0"]

    else:
        return graphics["xp_0"]
