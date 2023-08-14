# functions for drawing certain text and images on screen
# lists for blitting elements/items to the screen that are contained within lists

character_sheet_text = []
character_sheet_window = []
journal_text = []
journal_window = []
level_up_text = []
level_up_window = []
level_up_visual = []
quest_box = []
quest_complete_box = []
quest_accept_box = []
quest_box_fishing = []
quest_complete_box_fishing = []
quest_accept_box_fishing = []
player_equipment = []
player_items = []
item_info_window = []
buy_info_window = []
sell_info_window = []
loot_popup_container = []
loot_text_container = []
knowledge_academia_window = []
first_quest_window = []
rest_recover_window = []
outpost_window = []
first_item_window = []
game_guide_container = []
world_map_container = []
type_advantage_window = []
weapon_container = []
potion_window_container = []
pets_window_container = []
fish_window_container = []
flower_pop_up_window = []
fish_pop_up_window = []

flower_pop_up_window_text = []
fish_pop_up_window_text = []


# draws elements on screen that have been appended to list by below functions
def draw_it(screen):
    if len(character_sheet_window) > 0:
        for character_window in character_sheet_window:
            screen.blit(character_window.surf, character_window.rect)
    if len(character_sheet_text) > 0:
        for character_text in character_sheet_text:
            screen.blit(character_text[0], character_text[1])
    if len(journal_window) > 0:
        for journals_window in journal_window:
            screen.blit(journals_window.surf, journals_window.rect)
    if len(journal_text) > 0:
        for journals_text in journal_text:
            screen.blit(journals_text[0], journals_text[1])
    if len(level_up_window) > 0:
        for level_ups_window in level_up_window:
            screen.blit(level_ups_window.surf, level_ups_window.rect)
    if len(level_up_text) > 0:
        for level_text in level_up_text:
            screen.blit(level_text[0], level_text[1])
    if len(character_sheet_text) > 0:
        for characters_text in character_sheet_text:
            screen.blit(characters_text[0], characters_text[1])
    if len(quest_box) > 0:
        for quest_element in quest_box:
            screen.blit(quest_element.surf, quest_element.rect)
    if len(quest_complete_box) > 0:
        for quest_complete_element in quest_complete_box:
            screen.blit(quest_complete_element.surf, quest_complete_element.rect)
    if len(quest_box_fishing) > 0:
        for quest_element_fishing in quest_box_fishing:
            screen.blit(quest_element_fishing.surf, quest_element_fishing.rect)
    if len(quest_complete_box_fishing) > 0:
        for quest_complete_element_fishing in quest_complete_box_fishing:
            screen.blit(quest_complete_element_fishing.surf, quest_complete_element_fishing.rect)
    if len(quest_accept_box) > 0:
        for accept_element in quest_accept_box:
            screen.blit(accept_element.surf, accept_element.rect)
    if len(quest_accept_box_fishing) > 0:
        for accept_element_fishing in quest_accept_box_fishing:
            screen.blit(accept_element_fishing.surf, accept_element_fishing.rect)
    if len(player_equipment) > 0:
        for equipment_here in player_equipment:
            screen.blit(equipment_here.surf, equipment_here.rect)
    if len(player_items) > 0:
        for item_here in player_items:
            screen.blit(item_here.surf, item_here.rect)
    if len(item_info_window) > 0:
        for item_info in item_info_window:
            screen.blit(item_info.surf, item_info.rect)
    if len(buy_info_window) > 0:
        for buy_info in buy_info_window:
            screen.blit(buy_info.surf, buy_info.rect)
    if len(sell_info_window) > 0:
        for sell_info in sell_info_window:
            screen.blit(sell_info.surf, sell_info.rect)
    if len(knowledge_academia_window) > 0:
        for knowledge_window_notification in knowledge_academia_window:
            screen.blit(knowledge_window_notification.surf,
                        knowledge_window_notification.rect)
    if len(rest_recover_window) > 0:
        for rest_window in rest_recover_window:
            screen.blit(rest_window.surf, rest_window.rect)
    if len(first_quest_window) > 0:
        for quest_window in first_quest_window:
            screen.blit(quest_window.surf, quest_window.rect)
    if len(first_item_window) > 0:
        for item_window in first_item_window:
            screen.blit(item_window.surf, item_window.rect)
    if len(outpost_window) > 0:
        for outpost_item in outpost_window:
            screen.blit(outpost_item.surf, outpost_item.rect)
    if len(game_guide_container) > 0:
        for guide_overlay in game_guide_container:
            screen.blit(guide_overlay.surf, guide_overlay.rect)
    if len(world_map_container) > 0:
        for map_element in world_map_container:
            screen.blit(map_element.surf, map_element.rect)
    if len(type_advantage_window) > 0:
        for type_element in type_advantage_window:
            screen.blit(type_element.surf, type_element.rect)
    if len(weapon_container) > 0:
        if len(item_info_window) == 0 and len(sell_info_window) == 0:
            for weapon in weapon_container:
                screen.blit(weapon.surf, weapon.rect)
    if len(potion_window_container) > 0:
        for potion_element in potion_window_container:
            screen.blit(potion_element.surf, potion_element.rect)
    if len(pets_window_container) > 0:
        for pets_element in pets_window_container:
            screen.blit(pets_element.surf, pets_element.rect)
    if len(fish_window_container) > 0:
        for fish_element in fish_window_container:
            screen.blit(fish_element.surf, fish_element.rect)
    if len(flower_pop_up_window) > 0:
        for flower_element in flower_pop_up_window:
            screen.blit(flower_element.surf, flower_element.rect)
    if len(fish_pop_up_window) > 0:
        for f_element in fish_pop_up_window:
            screen.blit(f_element.surf, f_element.rect)
    if len(flower_pop_up_window_text) > 0:
        for flower_text in flower_pop_up_window_text:
            screen.blit(flower_text[0], flower_text[1])
    if len(fish_pop_up_window_text) > 0:
        for fish_text in fish_pop_up_window_text:
            screen.blit(fish_text[0], fish_text[1])


def draw_level_up(screen, in_over_world):
    if len(level_up_visual) > 0:
        for visuals in level_up_visual:
            if not in_over_world:
                if visuals.name != "level up visual":
                    screen.blit(visuals.surf, visuals.rect)
            else:
                screen.blit(visuals.surf, visuals.rect)


def weapon_draw(player, graphics, staff, sword, bow, npc_garan, weapon_select):
    if npc_garan.gift:
        if player.offense == 0:
            if len(weapon_container) > 3:
                weapon_container.clear()
            staff.update(staff.x_coordinate, staff.y_coordinate, graphics["staff_0"])
            sword.update(sword.x_coordinate, sword.y_coordinate, graphics["sword_0"])
            bow.update(bow.x_coordinate, bow.y_coordinate, graphics["bow_0"])
            weapon_container.append(staff)
            weapon_container.append(sword)
            weapon_container.append(bow)
        if player.offense == 1:
            if len(weapon_container) > 3:
                weapon_container.clear()
            staff.update(staff.x_coordinate, staff.y_coordinate, graphics["staff_1"])
            sword.update(sword.x_coordinate, sword.y_coordinate, graphics["sword_1"])
            bow.update(bow.x_coordinate, bow.y_coordinate, graphics["bow_1"])
            weapon_container.append(staff)
            weapon_container.append(sword)
            weapon_container.append(bow)
        if player.offense == 2:
            if len(weapon_container) > 3:
                weapon_container.clear()
            staff.update(staff.x_coordinate, staff.y_coordinate, graphics["staff_2"])
            sword.update(sword.x_coordinate, sword.y_coordinate, graphics["sword_2"])
            bow.update(bow.x_coordinate, bow.y_coordinate, graphics["bow_2"])
            weapon_container.append(staff)
            weapon_container.append(sword)
            weapon_container.append(bow)
        if player.offense == 3:
            if len(weapon_container) > 3:
                weapon_container.clear()
            staff.update(staff.x_coordinate, staff.y_coordinate, graphics["staff_3"])
            sword.update(sword.x_coordinate, sword.y_coordinate, graphics["sword_3"])
            bow.update(bow.x_coordinate, bow.y_coordinate, graphics["bow_3"])
            weapon_container.append(staff)
            weapon_container.append(sword)
            weapon_container.append(bow)
        if player.offense == 4:
            if len(weapon_container) > 3:
                weapon_container.clear()
            staff.update(staff.x_coordinate, staff.y_coordinate, graphics["staff_4"])
            sword.update(sword.x_coordinate, sword.y_coordinate, graphics["sword_4"])
            bow.update(bow.x_coordinate, bow.y_coordinate, graphics["bow_4"])
            weapon_container.append(staff)
            weapon_container.append(sword)
            weapon_container.append(bow)

        if player.role == "mage":
            weapon_select.update(1079, 284, graphics["weapon_select"])
        if player.role == "fighter":
            weapon_select.update(1154, 284, graphics["weapon_select"])
        if player.role == "scout":
            weapon_select.update(1229, 284, graphics["weapon_select"])

        if player.role != "":
            weapon_container.append(weapon_select)


def item_info_draw(inventory_item, info_items, item_info_button, graphic):
    if inventory_item:
        if inventory_item.name == "small health potion":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_health_pot_img"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["use_button_img"])
            item_info_window.append(item_info_button)
            return inventory_item
        if inventory_item.name == "small energy potion":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_energy_pot_img"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["use_button_img"])
            item_info_window.append(item_info_button)
            return inventory_item
        if inventory_item.name == "big health potion":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_big_health_pot_img"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["use_button_img"])
            item_info_window.append(item_info_button)
            return inventory_item
        if inventory_item.name == "big energy potion":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_big_energy_pot_img"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["use_button_img"])
            item_info_window.append(item_info_button)
            return inventory_item
        if inventory_item.name == "super potion":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_super_pot_img"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["use_button_img"])
            item_info_window.append(item_info_button)
            return inventory_item

        if inventory_item.name == "basic armor":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_basic_armor"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["equip_button_img"])
            item_info_window.append(item_info_button)
            return inventory_item
        if inventory_item.name == "forged armor":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_forged_armor"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["equip_button_img"])
            item_info_window.append(item_info_button)
            return inventory_item
        if inventory_item.name == "mythical armor":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_mythical_armor"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["equip_button_img"])
            item_info_window.append(item_info_button)
            return inventory_item
        if inventory_item.name == "legendary armor":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_legendary_armor"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["equip_button_img"])
            item_info_window.append(item_info_button)
            return inventory_item

        if inventory_item.name == "shiny rock":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_shiny_rock_img"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["ok_button_img"])
            item_info_window.append(item_info_button)
        if inventory_item.name == "bone dust":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_bone_dust_img"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["ok_button_img"])
            item_info_window.append(item_info_button)
        if inventory_item.name == "boss key" or inventory_item.name == "ramps key":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_boss_key_img"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["ok_button_img"])
            item_info_window.append(item_info_button)
        if inventory_item.name == "power gloves":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_gloves"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["equip_button_img"])
            item_info_window.append(item_info_button)
            return inventory_item
        if inventory_item.name == "cracked ember":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_ember"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["ok_button_img"])
            item_info_window.append(item_info_button)
        if inventory_item.name == "broken band":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_band"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["ok_button_img"])
            item_info_window.append(item_info_button)
        if inventory_item.name == "pet seed":
            if inventory_item.level == 2:
                info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_creature_seed_ready"])
            else:
                info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_creature_seed"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["ok_button_img"])
            item_info_window.append(item_info_button)
        if inventory_item.type == "whistle":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_whistle"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["use_button_img"])
            item_info_window.append(item_info_button)
            return inventory_item
        if inventory_item.name == "dried fins":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_dread_fins"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["ok_button_img"])
            item_info_window.append(item_info_button)
        if inventory_item.name == "oscura pluma":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_oscura_pluma"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["ok_button_img"])
            item_info_window.append(item_info_button)
        if inventory_item.name == "chroma boots":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_chroma_boots"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["equip_button_img"])
            item_info_window.append(item_info_button)
            return inventory_item
        if inventory_item.name == "pet cookie":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_cookie_img"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["use_button_img"])
            item_info_window.append(item_info_button)
            return inventory_item
        if inventory_item.name == "pet candy":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_candy_img"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["use_button_img"])
            item_info_window.append(item_info_button)
            return inventory_item
        if inventory_item.name == "pet tart":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_tart_img"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["use_button_img"])
            item_info_window.append(item_info_button)
            return inventory_item
        if inventory_item.name == "bone shard":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_bone_shard"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["ok_button_img"])
            item_info_window.append(item_info_button)
            return inventory_item
        if inventory_item.name == "prism":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_prism"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["ok_button_img"])
            item_info_window.append(item_info_button)
            return inventory_item
        if inventory_item.name == "casing":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_casing"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["ok_button_img"])
            item_info_window.append(item_info_button)
            return inventory_item
        if inventory_item.name == "smelted casing":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_smelted_casing"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["ok_button_img"])
            item_info_window.append(item_info_button)
            return inventory_item
        if inventory_item.name == "enchanted casing":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_enchanted_casing"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["ok_button_img"])
            item_info_window.append(item_info_button)
            return inventory_item
        if inventory_item.name == "seldon firework":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_seldon_firework"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["use_button_img"])
            item_info_window.append(item_info_button)
            return inventory_item
        if inventory_item.name == "korlok firework":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_korlok_firework"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["use_button_img"])
            item_info_window.append(item_info_button)
            return inventory_item
        if inventory_item.name == "eldream firework":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_eldream_firework"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["use_button_img"])
            item_info_window.append(item_info_button)
            return inventory_item
        if inventory_item.name == "seldon bait":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_seldon_bait"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["ok_button_img"])
            item_info_window.append(item_info_button)
            return inventory_item
        if inventory_item.name == "korlok bait":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_korlok_bait"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["ok_button_img"])
            item_info_window.append(item_info_button)
            return inventory_item
        if inventory_item.name == "eldream bait":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_eldream_bait"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["ok_button_img"])
            item_info_window.append(item_info_button)
            return inventory_item
        if inventory_item.name == "mage book":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_mage_book"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["use_button_img"])
            item_info_window.append(item_info_button)
            return inventory_item
        if inventory_item.name == "fighter book":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_fighter_book"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["use_button_img"])
            item_info_window.append(item_info_button)
            return inventory_item
        if inventory_item.name == "scout book":
            info_items.update(info_items.x_coordinate, info_items.y_coordinate, graphic["info_scout_book"])
            item_info_window.append(info_items)
            item_info_button.update(item_info_button.x_coordinate, item_info_button.y_coordinate,
                                    graphic["use_button_img"])
            item_info_window.append(item_info_button)
            return inventory_item


def buy_info_draw(buy_item, buy_items, yes_button, graphic):
    if buy_item:
        if buy_item.name == "small health potion":
            buy_items.update(buy_items.x_coordinate, buy_items.y_coordinate, graphic["b_health_pot_img"])
            buy_info_window.append(buy_items)
            yes_button.update(900, 308, graphic["yes_button_img"])
            buy_info_window.append(yes_button)
            return buy_item
        if buy_item.name == "small energy potion":
            buy_items.update(buy_items.x_coordinate, buy_items.y_coordinate, graphic["b_energy_pot_img"])
            buy_info_window.append(buy_items)
            yes_button.update(900, 308, graphic["yes_button_img"])
            buy_info_window.append(yes_button)
            return buy_item
        if buy_item.name == "basic armor":
            buy_items.update(buy_items.x_coordinate, buy_items.y_coordinate, graphic["b_basic_armor"])
            buy_info_window.append(buy_items)
            yes_button.update(900, 308, graphic["yes_button_img"])
            buy_info_window.append(yes_button)
            return buy_item
        if buy_item.name == "forged armor":
            buy_items.update(buy_items.x_coordinate, buy_items.y_coordinate, graphic["b_forged_armor"])
            buy_info_window.append(buy_items)
            yes_button.update(900, 308, graphic["yes_button_img"])
            buy_info_window.append(yes_button)
            return buy_item
        if buy_item.name == "mythical armor":
            buy_items.update(buy_items.x_coordinate, buy_items.y_coordinate, graphic["b_mythical_armor"])
            buy_info_window.append(buy_items)
            yes_button.update(900, 308, graphic["yes_button_img"])
            buy_info_window.append(yes_button)
            return buy_item
        if buy_item.name == "pet cookie":
            buy_items.update(buy_items.x_coordinate, buy_items.y_coordinate, graphic["b_cookie_img"])
            buy_info_window.append(buy_items)
            yes_button.update(900, 308, graphic["yes_button_img"])
            buy_info_window.append(yes_button)
            return buy_item
        if buy_item.name == "pet candy":
            buy_items.update(buy_items.x_coordinate, buy_items.y_coordinate, graphic["b_candy_img"])
            buy_info_window.append(buy_items)
            yes_button.update(900, 308, graphic["yes_button_img"])
            buy_info_window.append(yes_button)
            return buy_item
        if buy_item.name == "pet tart":
            buy_items.update(buy_items.x_coordinate, buy_items.y_coordinate, graphic["b_tart_img"])
            buy_info_window.append(buy_items)
            yes_button.update(900, 308, graphic["yes_button_img"])
            buy_info_window.append(yes_button)
            return buy_item
        if buy_item.name == "seldon firework":
            buy_items.update(buy_items.x_coordinate, buy_items.y_coordinate, graphic["b_seldon_firework"])
            buy_info_window.append(buy_items)
            yes_button.update(900, 308, graphic["yes_button_img"])
            buy_info_window.append(yes_button)
            return buy_item
        if buy_item.name == "korlok firework":
            buy_items.update(buy_items.x_coordinate, buy_items.y_coordinate, graphic["b_korlok_firework"])
            buy_info_window.append(buy_items)
            yes_button.update(900, 308, graphic["yes_button_img"])
            buy_info_window.append(yes_button)
            return buy_item
        if buy_item.name == "eldream firework":
            buy_items.update(buy_items.x_coordinate, buy_items.y_coordinate, graphic["b_eldream_firework"])
            buy_info_window.append(buy_items)
            yes_button.update(900, 308, graphic["yes_button_img"])
            buy_info_window.append(yes_button)
            return buy_item
        if buy_item.name == "seldon bait":
            buy_items.update(buy_items.x_coordinate, buy_items.y_coordinate, graphic["b_seldon_bait"])
            buy_info_window.append(buy_items)
            yes_button.update(900, 308, graphic["yes_button_img"])
            buy_info_window.append(yes_button)
            return buy_item
        if buy_item.name == "korlok bait":
            buy_items.update(buy_items.x_coordinate, buy_items.y_coordinate, graphic["b_korlok_bait"])
            buy_info_window.append(buy_items)
            yes_button.update(900, 308, graphic["yes_button_img"])
            buy_info_window.append(yes_button)
            return buy_item
        if buy_item.name == "eldream bait":
            buy_items.update(buy_items.x_coordinate, buy_items.y_coordinate, graphic["b_eldream_bait"])
            buy_info_window.append(buy_items)
            yes_button.update(900, 308, graphic["yes_button_img"])
            buy_info_window.append(yes_button)
            return buy_item


def sell_info_draw(sell_item, sell_items, yes_button, graphic):
    if sell_item:
        if sell_item.name == "small health potion":
            sell_items.update(sell_items.x_coordinate, sell_items.y_coordinate, graphic["s_health_pot_img"])
            sell_info_window.append(sell_items)
            yes_button.update(1153, 345, graphic["yes_button_img"])
            sell_info_window.append(yes_button)
            return sell_item
        if sell_item.name == "small energy potion":
            sell_items.update(sell_items.x_coordinate, sell_items.y_coordinate, graphic["s_energy_pot_img"])
            sell_info_window.append(sell_items)
            yes_button.update(1153, 345, graphic["yes_button_img"])
            sell_info_window.append(yes_button)
            return sell_item
        if sell_item.name == "basic armor":
            sell_items.update(sell_items.x_coordinate, sell_items.y_coordinate, graphic["s_basic_armor"])
            sell_info_window.append(sell_items)
            yes_button.update(1153, 345, graphic["yes_button_img"])
            sell_info_window.append(yes_button)
            return sell_item
        if sell_item.name == "forged armor":
            sell_items.update(sell_items.x_coordinate, sell_items.y_coordinate, graphic["s_forged_armor"])
            sell_info_window.append(sell_items)
            yes_button.update(1153, 345, graphic["yes_button_img"])
            sell_info_window.append(yes_button)
            return sell_item
        if sell_item.name == "mythical armor":
            sell_items.update(sell_items.x_coordinate, sell_items.y_coordinate, graphic["s_mythical_armor"])
            sell_info_window.append(sell_items)
            yes_button.update(1153, 345, graphic["yes_button_img"])
            sell_info_window.append(yes_button)
            return sell_item
        if sell_item.name == "shiny rock":
            sell_items.update(sell_items.x_coordinate, sell_items.y_coordinate, graphic["s_shiny_rock_img"])
            sell_info_window.append(sell_items)
            yes_button.update(1153, 345, graphic["yes_button_img"])
            sell_info_window.append(yes_button)
            return sell_item
        if sell_item.name == "bone dust":
            sell_items.update(sell_items.x_coordinate, sell_items.y_coordinate, graphic["s_bone_dust_img"])
            sell_info_window.append(sell_items)
            yes_button.update(1153, 345, graphic["yes_button_img"])
            sell_info_window.append(yes_button)
            return sell_item
        if sell_item.name == "cracked ember":
            sell_items.update(sell_items.x_coordinate, sell_items.y_coordinate, graphic["s_ember_img"])
            sell_info_window.append(sell_items)
            yes_button.update(1153, 345, graphic["yes_button_img"])
            sell_info_window.append(yes_button)
            return sell_item
        if sell_item.name == "broken band":
            sell_items.update(sell_items.x_coordinate, sell_items.y_coordinate, graphic["s_band_img"])
            sell_info_window.append(sell_items)
            yes_button.update(1153, 345, graphic["yes_button_img"])
            sell_info_window.append(yes_button)
            return sell_item
        if sell_item.name == "dried fins":
            sell_items.update(sell_items.x_coordinate, sell_items.y_coordinate, graphic["s_fins_img"])
            sell_info_window.append(sell_items)
            yes_button.update(1153, 345, graphic["yes_button_img"])
            sell_info_window.append(yes_button)
            return sell_item
        if sell_item.name == "oscura pluma":
            sell_items.update(sell_items.x_coordinate, sell_items.y_coordinate, graphic["s_pluma_img"])
            sell_info_window.append(sell_items)
            yes_button.update(1153, 345, graphic["yes_button_img"])
            sell_info_window.append(yes_button)
            return sell_item
        if sell_item.name == "pet cookie":
            sell_items.update(sell_items.x_coordinate, sell_items.y_coordinate, graphic["s_cookie_img"])
            sell_info_window.append(sell_items)
            yes_button.update(1153, 345, graphic["yes_button_img"])
            sell_info_window.append(yes_button)
            return sell_item
        if sell_item.name == "pet candy":
            sell_items.update(sell_items.x_coordinate, sell_items.y_coordinate, graphic["s_candy_img"])
            sell_info_window.append(sell_items)
            yes_button.update(1153, 345, graphic["yes_button_img"])
            sell_info_window.append(yes_button)
            return sell_item
        if sell_item.name == "pet tart":
            sell_items.update(sell_items.x_coordinate, sell_items.y_coordinate, graphic["s_tart_img"])
            sell_info_window.append(sell_items)
            yes_button.update(1153, 345, graphic["yes_button_img"])
            sell_info_window.append(yes_button)
            return sell_item
        if sell_item.name == "bone shard":
            sell_items.update(sell_items.x_coordinate, sell_items.y_coordinate, graphic["s_bone_shard"])
            sell_info_window.append(sell_items)
            yes_button.update(1153, 345, graphic["yes_button_img"])
            sell_info_window.append(yes_button)
            return sell_item
        if sell_item.name == "seldon firework":
            sell_items.update(sell_items.x_coordinate, sell_items.y_coordinate, graphic["s_seldon_firework"])
            sell_info_window.append(sell_items)
            yes_button.update(1153, 345, graphic["yes_button_img"])
            sell_info_window.append(yes_button)
            return sell_item
        if sell_item.name == "korlok firework":
            sell_items.update(sell_items.x_coordinate, sell_items.y_coordinate, graphic["s_korlok_firework"])
            sell_info_window.append(sell_items)
            yes_button.update(1153, 345, graphic["yes_button_img"])
            sell_info_window.append(yes_button)
            return sell_item
        if sell_item.name == "eldream firework":
            sell_items.update(sell_items.x_coordinate, sell_items.y_coordinate, graphic["s_eldream_firework"])
            sell_info_window.append(sell_items)
            yes_button.update(1153, 345, graphic["yes_button_img"])
            sell_info_window.append(yes_button)
            return sell_item
        if sell_item.name == "seldon bait":
            sell_items.update(sell_items.x_coordinate, sell_items.y_coordinate, graphic["s_seldon_bait"])
            sell_info_window.append(sell_items)
            yes_button.update(1153, 345, graphic["yes_button_img"])
            sell_info_window.append(yes_button)
            return sell_item
        if sell_item.name == "korlok bait":
            sell_items.update(sell_items.x_coordinate, sell_items.y_coordinate, graphic["s_korlok_bait"])
            sell_info_window.append(sell_items)
            yes_button.update(1153, 345, graphic["yes_button_img"])
            sell_info_window.append(yes_button)
            return sell_item
        if sell_item.name == "eldream bait":
            sell_items.update(sell_items.x_coordinate, sell_items.y_coordinate, graphic["s_eldream_bait"])
            sell_info_window.append(sell_items)
            yes_button.update(1153, 345, graphic["yes_button_img"])
            sell_info_window.append(yes_button)
            return sell_item


def text_info_draw(screen, player, font, info_text_1, info_text_2, info_text_3, info_text_4, in_over_world,
                   basic_fish_counter, better_fish_counter, even_better_fish_counter, best_fish_counter):
    # get current player rupee count and create surf and rectangle to blit to screen------------------------------------
    text_rupee_surf = font.render(str(player.rupees), True, "black", "light green")
    text_rupee_rect = text_rupee_surf.get_rect()
    text_rupee_rect.center = (1120, 693)
    screen.blit(text_rupee_surf, text_rupee_rect)
    if len(flower_pop_up_window) > 0:
        # seldon flowers -----------------------------------------------------------------------------------------------
        flower_seldon_surf = font.render(str(player.flowers_amuna), True, "black", "light yellow")
        flower_seldon_rect = flower_seldon_surf.get_rect()
        flower_seldon_rect.center = (1114, 642)
        flower_pop_up_window_text.append((flower_seldon_surf, flower_seldon_rect))
        # eldream flowers ----------------------------------------------------------------------------------------------
        flower_eldream_surf = font.render(str(player.flowers_sorae), True, "black", "light yellow")
        flower_eldream_rect = flower_eldream_surf.get_rect()
        flower_eldream_rect.center = (1229, 642)
        flower_pop_up_window_text.append((flower_eldream_surf, flower_eldream_rect))
    if len(fish_pop_up_window) > 0:
        # basic fish ---------------------------------------------------------------------------------------------------
        basic_fish_surf = font.render(str(basic_fish_counter), True, "black", "light yellow")
        basic_fish_rect = basic_fish_surf.get_rect()
        basic_fish_rect.center = (1088, 642)
        fish_pop_up_window_text.append((basic_fish_surf, basic_fish_rect))
        # better fish --------------------------------------------------------------------------------------------------
        better_fish_surf = font.render(str(better_fish_counter), True, "black", "light yellow")
        better_fish_rect = better_fish_surf.get_rect()
        better_fish_rect.center = (1147, 642)
        fish_pop_up_window_text.append((better_fish_surf, better_fish_rect))
        # even better fish ---------------------------------------------------------------------------------------------
        even_better_fish_surf = font.render(str(even_better_fish_counter), True, "black", "light yellow")
        even_better_fish_rect = even_better_fish_surf.get_rect()
        even_better_fish_rect.center = (1205, 642)
        fish_pop_up_window_text.append((even_better_fish_surf, even_better_fish_rect))
        # best fish ----------------------------------------------------------------------------------------------------
        best_fish_surf = font.render(str(best_fish_counter), True, "black", "light yellow")
        best_fish_rect = best_fish_surf.get_rect()
        best_fish_rect.center = (1263, 642)
        fish_pop_up_window_text.append((best_fish_surf, best_fish_rect))
    # get current player level and create surf and rectangle to blit to screen------------------------------------------
    text_level_surf = font.render(str(player.level), True, "black", "light yellow")
    text_level_rect = text_level_surf.get_rect()
    text_level_rect.center = (1108, 359)
    if len(item_info_window) == 0 and len(sell_info_window) == 0:
        screen.blit(text_level_surf, text_level_rect)
    # current player location for UI overlay ---------------------------------------------------------------------------
    if in_over_world:
        if player.current_zone == "seldon":
            text_location = font.render(str("Seldon"), True, "black", "light yellow")
        if player.current_zone == "stardust":
            text_location = font.render(str("Stardust"), True, "black", "light yellow")
        if player.current_zone == "rohir":
            text_location = font.render(str("Rohir"), True, "black", "light yellow")
        if player.current_zone == "reservoir a" or player.current_zone == "reservoir b" or \
                player.current_zone == "reservoir c":
            text_location = font.render(str("Reservoir"), True, "black", "light yellow")
        if player.current_zone == "korlok" or player.current_zone == "fishing hut":
            text_location = font.render(str("Korlok"), True, "black", "light yellow")
        if player.current_zone == "mines":
            text_location = font.render(str("Mines"), True, "black", "light yellow")
        if player.current_zone == "forge":
            text_location = font.render(str("Forge"), True, "black", "light yellow")
        if player.current_zone == "terra trail":
            text_location = font.render(str("Terra Trail"), True, "black", "light yellow")
        if player.current_zone == "eldream":
            text_location = font.render(str("Eldream"), True, "black", "light yellow")
        if (player.current_zone == "ectrenos" or player.current_zone == "ectrenos left" or
                player.current_zone == "ectrenos right" or player.current_zone == "ectrenos alcove" or
                player.current_zone == "ectrenos front" or player.current_zone == "altar" or
                player.current_zone == "fishing alcove"):
            text_location = font.render(str("Ectrenos"), True, "black", "light yellow")
        if player.current_zone == "marrow" or player.current_zone == "marrow entrance" or \
                player.current_zone == "marrow tower east" or player.current_zone == "marrow tower west" or \
                player.current_zone == "marrow ramps east" or player.current_zone == "marrow ramps west" or \
                player.current_zone == "marrow ramps east end" or player.current_zone == "marrow ramps west end" \
                or player.current_zone == "sub marrow":
            text_location = font.render(str("Marrow"), True, "black", "light yellow")
        text_location_rect = text_location.get_rect()
        text_location_rect.midleft = (935, 29)
        if player.x_coordinate > 730 and player.y_coordinate < 125:
            text_location.set_alpha(50)
        if len(game_guide_container) == 0:
            screen.blit(text_location, text_location_rect)
    # current info text for message box in lower left corner of screen, first line--------------------------------------
    text_info_surf_1 = font.render(info_text_1, True, "black", "light yellow")
    text_info_rect_1 = text_info_surf_1.get_rect()
    text_info_rect_1.midleft = (30, 630)
    if player.x_coordinate < 335 and 600 < player.y_coordinate:
        text_info_surf_1.set_alpha(50)
    screen.blit(text_info_surf_1, text_info_rect_1)
    # current info text for message box in lower left corner of screen, second line-------------------------------------
    text_info_surf_2 = font.render(info_text_2, True, "black", "light yellow")
    text_info_rect_2 = text_info_surf_2.get_rect()
    text_info_rect_2.midleft = (30, 650)
    if player.x_coordinate < 335 and 600 < player.y_coordinate:
        text_info_surf_2.set_alpha(50)
    screen.blit(text_info_surf_2, text_info_rect_2)
    # current info text for message box in lower left corner of screen, third line--------------------------------------
    text_info_surf_3 = font.render(info_text_3, True, "black", "light yellow")
    text_info_rect_3 = text_info_surf_3.get_rect()
    text_info_rect_3.midleft = (30, 670)
    screen.blit(text_info_surf_3, text_info_rect_3)
    # current info text for message box in lower left corner of screen, fourth line-------------------------------------
    text_info_surf_4 = font.render(info_text_4, True, "black", "light yellow")
    text_info_rect_4 = text_info_surf_4.get_rect()
    text_info_rect_4.midleft = (30, 690)
    screen.blit(text_info_surf_4, text_info_rect_4)

    if len(item_info_window) == 0 and len(buy_info_window) == 0 and len(sell_info_window) == 0:
        if player.star_power > 4:
            if player.star_power == 5:
                star_extra_surf = font.render(str("+1"), True, "black", "light yellow")
            if player.star_power == 6:
                star_extra_surf = font.render(str("+2"), True, "black", "light yellow")
            if player.star_power == 7:
                star_extra_surf = font.render(str("+3"), True, "black", "light yellow")
            if player.star_power == 8:
                star_extra_surf = font.render(str("+4"), True, "black", "light yellow")

            if player.star_power == 9:
                star_extra_surf = font.render(str("+5"), True, "black", "light yellow")
            if player.star_power == 10:
                star_extra_surf = font.render(str("+6"), True, "black", "light yellow")
            if player.star_power == 11:
                star_extra_surf = font.render(str("+7"), True, "black", "light yellow")
            if player.star_power == 12:
                star_extra_surf = font.render(str("+8"), True, "black", "light yellow")

            star_extra_rect = star_extra_surf.get_rect()
            star_extra_rect.midleft = (1240, 360)
            screen.blit(star_extra_surf, star_extra_rect)


def character_sheet_info_draw(character_sheet, player, font, draw_condition):
    if not draw_condition:
        character_sheet_text.clear()
        character_sheet_window.clear()
    else:
        text_name_surf = font.render(str(player.name), True, "black", "light yellow")
        text_name_rect = text_name_surf.get_rect()
        text_name_rect.midleft = (595, 152)
        text_race_surf = font.render(str(player.race), True, "black", "light yellow")
        text_race_rect = text_race_surf.get_rect()
        text_race_rect.midleft = (592, 190)
        text_rolled_surf = font.render(str(player.role), True, "black", "light yellow")
        text_rolled_rect = text_rolled_surf.get_rect()
        text_rolled_rect.midleft = (588, 228)
        text_health_surf = font.render(str(player.health), True, "black", "light yellow")
        text_health_rect = text_health_surf.get_rect()
        text_health_rect.midleft = (855, 151)
        text_energy_surf = font.render(str(player.energy), True, "black", "light yellow")
        text_energy_rect = text_energy_surf.get_rect()
        text_energy_rect.midleft = (855, 189)
        text_experience_surf = font.render(str(player.experience), True, "black", "light yellow")
        text_experience_rect = text_experience_surf.get_rect()
        text_experience_rect.midleft = (890, 229)
        text_mage_surf = font.render(str(player.knowledge["mage"]), True, "black", "light yellow")
        text_mage_rect = text_mage_surf.get_rect()
        text_mage_rect.midleft = (680, 310)
        text_fighter_surf = font.render(str(player.knowledge["fighter"]), True, "black", "light yellow")
        text_fighter_rect = text_fighter_surf.get_rect()
        text_fighter_rect.midleft = (688, 348)
        text_scout_surf = font.render(str(player.knowledge["scout"]), True, "black", "light yellow")
        text_scout_rect = text_scout_surf.get_rect()
        text_scout_rect.midleft = (680, 385)
        text_amuna_surf = font.render(str(player.reputation["amuna"]), True, "black", "light yellow")
        text_amuna_rect = text_amuna_surf.get_rect()
        text_amuna_rect.midleft = (940, 310)
        text_nuldar_surf = font.render(str(player.reputation["nuldar"]), True, "black", "light yellow")
        text_nuldar_rect = text_nuldar_surf.get_rect()
        text_nuldar_rect.midleft = (940, 348)
        text_sorae_surf = font.render(str(player.reputation["sorae"]), True, "black", "light yellow")
        text_sorae_rect = text_sorae_surf.get_rect()
        text_sorae_rect.midleft = (935, 385)
        text_mage_skills_surf = font.render("[ " + str(player.skills_mage["skill 2"]) + " ] " +
                                            "[ " + str(player.skills_mage["skill 3"]) + " ] " +
                                            "[ " + str(player.skills_mage["skill 4"]) + " ] ",
                                            True, "black", "light yellow")
        text_mage_skills_rect = text_mage_skills_surf.get_rect()
        text_mage_skills_rect.midleft = (650, 506)
        text_fighter_skills_surf = font.render("[ " + str(player.skills_fighter["skill 2"]) + " ] " +
                                               "[ " + str(player.skills_fighter["skill 3"]) + " ] " +
                                               "[ " + str(player.skills_fighter["skill 4"]) + " ] ",
                                               True, "black", "light yellow")
        text_fighter_skills_rect = text_fighter_skills_surf.get_rect()
        text_fighter_skills_rect.midleft = (650, 543)
        text_scout_skills_surf = font.render("[ " + str(player.skills_scout["skill 2"]) + " ] " +
                                             "[ " + str(player.skills_scout["skill 3"]) + " ] " +
                                             "[ " + str(player.skills_scout["skill 4"]) + " ] ",
                                             True, "black", "light yellow")
        text_scout_skills_rect = text_scout_skills_surf.get_rect()
        text_scout_skills_rect.midleft = (650, 582)

        character_sheet_text.append((text_name_surf, text_name_rect))
        character_sheet_text.append((text_race_surf, text_race_rect))
        character_sheet_text.append((text_rolled_surf, text_rolled_rect))
        character_sheet_text.append((text_health_surf, text_health_rect))
        character_sheet_text.append((text_energy_surf, text_energy_rect))
        character_sheet_text.append((text_experience_surf, text_experience_rect))
        character_sheet_text.append((text_mage_surf, text_mage_rect))
        character_sheet_text.append((text_fighter_surf, text_fighter_rect))
        character_sheet_text.append((text_scout_surf, text_scout_rect))
        character_sheet_text.append((text_amuna_surf, text_amuna_rect))
        character_sheet_text.append((text_nuldar_surf, text_nuldar_rect))
        character_sheet_text.append((text_sorae_surf, text_sorae_rect))
        character_sheet_text.append((text_mage_skills_surf, text_mage_skills_rect))
        character_sheet_text.append((text_fighter_skills_surf, text_fighter_skills_rect))
        character_sheet_text.append((text_scout_skills_surf, text_scout_skills_rect))
        character_sheet_window.append(character_sheet)


def journal_info_draw(journal, player, font, draw_condition, switch_phase, npc_artherian, artherian_2):
    if not draw_condition:
        journal_text.clear()
        journal_window.clear()
    else:
        if player.current_zone == "seldon" or player.current_zone == "stardust" or player.current_zone == "rohir" or \
                player.current_zone == "reservoir a" or player.current_zone == "reservoir b" \
                or player.current_zone == "reservoir c":
            text_quest1_surf = font.render(str(list(player.current_quests)[0]), True, "black", "light yellow")
            text_quest1_rect = text_quest1_surf.get_rect()
            text_quest1_rect.midleft = (600, 145)
            text_quest1_info_surf = font.render(str(list(player.current_quests.values())[0]), True, "black",
                                                "light yellow")
            text_quest1_info_rect = text_quest1_info_surf.get_rect()
            text_quest1_info_rect.midleft = (540, 190)
            text_quest1_prog_surf = font.render(str(player.quest_progress["sneaky snakes"]) + " /4",
                                                True, "black", "light yellow")
            text_quest1_prog_rect = text_quest1_prog_surf.get_rect()
            text_quest1_prog_rect.midleft = (950, 145)

            text_quest2_surf = font.render(str(list(player.current_quests)[1]), True, "black", "light yellow")
            text_quest2_rect = text_quest2_surf.get_rect()
            text_quest2_rect.midleft = (600, 272)
            text_quest2_info_surf = font.render(str(list(player.current_quests.values())[1]), True, "black",
                                                "light yellow")
            text_quest2_info_rect = text_quest2_info_surf.get_rect()
            text_quest2_info_rect.midleft = (540, 320)
            text_quest2_prog_surf = font.render(str(player.quest_progress["village repairs"]) + " /4",
                                                True, "black", "light yellow")
            text_quest2_prog_rect = text_quest2_prog_surf.get_rect()
            text_quest2_prog_rect.midleft = (950, 272)

            text_quest3_surf = font.render(str(list(player.current_quests)[2]), True, "black", "light yellow")
            text_quest3_rect = text_quest3_surf.get_rect()
            text_quest3_rect.midleft = (600, 405)
            text_quest3_info_surf = font.render(str(list(player.current_quests.values())[2]), True, "black",
                                                "light yellow")
            text_quest3_info_rect = text_quest3_info_surf.get_rect()
            text_quest3_info_rect.midleft = (540, 455)
            text_quest3_prog_surf = font.render(str(player.quest_progress["where's nede?"]) + " /1", True,
                                                "black", "light yellow")
            text_quest3_prog_rect = text_quest3_prog_surf.get_rect()
            text_quest3_prog_rect.midleft = (950, 405)

            text_quest4_surf = font.render(str(list(player.current_quests)[3]), True, "black", "light yellow")
            text_quest4_rect = text_quest4_surf.get_rect()
            text_quest4_rect.midleft = (600, 538)
            text_quest4_info_surf = font.render(str(list(player.current_quests.values())[3]), True, "black",
                                                "light yellow")
            text_quest4_info_rect = text_quest4_info_surf.get_rect()
            text_quest4_info_rect.midleft = (540, 585)
            text_quest4_prog_surf = font.render(str(player.quest_progress["ghouled again"]) + " /4", True,
                                                "black", "light yellow")
            text_quest4_prog_rect = text_quest4_prog_surf.get_rect()
            text_quest4_prog_rect.midleft = (950, 538)

        if player.current_zone == "korlok" or player.current_zone == "mines" or \
                player.current_zone == "terra trail" or player.current_zone == "fishing hut" \
                or player.current_zone == "forge":
            text_quest1_surf = font.render(str(list(player.current_quests)[4]), True, "black", "light yellow")
            text_quest1_rect = text_quest1_surf.get_rect()
            text_quest1_rect.midleft = (600, 145)
            text_quest1_info_surf = font.render(str(list(player.current_quests.values())[4]), True, "black",
                                                "light yellow")
            text_quest1_info_rect = text_quest1_info_surf.get_rect()
            text_quest1_info_rect.midleft = (540, 190)
            text_quest1_prog_surf = font.render(str(player.quest_progress["band hammer"]) + " /4",
                                                True, "black", "light yellow")
            text_quest1_prog_rect = text_quest1_prog_surf.get_rect()
            text_quest1_prog_rect.midleft = (950, 145)

            text_quest2_surf = font.render(str(list(player.current_quests)[5]), True, "black", "light yellow")
            text_quest2_rect = text_quest2_surf.get_rect()
            text_quest2_rect.midleft = (600, 272)
            text_quest2_info_surf = font.render(str(list(player.current_quests.values())[5]), True, "black",
                                                "light yellow")
            text_quest2_info_rect = text_quest2_info_surf.get_rect()
            text_quest2_info_rect.midleft = (540, 320)
            text_quest2_prog_surf = font.render(str(player.quest_progress["elementary elementals"]) + " /4",
                                                True, "black", "light yellow")
            text_quest2_prog_rect = text_quest2_prog_surf.get_rect()
            text_quest2_prog_rect.midleft = (950, 272)

            text_quest3_surf = font.render(str(list(player.current_quests)[6]), True, "black", "light yellow")
            text_quest3_rect = text_quest3_surf.get_rect()
            text_quest3_rect.midleft = (600, 405)
            text_quest3_info_surf = font.render(str(list(player.current_quests.values())[6]), True, "black",
                                                "light yellow")
            text_quest3_info_rect = text_quest3_info_surf.get_rect()
            text_quest3_info_rect.midleft = (540, 455)
            text_quest3_prog_surf = font.render(str(player.quest_progress["can't apothecary it"]) + " /4", True,
                                                "black", "light yellow")
            text_quest3_prog_rect = text_quest3_prog_surf.get_rect()
            text_quest3_prog_rect.midleft = (950, 405)

            text_quest4_surf = font.render(str(list(player.current_quests)[7]), True, "black", "light yellow")
            text_quest4_rect = text_quest4_surf.get_rect()
            text_quest4_rect.midleft = (600, 538)
            text_quest4_info_surf = font.render(str(list(player.current_quests.values())[7]), True, "black",
                                                "light yellow")
            text_quest4_info_rect = text_quest4_info_surf.get_rect()
            text_quest4_info_rect.midleft = (540, 585)
            text_quest4_prog_surf = font.render(str(player.quest_progress["it's dangerous to go alone"]) + " /1", True,
                                                "black", "light yellow")
            text_quest4_prog_rect = text_quest4_prog_surf.get_rect()
            text_quest4_prog_rect.midleft = (950, 538)

        if player.current_zone == "eldream" or player.current_zone == "ectrenos" or \
                player.current_zone == "ectrenos left" or player.current_zone == "ectrenos right" \
                or player.current_zone == "ectrenos front" or player.current_zone == "ectrenos alcove" \
                or player.current_zone == "altar" or player.current_zone == "fishing alcove":
            text_quest1_surf = font.render(str(list(player.current_quests)[8]), True, "black", "light yellow")
            text_quest1_rect = text_quest1_surf.get_rect()
            text_quest1_rect.midleft = (600, 145)
            text_quest1_info_surf = font.render(str(list(player.current_quests.values())[8]), True, "black",
                                                "light yellow")
            text_quest1_info_rect = text_quest1_info_surf.get_rect()
            text_quest1_info_rect.midleft = (540, 190)
            text_quest1_prog_surf = font.render(str(player.quest_progress["kart troubles"]) + " /4",
                                                True, "black", "light yellow")
            text_quest1_prog_rect = text_quest1_prog_surf.get_rect()
            text_quest1_prog_rect.midleft = (950, 145)

            text_quest2_surf = font.render(str(list(player.current_quests)[9]), True, "black", "light yellow")
            text_quest2_rect = text_quest2_surf.get_rect()
            text_quest2_rect.midleft = (600, 272)
            text_quest2_info_surf = font.render(str(list(player.current_quests.values())[9]), True, "black",
                                                "light yellow")
            text_quest2_info_rect = text_quest2_info_surf.get_rect()
            text_quest2_info_rect.midleft = (540, 320)
            text_quest2_prog_surf = font.render(str(player.quest_progress["las escondidas"]) + " /4",
                                                True, "black", "light yellow")
            text_quest2_prog_rect = text_quest2_prog_surf.get_rect()
            text_quest2_prog_rect.midleft = (950, 272)

            text_quest3_surf = font.render(str(list(player.current_quests)[10]), True, "black", "light yellow")
            text_quest3_rect = text_quest3_surf.get_rect()
            text_quest3_rect.midleft = (600, 405)
            text_quest3_info_surf = font.render(str(list(player.current_quests.values())[10]), True, "black",
                                                "light yellow")
            text_quest3_info_rect = text_quest3_info_surf.get_rect()
            text_quest3_info_rect.midleft = (540, 455)
            text_quest3_prog_surf = font.render(str(player.quest_progress["hatch 'em all"]) + " /1", True,
                                                "black", "light yellow")
            text_quest3_prog_rect = text_quest3_prog_surf.get_rect()
            text_quest3_prog_rect.midleft = (950, 405)

            text_quest4_surf = font.render(str(list(player.current_quests)[11]), True, "black", "light yellow")
            text_quest4_rect = text_quest4_surf.get_rect()
            text_quest4_rect.midleft = (600, 538)
            text_quest4_info_surf = font.render(str(list(player.current_quests.values())[11]), True, "black",
                                                "light yellow")
            text_quest4_info_rect = text_quest4_info_surf.get_rect()
            text_quest4_info_rect.midleft = (540, 585)
            text_quest4_prog_surf = font.render(str(player.quest_progress["shades of fear"]) + " /4", True,
                                                "black", "light yellow")
            text_quest4_prog_rect = text_quest4_prog_surf.get_rect()
            text_quest4_prog_rect.midleft = (950, 538)

        if player.current_zone == "marrow entrance" or player.current_zone == "marrow ramps west" or \
                player.current_zone == "marrow ramps east" or player.current_zone == "marrow tower west" \
                or player.current_zone == "marrow tower east" or player.current_zone == "marrow ramps west end" \
                or player.current_zone == "marrow ramps east end" or player.current_zone == "marrow" \
                or player.current_zone == "sub marrow":

            text_quest1_surf = font.render("Barrier blockade", True, "black", "light yellow")
            text_quest1_rect = text_quest1_surf.get_rect()
            text_quest1_rect.midleft = (600, 145)
            text_quest1_info_surf = font.render("", True, "black",
                                                "light yellow")
            text_quest1_info_rect = text_quest1_info_surf.get_rect()
            text_quest1_info_rect.midleft = (540, 190)
            if switch_phase != "complete":
                text_quest1_prog_surf = font.render("0/1", True, "black", "light yellow")
                text_quest1_info_surf = font.render("Activate the switch to access Marrow.",
                                                    True, "black", "light yellow")
            if switch_phase == "complete":
                text_quest1_prog_surf = font.render("1/1", True, "black", "light yellow")
                text_quest1_info_surf = font.render("You opened the barrier.",
                                                    True, "black", "light yellow")

            text_quest1_prog_rect = text_quest1_prog_surf.get_rect()
            text_quest1_prog_rect.midleft = (950, 145)

            text_quest2_surf = font.render("Vamos Vanguard", True, "black", "light yellow")
            text_quest2_rect = text_quest2_surf.get_rect()
            text_quest2_rect.midleft = (600, 272)
            text_quest2_info_surf = font.render("", True, "black", "light yellow")
            text_quest2_info_rect = text_quest2_info_surf.get_rect()
            text_quest2_info_rect.midleft = (540, 320)
            text_quest2_prog_surf = font.render("0/2", True, "black", "light yellow")
            text_quest2_prog_rect = text_quest2_prog_surf.get_rect()
            text_quest2_prog_rect.midleft = (950, 272)

            text_quest3_surf = font.render("Legends never die", True, "black", "light yellow")
            text_quest3_rect = text_quest3_surf.get_rect()
            text_quest3_rect.midleft = (600, 405)
            if not npc_artherian.gift:
                text_quest3_info_surf = font.render("Talk to Artherian to start this task.",
                                                    True, "black", "light yellow")
            if npc_artherian.gift and not artherian_2:
                text_quest3_info_surf = font.render("Smelt and Enchant the armor casing.",
                                                    True, "black", "light yellow")
            if artherian_2:
                text_quest3_info_surf = font.render("Return to Artherian with the Enchanted Casing.",
                                                    True, "black", "light yellow")
            if npc_artherian.quest_complete:
                text_quest3_info_surf = font.render("You completed this task.", True, "black", "light yellow")
            text_quest3_info_rect = text_quest3_info_surf.get_rect()
            text_quest3_info_rect.midleft = (540, 455)
            text_quest3_prog_surf = font.render("0/2", True, "black", "light yellow")
            if npc_artherian.gift and not artherian_2:
                text_quest3_prog_surf = font.render("1/2", True, "black", "light yellow")
            if artherian_2:
                text_quest3_prog_surf = font.render("2/2", True, "black", "light yellow")
            text_quest3_prog_rect = text_quest3_prog_surf.get_rect()
            text_quest3_prog_rect.midleft = (950, 405)

            text_quest4_surf = font.render("Ultimate ultimatum", True, "black", "light yellow")
            text_quest4_rect = text_quest4_surf.get_rect()
            text_quest4_rect.midleft = (600, 538)
            text_quest4_info_surf = font.render("", True, "black", "light yellow")
            text_quest4_info_rect = text_quest4_info_surf.get_rect()
            text_quest4_info_rect.midleft = (540, 585)
            text_quest4_prog_surf = font.render("0/1", True, "black", "light yellow")
            text_quest4_prog_rect = text_quest4_prog_surf.get_rect()
            text_quest4_prog_rect.midleft = (950, 538)

        journal_text.append((text_quest1_surf, text_quest1_rect))
        journal_text.append((text_quest1_info_surf, text_quest1_info_rect))
        journal_text.append((text_quest1_prog_surf, text_quest1_prog_rect))
        journal_text.append((text_quest2_surf, text_quest2_rect))
        journal_text.append((text_quest2_info_surf, text_quest2_info_rect))
        journal_text.append((text_quest2_prog_surf, text_quest2_prog_rect))
        journal_text.append((text_quest3_surf, text_quest3_rect))
        journal_text.append((text_quest3_info_surf, text_quest3_info_rect))
        journal_text.append((text_quest3_prog_surf, text_quest3_prog_rect))
        journal_text.append((text_quest4_surf, text_quest4_rect))
        journal_text.append((text_quest4_info_surf, text_quest4_info_rect))
        journal_text.append((text_quest4_prog_surf, text_quest4_prog_rect))
        journal_window.append(journal)


def level_up_draw(level_up_win, player, level_up_font, draw_condition):
    if not draw_condition:
        level_up_text.clear()
        level_up_window.clear()

    else:
        text_leveled_up_surf = level_up_font.render(str(player.level), True, "black", "light yellow")
        text_leveled_up_rect = text_leveled_up_surf.get_rect()
        text_leveled_up_rect.center = (260, 146)

        level_up_text.append((text_leveled_up_surf, text_leveled_up_rect))
        level_up_window.append(level_up_win)


def quest_box_draw(quest_npc, draw_condition, garan_quest_window, maurelle_quest_window, celeste_quest_window,
                   torune_quest_window, voruke_quest_window, zerah_quest_window, kirean_quest_window,
                   dionte_quest_window, accept_button, decline_button, omoku_quest_window, leyre_quest_window,
                   aitor_quest_window, everett_quest_window, artherian_quest_window, artherian_quest_window_2,
                   artherian_1, maydria_quest_window):
    if not draw_condition:
        quest_box.clear()
    else:
        try:
            if quest_npc.name == "garan":
                quest_box.append(garan_quest_window)
            if quest_npc.name == "maurelle":
                quest_box.append(maurelle_quest_window)
            if quest_npc.name == "celeste":
                quest_box.append(celeste_quest_window)
            if quest_npc.name == "torune":
                quest_box.append(torune_quest_window)
            if quest_npc.name == "voruke":
                quest_box.append(voruke_quest_window)
            if quest_npc.name == "zerah":
                quest_box.append(zerah_quest_window)
            if quest_npc.name == "kirean":
                quest_box.append(kirean_quest_window)
            if quest_npc.name == "dionte":
                quest_box.append(dionte_quest_window)
            if quest_npc.name == "omoku":
                quest_box.append(omoku_quest_window)
            if quest_npc.name == "leyre":
                quest_box.append(leyre_quest_window)
            if quest_npc.name == "aitor":
                quest_box.append(aitor_quest_window)
            if quest_npc.name == "everett":
                quest_box.append(everett_quest_window)
            if quest_npc.name == "artherian":
                if not artherian_1:
                    quest_box.append(artherian_quest_window)
                else:
                    quest_box.append(artherian_quest_window_2)
            if quest_npc.name == "maydria":
                quest_box.append(maydria_quest_window)

        except AttributeError:
            if quest_npc == "kirean":
                quest_box.append(kirean_quest_window)
            if quest_npc == "aitor":
                quest_box.append(aitor_quest_window)

        quest_box.append(accept_button)
        quest_box.append(decline_button)


def quest_complete_draw(quest_npc, draw_condition, garan_quest_window, maurelle_quest_window, celeste_quest_window,
                        torune_quest_window, voruke_quest_window, zerah_quest_window, kirean_quest_window,
                        dionte_quest_window, omoku_quest_window, leyre_quest_window, aitor_quest_window,
                        everett_quest_window, artherian_quest_window, maydria_task_window):
    if not draw_condition:
        quest_complete_box.clear()
    else:
        try:
            if quest_npc.name == "garan":
                quest_complete_box.append(garan_quest_window)
            if quest_npc.name == "maurelle":
                quest_complete_box.append(maurelle_quest_window)
            if quest_npc.name == "celeste":
                quest_complete_box.append(celeste_quest_window)
            if quest_npc.name == "torune":
                quest_complete_box.append(torune_quest_window)
            if quest_npc.name == "voruke":
                quest_complete_box.append(voruke_quest_window)
            if quest_npc.name == "zerah":
                quest_complete_box.append(zerah_quest_window)
            if quest_npc.name == "kirean":
                quest_complete_box.append(kirean_quest_window)
            if quest_npc.name == "dionte":
                quest_complete_box.append(dionte_quest_window)
            if quest_npc.name == "omoku":
                quest_complete_box.append(omoku_quest_window)
            if quest_npc.name == "leyre":
                quest_complete_box.append(leyre_quest_window)
            if quest_npc.name == "aitor":
                quest_complete_box.append(aitor_quest_window)
            if quest_npc.name == "everett":
                quest_complete_box.append(everett_quest_window)
            if quest_npc.name == "artherian":
                quest_complete_box.append(artherian_quest_window)
            if quest_npc.name == "maydria":
                quest_complete_box.append(maydria_task_window)
        except AttributeError:
            if quest_npc == "kirean":
                quest_complete_box.append(kirean_quest_window)
            if quest_npc == "aitor":
                quest_complete_box.append(aitor_quest_window)


def quest_box_draw_fishing(quest_npc, draw_condition, jerry_quest_window, accept_button, decline_button):
    if not draw_condition:
        quest_box_fishing.clear()
    else:
        if quest_npc == "jerry":
            quest_box_fishing.append(jerry_quest_window)
        quest_box_fishing.append(accept_button)
        quest_box_fishing.append(decline_button)


def quest_complete_draw_fishing(quest_npc, draw_condition, jerry_quest_window):
    if not draw_condition:
        quest_complete_box_fishing.clear()
    else:
        if quest_npc == "jerry":
            quest_complete_box_fishing.append(jerry_quest_window)


def equipment_updates(player, graphics, basic_armor, forged_armor, mythical_armor, legendary_armor, power_gloves,
                      chroma_boots):
    player_equipment.clear()

    if player.equipment["armor"] != "":
        if player.equipment["armor"].name == "basic armor":
            basic_armor.update(1078, 197, graphics["basic_armor"])
            player_equipment.append(basic_armor)
        if player.equipment["armor"].name == "forged armor":
            forged_armor.update(1078, 197, graphics["forged_armor"])
            player_equipment.append(forged_armor)
        if player.equipment["armor"].name == "mythical armor":
            mythical_armor.update(1078, 197, graphics["mythical_armor"])
            player_equipment.append(mythical_armor)
        if player.equipment["armor"].name == "legendary armor":
            legendary_armor.update(1078, 197, graphics["legendary_armor"])
            player_equipment.append(legendary_armor)

    if player.equipment["gloves"] != "":
        if player.equipment["gloves"].name == "power gloves":
            power_gloves.update(1153, 197, graphics["gloves"])
            player_equipment.append(power_gloves)

    if player.equipment["boots"] != "":
        if player.equipment["boots"].name == "chroma boots":
            chroma_boots.update(1229, 197, graphics["boots_img"])
            player_equipment.append(chroma_boots)


def item_updates(player, graphic):
    player_items.clear()

    if len(player.items) > 0:
        first_coord = 1063
        second_coord = 462
        try:
            inventory_counter = 0

            for item_here in player.items:
                if item_here.name == "small health potion":
                    item_here.update(first_coord, second_coord, graphic["small_health_pot_img"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "small energy potion":
                    item_here.update(first_coord, second_coord, graphic["small_energy_pot_img"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "big health potion":
                    item_here.update(first_coord, second_coord, graphic["health_pot_img"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "big energy potion":
                    item_here.update(first_coord, second_coord, graphic["energy_pot_img"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "super potion":
                    item_here.update(first_coord, second_coord, graphic["super_pot_img"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "shiny rock":
                    item_here.update(first_coord, second_coord, graphic["shiny_rock_img"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "bone dust":
                    item_here.update(first_coord, second_coord, graphic["bone_dust_img"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "basic armor":
                    item_here.update(first_coord, second_coord, graphic["basic_armor"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "forged armor":
                    item_here.update(first_coord, second_coord, graphic["forged_armor"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "mythical armor":
                    item_here.update(first_coord, second_coord, graphic["mythical_armor"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "legendary armor":
                    item_here.update(first_coord, second_coord, graphic["legendary_armor"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "boss key" or item_here.name == "ramps key":
                    item_here.update(first_coord, second_coord, graphic["key_img"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "power gloves":
                    item_here.update(first_coord, second_coord, graphic["gloves"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "cracked ember":
                    item_here.update(first_coord, second_coord, graphic["ember"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "broken band":
                    item_here.update(first_coord, second_coord, graphic["band"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "pet seed":
                    if item_here.level == 2:
                        item_here.update(first_coord, second_coord, graphic["seed_ready_img"])
                    else:
                        item_here.update(first_coord, second_coord, graphic["seed_img"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "pet whistle kasper":
                    item_here.update(first_coord, second_coord, graphic["whistle_kasper_img"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "pet whistle torok":
                    item_here.update(first_coord, second_coord, graphic["whistle_torok_img"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "pet whistle iriana":
                    item_here.update(first_coord, second_coord, graphic["whistle_iriana_img"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "dried fins":
                    item_here.update(first_coord, second_coord, graphic["fins_img"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "oscura pluma":
                    item_here.update(first_coord, second_coord, graphic["pluma_img"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "chroma boots":
                    item_here.update(first_coord, second_coord, graphic["boots_img"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "pet cookie":
                    item_here.update(first_coord, second_coord, graphic["pet_cookie_img"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "pet candy":
                    item_here.update(first_coord, second_coord, graphic["pet_candy_img"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "pet tart":
                    item_here.update(first_coord, second_coord, graphic["pet_tart_img"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "bone shard":
                    item_here.update(first_coord, second_coord, graphic["bone_shard"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "prism":
                    item_here.update(first_coord, second_coord, graphic["prism"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "casing":
                    item_here.update(first_coord, second_coord, graphic["casing"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "smelted casing":
                    item_here.update(first_coord, second_coord, graphic["smelted_casing"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "enchanted casing":
                    item_here.update(first_coord, second_coord, graphic["enchanted_casing"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "seldon firework":
                    item_here.update(first_coord, second_coord, graphic["seldon_firework"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "korlok firework":
                    item_here.update(first_coord, second_coord, graphic["korlok_firework"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "eldream firework":
                    item_here.update(first_coord, second_coord, graphic["eldream_firework"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "seldon bait":
                    item_here.update(first_coord, second_coord, graphic["seldon_bait"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "korlok bait":
                    item_here.update(first_coord, second_coord, graphic["korlok_bait"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "eldream bait":
                    item_here.update(first_coord, second_coord, graphic["eldream_bait"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "mage book":
                    item_here.update(first_coord, second_coord, graphic["mage_book"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "fighter book":
                    item_here.update(first_coord, second_coord, graphic["fighter_book"])
                    player_items.append(item_here)
                    inventory_counter += 1
                if item_here.name == "scout book":
                    item_here.update(first_coord, second_coord, graphic["scout_book"])
                    player_items.append(item_here)
                    inventory_counter += 1

                first_coord += 60

                if inventory_counter > 3:
                    second_coord += 60
                    first_coord = 1063
                    inventory_counter = 0

        except AttributeError:
            pass


def button_highlights(pygame, player, start_chosen, new_game_chosen, new_game_button, pos, button_highlight,
                      graphic_dict, continue_button, start_button, back_button, amuna_button, nuldar_button,
                      sorae_button, save_check_window, yes_button, no_button, item_info_button, rest_button,
                      leave_button, buy_button, in_inn, in_shop, buy_clicked, offense_select_button,
                      in_battle, mage_attack_button, fighter_attack_button, scout_attack_button,
                      no_role_attack_button, barrier_button, sharp_sense_button, hard_strike_button, in_over_world,
                      seldon_map_button, korlok_map_button, eldream_map_button, marrow_map_button, character_button,
                      quests_button, save_button, map_button, in_npc_interaction, quest_button, quest_clicked,
                      accept_button, decline_button, in_apothecary, staff, sword, bow, potion_button,
                      create_potion_button, in_menagerie, ok_button, hatch_ready, menagerie_window_open,
                      kasper_manage_button, torok_manage_button, iriana_manage_button, amuna_male_button,
                      amuna_female_button, nuldar_male_button, nuldar_female_button, sorae_alpha_button,
                      sorae_beta_button, in_academia, mage_learn_clicked, fighter_learn_clicked,
                      scout_learn_clicked, mage_learn_button, fighter_learn_button, scout_learn_button,
                      barrier_learn_button, close_button, garan_gift, mirror_learn_button, mirror_button,
                      vanish_button, stun_button, kasper_unlocked, torok_unlocked, iriana_unlocked, music_toggle,
                      in_hut, basic_fish, better_fish, even_better_fish, best_fish):
    # inventory rects
    inv_1 = pygame.Rect((1035, 435), (50, 50))
    inv_2 = pygame.Rect((1095, 435), (50, 50))
    inv_3 = pygame.Rect((1155, 435), (50, 50))
    inv_4 = pygame.Rect((1215, 435), (50, 50))
    inv_5 = pygame.Rect((1035, 495), (50, 50))
    inv_6 = pygame.Rect((1095, 495), (50, 50))
    inv_7 = pygame.Rect((1155, 495), (50, 50))
    inv_8 = pygame.Rect((1215, 495), (50, 50))
    inv_9 = pygame.Rect((1035, 555), (50, 50))
    inv_10 = pygame.Rect((1095, 555), (50, 50))
    inv_11 = pygame.Rect((1155, 555), (50, 50))
    inv_12 = pygame.Rect((1215, 555), (50, 50))
    inv_13 = pygame.Rect((1035, 615), (50, 50))
    inv_14 = pygame.Rect((1095, 615), (50, 50))
    inv_15 = pygame.Rect((1155, 615), (50, 50))
    inv_16 = pygame.Rect((1215, 615), (50, 50))
    flower_button = pygame.Rect((1150, 670), (65, 65))
    fish_button = pygame.Rect((1210, 670), (65, 65))
    # shop inventory rects
    shop_inv_1 = pygame.Rect((780, 405), (50, 50))
    shop_inv_2 = pygame.Rect((840, 405), (50, 50))
    shop_inv_3 = pygame.Rect((900, 405), (50, 50))
    shop_inv_4 = pygame.Rect((960, 405), (50, 50))
    shop_inv_5 = pygame.Rect((780, 465), (50, 50))
    shop_inv_6 = pygame.Rect((840, 465), (50, 50))
    shop_inv_7 = pygame.Rect((900, 465), (50, 50))
    shop_inv_8 = pygame.Rect((960, 465), (50, 50))
    # equipment rects
    armor = pygame.Rect((1050, 170), (50, 50))
    gloves = pygame.Rect((1125, 170), (50, 50))
    boots = pygame.Rect((1200, 170), (50, 50))

    if not start_chosen:
        if not new_game_chosen:
            if new_game_button.rect.collidepoint(pos):
                button_highlight.update(new_game_button.x_coordinate + 10, new_game_button.y_coordinate,
                                        graphic_dict["start high"])
                return True
            if continue_button.rect.collidepoint(pos):
                button_highlight.update(continue_button.x_coordinate + 10, continue_button.y_coordinate,
                                        graphic_dict["start high"])
                return True
            if music_toggle.rect.collidepoint(pos):
                button_highlight.update(music_toggle.x_coordinate, music_toggle.y_coordinate,
                                        graphic_dict["music_button_high"])
                return True

        if new_game_chosen:
            if start_button.rect.collidepoint(pos):
                button_highlight.update(start_button.x_coordinate + 22, start_button.y_coordinate,
                                        graphic_dict["begin high"])
                return True
            if back_button.rect.collidepoint(pos):
                button_highlight.update(back_button.x_coordinate, back_button.y_coordinate + 7,
                                        graphic_dict["main high"])
                return True

            if amuna_button.rect.collidepoint(pos):
                button_highlight.update(140, amuna_button.y_coordinate, graphic_dict["race high"])
                return True
            if nuldar_button.rect.collidepoint(pos):
                button_highlight.update(140, nuldar_button.y_coordinate, graphic_dict["race high"])
                return True
            if sorae_button.rect.collidepoint(pos):
                button_highlight.update(140, sorae_button.y_coordinate, graphic_dict["race high"])
                return True

            if amuna_male_button.rect.collidepoint(pos):
                button_highlight.update(amuna_male_button.x_coordinate + 154, amuna_male_button.y_coordinate,
                                        graphic_dict["gender high"])
                return True
            if amuna_female_button.rect.collidepoint(pos):
                button_highlight.update(amuna_female_button.x_coordinate + 154, amuna_female_button.y_coordinate,
                                        graphic_dict["gender high"])
                return True
            if nuldar_male_button.rect.collidepoint(pos):
                button_highlight.update(nuldar_male_button.x_coordinate + 154, nuldar_male_button.y_coordinate,
                                        graphic_dict["gender high"])
                return True
            if nuldar_female_button.rect.collidepoint(pos):
                button_highlight.update(nuldar_female_button.x_coordinate + 154, nuldar_female_button.y_coordinate,
                                        graphic_dict["gender high"])
                return True
            if sorae_alpha_button.rect.collidepoint(pos):
                button_highlight.update(sorae_alpha_button.x_coordinate + 153, sorae_alpha_button.y_coordinate,
                                        graphic_dict["gender high"])
                return True
            if sorae_beta_button.rect.collidepoint(pos):
                button_highlight.update(sorae_beta_button.x_coordinate + 153, sorae_beta_button.y_coordinate,
                                        graphic_dict["gender high"])
                return True
            if music_toggle.rect.collidepoint(pos):
                button_highlight.update(music_toggle.x_coordinate, music_toggle.y_coordinate,
                                        graphic_dict["music_button_high"])
                return True

    if start_chosen:
        if len(item_info_window) == 0 and len(sell_info_window) == 0 and garan_gift:
            if staff.rect.collidepoint(pos):
                button_highlight.update(1077, 283, graphic_dict["item high"])
                return True
            if sword.rect.collidepoint(pos):
                button_highlight.update(1152, 283, graphic_dict["item high"])
                return True
            if bow.rect.collidepoint(pos):
                button_highlight.update(1227, 283, graphic_dict["item high"])
                return True
        if inv_1.collidepoint(pos):
            if len(player.items) > 0:
                button_highlight.update(1062, 461, graphic_dict["item high"])
                return True
        elif inv_2.collidepoint(pos):
            if len(player.items) > 1:
                button_highlight.update(1122, 461, graphic_dict["item high"])
                return True
        elif inv_3.collidepoint(pos):
            if len(player.items) > 2:
                button_highlight.update(1182, 461, graphic_dict["item high"])
                return True
        elif inv_4.collidepoint(pos):
            if len(player.items) > 3:
                button_highlight.update(1242, 461, graphic_dict["item high"])
                return True
        elif inv_5.collidepoint(pos):
            if len(player.items) > 4:
                button_highlight.update(1062, 521, graphic_dict["item high"])
                return True
        elif inv_6.collidepoint(pos):
            if len(player.items) > 5:
                button_highlight.update(1122, 521, graphic_dict["item high"])
                return True
        elif inv_7.collidepoint(pos):
            if len(player.items) > 6:
                button_highlight.update(1182, 521, graphic_dict["item high"])
                return True
        elif inv_8.collidepoint(pos):
            if len(player.items) > 7:
                button_highlight.update(1242, 521, graphic_dict["item high"])
                return True
        elif inv_9.collidepoint(pos):
            if len(player.items) > 8:
                button_highlight.update(1062, 581, graphic_dict["item high"])
                return True
        elif inv_10.collidepoint(pos):
            if len(player.items) > 9:
                button_highlight.update(1122, 581, graphic_dict["item high"])
                return True
        elif inv_11.collidepoint(pos):
            if len(player.items) > 10:
                button_highlight.update(1182, 581, graphic_dict["item high"])
                return True
        elif inv_12.collidepoint(pos):
            if len(player.items) > 11:
                button_highlight.update(1242, 581, graphic_dict["item high"])
                return True
        elif inv_13.collidepoint(pos):
            if len(player.items) > 12 and len(flower_pop_up_window) == 0 and len(fish_pop_up_window) == 0:
                button_highlight.update(1062, 641, graphic_dict["item high"])
                return True
        elif inv_14.collidepoint(pos):
            if len(player.items) > 13 and len(flower_pop_up_window) == 0 and len(fish_pop_up_window) == 0:
                button_highlight.update(1122, 641, graphic_dict["item high"])
                return True
        elif inv_15.collidepoint(pos):
            if len(player.items) > 14 and len(flower_pop_up_window) == 0 and len(fish_pop_up_window) == 0:
                button_highlight.update(1182, 641, graphic_dict["item high"])
                return True
        elif inv_16.collidepoint(pos):
            if len(player.items) > 15 and len(flower_pop_up_window) == 0 and len(fish_pop_up_window) == 0:
                button_highlight.update(1242, 641, graphic_dict["item high"])
                return True
        elif flower_button.collidepoint(pos):
            button_highlight.update(1182, 699, graphic_dict["item high"])
            return True
        elif fish_button.collidepoint(pos):
            button_highlight.update(1241, 699, graphic_dict["item high"])
            return True
        elif armor.collidepoint(pos):
            if len(item_info_window) == 0:
                if len(sell_info_window) == 0:
                    if player.equipment["armor"] != "":
                        button_highlight.update(1077, 195, graphic_dict["item high"])
                        return True
        elif gloves.collidepoint(pos):
            if len(item_info_window) == 0:
                if len(sell_info_window) == 0:
                    if player.equipment["gloves"] != "":
                        button_highlight.update(1152, 195, graphic_dict["item high"])
                        return True
        elif boots.collidepoint(pos):
            if len(item_info_window) == 0:
                if len(sell_info_window) == 0:
                    if player.equipment["boots"] != "":
                        button_highlight.update(1227, 195, graphic_dict["item high"])
                        return True
        elif len(save_check_window) > 0:
            if yes_button.rect.collidepoint(pos):
                button_highlight.update(yes_button.x_coordinate, yes_button.y_coordinate + 7,
                                        graphic_dict["main high"])
                return True
            elif no_button.rect.collidepoint(pos):
                button_highlight.update(no_button.x_coordinate, no_button.y_coordinate + 7,
                                        graphic_dict["main high"])
                return True

        elif len(item_info_window) > 0:
            if item_info_button.rect.collidepoint(pos):
                button_highlight.update(item_info_button.x_coordinate, item_info_button.y_coordinate + 7,
                                        graphic_dict["main high"])
                return True

        if in_inn:
            if rest_button.rect.collidepoint(pos):
                button_highlight.update(rest_button.x_coordinate,
                                        rest_button.y_coordinate + 7,
                                        graphic_dict["main high"])
                return True
            elif leave_button.rect.collidepoint(pos):
                button_highlight.update(leave_button.x_coordinate, leave_button.y_coordinate + 7,
                                        graphic_dict["main high"])
                return True

        if in_shop:
            if buy_button.rect.collidepoint(pos):
                button_highlight.update(buy_button.x_coordinate,
                                        buy_button.y_coordinate + 7,
                                        graphic_dict["main high"])
                return True
            elif leave_button.rect.collidepoint(pos):
                button_highlight.update(leave_button.x_coordinate, leave_button.y_coordinate + 7,
                                        graphic_dict["main high"])
                return True

            if player.current_zone == "seldon" or player.current_zone == "korlok" or \
                    player.current_zone == "ectrenos right":
                if len(sell_info_window) > 0:
                    if yes_button.rect.collidepoint(pos):
                        button_highlight.update(yes_button.x_coordinate, yes_button.y_coordinate + 6,
                                                graphic_dict["main high"])
                        return True
                elif buy_clicked:
                    if shop_inv_1.collidepoint(pos):
                        button_highlight.update(808, 431, graphic_dict["item high"])
                        return True
                    elif shop_inv_2.collidepoint(pos):
                        button_highlight.update(868, 431, graphic_dict["item high"])
                        return True
                    elif shop_inv_3.collidepoint(pos):
                        button_highlight.update(928, 431, graphic_dict["item high"])
                        return True
                    elif shop_inv_4.collidepoint(pos):
                        button_highlight.update(988, 431, graphic_dict["item high"])
                        return True
                    elif shop_inv_5.collidepoint(pos):
                        button_highlight.update(808, 491, graphic_dict["item high"])
                        return True
                    elif shop_inv_6.collidepoint(pos):
                        button_highlight.update(868, 491, graphic_dict["item high"])
                        return True
                    elif shop_inv_7.collidepoint(pos):
                        button_highlight.update(928, 491, graphic_dict["item high"])
                        return True
                    elif shop_inv_8.collidepoint(pos):
                        button_highlight.update(988, 491, graphic_dict["item high"])
                        return True
                    elif len(buy_info_window) > 0:
                        if yes_button.rect.collidepoint(pos):
                            button_highlight.update(yes_button.x_coordinate, yes_button.y_coordinate + 6,
                                                    graphic_dict["main high"])
                            return True

            if player.current_zone == "stardust":
                if buy_clicked:
                    if offense_select_button.rect.collidepoint(pos):
                        button_highlight.update(offense_select_button.x_coordinate,
                                                offense_select_button.y_coordinate,
                                                graphic_dict["role_high"])
                        return True

        if in_battle:
            if mage_attack_button.rect.collidepoint(pos) or fighter_attack_button.rect.collidepoint(pos) \
                    or scout_attack_button.rect.collidepoint(pos) or no_role_attack_button.rect.collidepoint(pos):
                button_highlight.update(mage_attack_button.x_coordinate - 2, mage_attack_button.y_coordinate + 1,
                                        graphic_dict["skill high"])
                return True
            elif barrier_button.rect.collidepoint(pos) or sharp_sense_button.rect.collidepoint(pos) \
                    or hard_strike_button.rect.collidepoint(pos):
                button_highlight.update(barrier_button.x_coordinate - 2,
                                        barrier_button.y_coordinate + 1,
                                        graphic_dict["skill high"])
                return True
            elif mirror_button.rect.collidepoint(pos) or vanish_button.rect.collidepoint(pos) \
                    or stun_button.rect.collidepoint(pos):
                button_highlight.update(mirror_button.x_coordinate - 2,
                                        mirror_button.y_coordinate + 1,
                                        graphic_dict["skill high"])
                return True

        if in_over_world:
            if len(world_map_container) > 0:
                if seldon_map_button.rect.collidepoint(pos):
                    button_highlight.update(seldon_map_button.x_coordinate, seldon_map_button.y_coordinate,
                                            graphic_dict["map_button_high"])
                    return True
                if korlok_map_button.rect.collidepoint(pos):
                    button_highlight.update(korlok_map_button.x_coordinate, korlok_map_button.y_coordinate,
                                            graphic_dict["map_button_high"])
                    return True
                if eldream_map_button.rect.collidepoint(pos):
                    button_highlight.update(eldream_map_button.x_coordinate, eldream_map_button.y_coordinate,
                                            graphic_dict["map_button_high"])
                    return True
                if marrow_map_button.rect.collidepoint(pos):
                    button_highlight.update(marrow_map_button.x_coordinate, marrow_map_button.y_coordinate,
                                            graphic_dict["map_button_high"])
                    return True

            if character_button.rect.collidepoint(pos):
                button_highlight.update(character_button.x_coordinate, character_button.y_coordinate + 7,
                                        graphic_dict["main high"])
                return True
            elif quests_button.rect.collidepoint(pos):
                button_highlight.update(quests_button.x_coordinate, quests_button.y_coordinate + 7,
                                        graphic_dict["main high"])
                return True
            elif save_button.rect.collidepoint(pos):
                if len(game_guide_container) == 0:
                    button_highlight.update(save_button.x_coordinate + 1, save_button.y_coordinate + 2,
                                            graphic_dict["save hearth high"])
                    return True
            elif map_button.rect.collidepoint(pos):
                if len(game_guide_container) == 0:
                    button_highlight.update(map_button.x_coordinate + 1, map_button.y_coordinate + 2,
                                            graphic_dict["save hearth high"])
                    return True
            elif music_toggle.rect.collidepoint(pos):
                if len(game_guide_container) == 0:
                    button_highlight.update(music_toggle.x_coordinate, music_toggle.y_coordinate,
                                            graphic_dict["music_button_high"])
                    return True

        if in_npc_interaction:
            if quest_button.rect.collidepoint(pos):
                button_highlight.update(quest_button.x_coordinate, quest_button.y_coordinate + 7,
                                        graphic_dict["main high"])
                return True
            elif leave_button.rect.collidepoint(pos):
                button_highlight.update(leave_button.x_coordinate, leave_button.y_coordinate + 7,
                                        graphic_dict["main high"])
                return True

            # quest window accept or decline button highlights when moused over
            if quest_clicked:
                if accept_button.rect.collidepoint(pos):
                    button_highlight.update(accept_button.x_coordinate, accept_button.y_coordinate + 7,
                                            graphic_dict["main high"])
                    return True
                elif decline_button.rect.collidepoint(pos):
                    button_highlight.update(decline_button.x_coordinate,
                                            decline_button.y_coordinate + 7,
                                            graphic_dict["main high"])
                    return True

        if in_academia:
            # highlighting books once moused over
            if not mage_learn_clicked and not fighter_learn_clicked and not scout_learn_clicked:
                if mage_learn_button.rect.collidepoint(pos):
                    button_highlight.update(mage_learn_button.x_coordinate - 7,
                                            mage_learn_button.y_coordinate + 12,
                                            graphic_dict["skill high"])
                    return True
                elif fighter_learn_button.rect.collidepoint(pos):
                    button_highlight.update(fighter_learn_button.x_coordinate - 1,
                                            fighter_learn_button.y_coordinate + 12,
                                            graphic_dict["skill high"])
                    return True
                elif scout_learn_button.rect.collidepoint(pos):
                    button_highlight.update(scout_learn_button.x_coordinate - 2,
                                            scout_learn_button.y_coordinate + 12,
                                            graphic_dict["skill high"])
                    return True
                elif leave_button.rect.collidepoint(pos):
                    button_highlight.update(leave_button.x_coordinate, leave_button.y_coordinate + 7,
                                            graphic_dict["main high"])
                    return True

            # highlighting skill learn buttons inside of books once moused over
            else:
                if barrier_learn_button.rect.collidepoint(pos):
                    button_highlight.update(barrier_learn_button.x_coordinate + 2,
                                            barrier_learn_button.y_coordinate + 3,
                                            graphic_dict["book_high"])
                    return True
                elif mirror_learn_button.rect.collidepoint(pos):
                    button_highlight.update(mirror_learn_button.x_coordinate + 2,
                                            mirror_learn_button.y_coordinate + 3,
                                            graphic_dict["book_high"])
                    return True
                elif close_button.rect.collidepoint(pos):
                    button_highlight.update(close_button.x_coordinate - 3, close_button.y_coordinate + 3,
                                            graphic_dict["close high"])
                    return True
                elif leave_button.rect.collidepoint(pos):
                    button_highlight.update(leave_button.x_coordinate, leave_button.y_coordinate + 7,
                                            graphic_dict["main high"])
                    return True

        if in_apothecary:
            if quest_button.rect.collidepoint(pos):
                button_highlight.update(quest_button.x_coordinate, quest_button.y_coordinate + 7,
                                        graphic_dict["main high"])
                return True
            elif leave_button.rect.collidepoint(pos):
                button_highlight.update(leave_button.x_coordinate, leave_button.y_coordinate + 7,
                                        graphic_dict["main high"])
                return True
            elif potion_button.rect.collidepoint(pos):
                button_highlight.update(potion_button.x_coordinate, potion_button.y_coordinate + 7,
                                        graphic_dict["main high"])
                return True
            elif create_potion_button.rect.collidepoint(pos):
                if len(potion_window_container) > 0:
                    button_highlight.update(create_potion_button.x_coordinate, create_potion_button.y_coordinate + 7,
                                            graphic_dict["main high"])
                    return True

            # quest window accept or decline button highlights when moused over
            if quest_clicked:
                if len(quest_box) > 0:
                    if accept_button.rect.collidepoint(pos):
                        button_highlight.update(accept_button.x_coordinate, accept_button.y_coordinate + 7,
                                                graphic_dict["main high"])
                        return True
                    elif decline_button.rect.collidepoint(pos):
                        button_highlight.update(decline_button.x_coordinate,
                                                decline_button.y_coordinate + 7,
                                                graphic_dict["main high"])
                        return True

        if in_menagerie:
            if quest_button.rect.collidepoint(pos):
                button_highlight.update(quest_button.x_coordinate, quest_button.y_coordinate + 7,
                                        graphic_dict["main high"])
                return True
            elif leave_button.rect.collidepoint(pos):
                button_highlight.update(leave_button.x_coordinate, leave_button.y_coordinate + 7,
                                        graphic_dict["main high"])
                return True
            elif potion_button.rect.collidepoint(pos):
                button_highlight.update(potion_button.x_coordinate, potion_button.y_coordinate + 7,
                                        graphic_dict["main high"])
                return True
            if hatch_ready:
                if ok_button.rect.collidepoint(pos):
                    button_highlight.update(ok_button.x_coordinate, ok_button.y_coordinate + 7,
                                            graphic_dict["main high"])
                    return True
            if menagerie_window_open:
                if not kasper_unlocked:
                    if kasper_manage_button.rect.collidepoint(pos):
                        button_highlight.update(kasper_manage_button.x_coordinate, kasper_manage_button.y_coordinate,
                                                graphic_dict["role_high"])
                        return True
                if not torok_unlocked:
                    if torok_manage_button.rect.collidepoint(pos):
                        button_highlight.update(torok_manage_button.x_coordinate, torok_manage_button.y_coordinate,
                                                graphic_dict["role_high"])
                        return True
                if not iriana_unlocked:
                    if iriana_manage_button.rect.collidepoint(pos):
                        button_highlight.update(iriana_manage_button.x_coordinate, iriana_manage_button.y_coordinate,
                                                graphic_dict["role_high"])
                        return True
            # quest window accept or decline button highlights when moused over
            if quest_clicked:
                if len(quest_box) > 0:
                    if accept_button.rect.collidepoint(pos):
                        button_highlight.update(accept_button.x_coordinate, accept_button.y_coordinate + 7,
                                                graphic_dict["main high"])
                        return True
                    elif decline_button.rect.collidepoint(pos):
                        button_highlight.update(decline_button.x_coordinate,
                                                decline_button.y_coordinate + 7,
                                                graphic_dict["main high"])
                        return True

        if in_hut:
            if quest_button.rect.collidepoint(pos):
                button_highlight.update(quest_button.x_coordinate, quest_button.y_coordinate + 7,
                                        graphic_dict["main high"])
                return True
            elif leave_button.rect.collidepoint(pos):
                button_highlight.update(leave_button.x_coordinate, leave_button.y_coordinate + 7,
                                        graphic_dict["main high"])
                return True
            elif potion_button.rect.collidepoint(pos):
                button_highlight.update(potion_button.x_coordinate, potion_button.y_coordinate + 7,
                                        graphic_dict["main high"])
                return True
            # quest window accept or decline button highlights when moused over
            if quest_clicked:
                if len(quest_box_fishing) > 0:
                    if accept_button.rect.collidepoint(pos):
                        button_highlight.update(accept_button.x_coordinate, accept_button.y_coordinate + 7,
                                                graphic_dict["main high"])
                        return True
                    elif decline_button.rect.collidepoint(pos):
                        button_highlight.update(decline_button.x_coordinate,
                                                decline_button.y_coordinate + 7,
                                                graphic_dict["main high"])
                        return True
            if len(fish_window_container) > 0:
                if basic_fish.rect.collidepoint(pos):
                    button_highlight.update(basic_fish.x_coordinate, basic_fish.y_coordinate + 7,
                                            graphic_dict["main high"])
                    return True
                elif better_fish.rect.collidepoint(pos):
                    button_highlight.update(better_fish.x_coordinate, better_fish.y_coordinate + 7,
                                            graphic_dict["main high"])
                    return True
                elif even_better_fish.rect.collidepoint(pos):
                    button_highlight.update(even_better_fish.x_coordinate, even_better_fish.y_coordinate + 7,
                                            graphic_dict["main high"])
                    return True
                elif best_fish.rect.collidepoint(pos):
                    button_highlight.update(best_fish.x_coordinate, best_fish.y_coordinate + 7,
                                            graphic_dict["main high"])
                    return True


# hearth button is clicked, sets fade transition for hearth screen and then back to district bg
def hearthstone_animation(pygame, screen, player, seldon_hearth_screen, seldon_district_bg, korlok_hearth_screen,
                          korlok_district_bg, eldream_hearth_screen, eldream_district_bg, SCREEN_WIDTH,
                          SCREEN_HEIGHT, game_window, marrow_hearth_screen, marrow_district_bg):
    if player.current_zone == "seldon":
        screen.fill((0, 0, 0))
        for alphas in range(0, 200):
            seldon_hearth_screen.set_alpha(alphas)
            screen.blit(seldon_hearth_screen, (0, 0))
            frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
            game_window.blit(frame, frame.get_rect())
            pygame.display.flip()
        screen.fill((0, 0, 0))
        for alphas in range(0, 50):
            seldon_district_bg.set_alpha(alphas)
            screen.blit(seldon_district_bg, (0, 0))
            frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
            game_window.blit(frame, frame.get_rect())
            pygame.display.flip()
        seldon_district_bg.set_alpha(255)
        screen.blit(seldon_district_bg, (0, 0))
        pygame.display.flip()
    if player.current_zone == "korlok":
        screen.fill((0, 0, 0))
        for alphas in range(0, 200):
            korlok_hearth_screen.set_alpha(alphas)
            screen.blit(korlok_hearth_screen, (0, 0))
            frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
            game_window.blit(frame, frame.get_rect())
            pygame.display.flip()
        screen.fill((0, 0, 0))
        for alphas in range(0, 50):
            korlok_district_bg.set_alpha(alphas)
            screen.blit(korlok_district_bg, (0, 0))
            frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
            game_window.blit(frame, frame.get_rect())
            pygame.display.flip()
        korlok_district_bg.set_alpha(255)
        screen.blit(korlok_district_bg, (0, 0))
        frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
        game_window.blit(frame, frame.get_rect())
        pygame.display.flip()
    if player.current_zone == "eldream":
        screen.fill((0, 0, 0))
        for alphas in range(0, 200):
            eldream_hearth_screen.set_alpha(alphas)
            screen.blit(eldream_hearth_screen, (0, 0))
            frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
            game_window.blit(frame, frame.get_rect())
            pygame.display.flip()
        screen.fill((0, 0, 0))
        for alphas in range(0, 50):
            eldream_district_bg.set_alpha(alphas)
            screen.blit(eldream_district_bg, (0, 0))
            frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
            game_window.blit(frame, frame.get_rect())
            pygame.display.flip()
        eldream_district_bg.set_alpha(255)
        screen.blit(eldream_district_bg, (0, 0))
        frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
        game_window.blit(frame, frame.get_rect())
        pygame.display.flip()
    if player.current_zone == "marrow":
        screen.fill((0, 0, 0))
        for alphas in range(0, 200):
            marrow_hearth_screen.set_alpha(alphas)
            screen.blit(marrow_hearth_screen, (0, 0))
            frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
            game_window.blit(frame, frame.get_rect())
            pygame.display.flip()
        screen.fill((0, 0, 0))
        for alphas in range(0, 50):
            marrow_district_bg.set_alpha(alphas)
            screen.blit(marrow_district_bg, (0, 0))
            frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
            game_window.blit(frame, frame.get_rect())
            pygame.display.flip()
        marrow_district_bg.set_alpha(255)
        screen.blit(marrow_district_bg, (0, 0))
        frame = pygame.transform.smoothscale(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
        game_window.blit(frame, frame.get_rect())
        pygame.display.flip()


def loot_popups(time, loot_updated, font, loot_popup, battle_info_to_return_to_main_loop, leveled):
    if not loot_updated:
        loot_popup_container.clear()
        loot_text_container.clear()
        loot_popup_container.append(loot_popup)
        xp_info_surf = font.render("+" + str(battle_info_to_return_to_main_loop["experience"] + " xp"),
                                   True, "black", (203, 195, 227))
        xp_info_rect = xp_info_surf.get_rect()
        xp_info_rect.center = (182, 492)
        loot_text_container.append((xp_info_surf, xp_info_rect))
        know_info_surf = font.render(str(battle_info_to_return_to_main_loop["knowledge"]),
                                     True, "black", (144, 238, 144))
        know_info_rect = know_info_surf.get_rect()
        know_info_rect.center = (205, 510)
        loot_text_container.append((know_info_surf, know_info_rect))
        loot_info_surf = font.render(str(battle_info_to_return_to_main_loop["item dropped"]),
                                     True, "black", "silver")
        loot_info_rect = loot_info_surf.get_rect()
        loot_info_rect.center = (170, 565)
        loot_text_container.append((loot_info_surf, loot_info_rect))
        loot_updated = True
        loot_level_tic = time.perf_counter()
        loot_info = True
        if battle_info_to_return_to_main_loop["leveled_up"] and not leveled:
            leveled = True

        loot_popup_return = {"loot_updated": loot_updated, "loot_level_tic": loot_level_tic, "loot_info": loot_info,
                             "leveled": leveled}

        return loot_popup_return


def mini_map(player, graphic_dict, world_map, seldon_map_button, korlok_map_button, eldream_map_button,
             marrow_map_button, amuna_location, nuldar_location, sorae_location):
    world_map_container.append(world_map)
    world_map_container.append(seldon_map_button)
    world_map_container.append(korlok_map_button)
    world_map_container.append(eldream_map_button)
    world_map_container.append(marrow_map_button)

    # update sprite showing player location representation on map
    if player.race == "amuna":
        if player.gender == "male":
            if player.current_zone == "seldon":
                amuna_location.update(seldon_map_button.x_coordinate,
                                      seldon_map_button.y_coordinate,
                                      graphic_dict["amuna_location"])
            if player.current_zone == "rohir":
                amuna_location.update(seldon_map_button.x_coordinate,
                                      seldon_map_button.y_coordinate - 75,
                                      graphic_dict["amuna_location"])
            if player.current_zone == "stardust":
                amuna_location.update(seldon_map_button.x_coordinate - 75,
                                      seldon_map_button.y_coordinate - 25,
                                      graphic_dict["amuna_location"])
            if player.current_zone == "korlok" or player.current_zone == "mines" or \
                    player.current_zone == "terra trail" or player.current_zone == "fishing hut" or \
                    player.current_zone == "reservoir a" or player.current_zone == "reservoir b" or \
                    player.current_zone == "reservoir c" or player.current_zone == "fishing hut":
                amuna_location.update(korlok_map_button.x_coordinate,
                                      korlok_map_button.y_coordinate,
                                      graphic_dict["amuna_location"])
            if player.current_zone == "eldream" or player.current_zone == "ectrenos" or \
                    player.current_zone == "ectrenos left" or player.current_zone == "ectrenos right" or \
                    player.current_zone == "ectrenos front" or player.current_zone == "ectrenos alcove" or \
                    player.current_zone == "altar" or player.current_zone == "fishing alcove":
                amuna_location.update(eldream_map_button.x_coordinate,
                                      eldream_map_button.y_coordinate,
                                      graphic_dict["amuna_location"])
            if player.current_zone == "marrow entrance" or player.current_zone == "marrow ramps west" or \
                    player.current_zone == "marrow ramps east" or player.current_zone == "marrow tower west" \
                    or player.current_zone == "marrow tower east" or player.current_zone == "marrow ramps west end" \
                    or player.current_zone == "marrow ramps east end" or player.current_zone == "marrow" \
                    or player.current_zone == "sub marrow":
                amuna_location.update(marrow_map_button.x_coordinate,
                                      marrow_map_button.y_coordinate,
                                      graphic_dict["amuna_location"])
            world_map_container.append(amuna_location)
        if player.gender == "female":
            if player.current_zone == "seldon":
                amuna_location.update(seldon_map_button.x_coordinate,
                                      seldon_map_button.y_coordinate,
                                      graphic_dict["amuna_female"])
            if player.current_zone == "rohir":
                amuna_location.update(seldon_map_button.x_coordinate,
                                      seldon_map_button.y_coordinate - 75,
                                      graphic_dict["amuna_female"])
            if player.current_zone == "stardust":
                amuna_location.update(seldon_map_button.x_coordinate - 75,
                                      seldon_map_button.y_coordinate - 25,
                                      graphic_dict["amuna_female"])
            if (player.current_zone == "korlok" or player.current_zone == "mines" or
                    player.current_zone == "terra trail" or player.current_zone == "fishing hut" or
                    player.current_zone == "reservoir a" or player.current_zone == "reservoir b" or
                    player.current_zone == "reservoir c" or player.current_zone == "forge" or
                    player.current_zone == "fishing hut"):
                amuna_location.update(korlok_map_button.x_coordinate,
                                      korlok_map_button.y_coordinate,
                                      graphic_dict["amuna_female"])
            if player.current_zone == "eldream" or player.current_zone == "ectrenos" or \
                    player.current_zone == "ectrenos left" or player.current_zone == "ectrenos right" or \
                    player.current_zone == "ectrenos front" or player.current_zone == "ectrenos alcove" or \
                    player.current_zone == "altar" or player.current_zone == "fishing alcove":
                amuna_location.update(eldream_map_button.x_coordinate,
                                      eldream_map_button.y_coordinate,
                                      graphic_dict["amuna_female"])
            if player.current_zone == "marrow entrance" or player.current_zone == "marrow ramps west" or \
                    player.current_zone == "marrow ramps east" or player.current_zone == "marrow tower west" \
                    or player.current_zone == "marrow tower east" or player.current_zone == "marrow ramps west end" \
                    or player.current_zone == "marrow ramps east end" or player.current_zone == "marrow" \
                    or player.current_zone == "sub marrow":
                amuna_location.update(marrow_map_button.x_coordinate,
                                      marrow_map_button.y_coordinate,
                                      graphic_dict["amuna_female"])
            world_map_container.append(amuna_location)
    if player.race == "nuldar":
        if player.gender == "male":
            if player.current_zone == "seldon":
                nuldar_location.update(seldon_map_button.x_coordinate,
                                       seldon_map_button.y_coordinate,
                                       graphic_dict["nuldar_location"])
            if player.current_zone == "rohir":
                nuldar_location.update(seldon_map_button.x_coordinate,
                                       seldon_map_button.y_coordinate - 75,
                                       graphic_dict["nuldar_location"])
            if player.current_zone == "stardust":
                nuldar_location.update(seldon_map_button.x_coordinate - 75,
                                       seldon_map_button.y_coordinate - 25,
                                       graphic_dict["nuldar_location"])
            if (player.current_zone == "korlok" or player.current_zone == "mines"
                    or player.current_zone == "terra trail" or player.current_zone == "fishing hut"
                    or player.current_zone == "reservoir a" or player.current_zone == "reservoir b"
                    or player.current_zone == "reservoir c" or player.current_zone == "forge"
                    or player.current_zone == "fishing hut"):
                nuldar_location.update(korlok_map_button.x_coordinate,
                                       korlok_map_button.y_coordinate,
                                       graphic_dict["nuldar_location"])
            if player.current_zone == "eldream" or player.current_zone == "ectrenos" or \
                    player.current_zone == "ectrenos left" or player.current_zone == "ectrenos right" or \
                    player.current_zone == "ectrenos front" or player.current_zone == "ectrenos alcove" or \
                    player.current_zone == "altar" or player.current_zone == "fishing alcove":
                nuldar_location.update(eldream_map_button.x_coordinate,
                                       eldream_map_button.y_coordinate,
                                       graphic_dict["nuldar_location"])
            if player.current_zone == "marrow entrance" or player.current_zone == "marrow ramps west" or \
                    player.current_zone == "marrow ramps east" or player.current_zone == "marrow tower west" \
                    or player.current_zone == "marrow tower east" or player.current_zone == "marrow ramps west end" \
                    or player.current_zone == "marrow ramps east end" or player.current_zone == "marrow" \
                    or player.current_zone == "sub marrow":
                nuldar_location.update(marrow_map_button.x_coordinate,
                                       marrow_map_button.y_coordinate,
                                       graphic_dict["nuldar_location"])
            world_map_container.append(nuldar_location)
        if player.gender == "female":
            if player.current_zone == "seldon":
                nuldar_location.update(seldon_map_button.x_coordinate,
                                       seldon_map_button.y_coordinate,
                                       graphic_dict["nuldar_female"])
            if player.current_zone == "rohir":
                nuldar_location.update(seldon_map_button.x_coordinate,
                                       seldon_map_button.y_coordinate - 75,
                                       graphic_dict["nuldar_female"])
            if player.current_zone == "stardust":
                nuldar_location.update(seldon_map_button.x_coordinate - 75,
                                       seldon_map_button.y_coordinate - 25,
                                       graphic_dict["nuldar_female"])
            if (player.current_zone == "korlok" or player.current_zone == "mines" or
                    player.current_zone == "terra trail" or player.current_zone == "fishing hut" or
                    player.current_zone == "reservoir a" or player.current_zone == "reservoir b" or
                    player.current_zone == "reservoir c" or player.current_zone == "forge"
                    or player.current_zone == "fishing hut"):
                nuldar_location.update(korlok_map_button.x_coordinate,
                                       korlok_map_button.y_coordinate,
                                       graphic_dict["nuldar_female"])
            if player.current_zone == "eldream" or player.current_zone == "ectrenos" or \
                    player.current_zone == "ectrenos left" or player.current_zone == "ectrenos right" or \
                    player.current_zone == "ectrenos front" or player.current_zone == "ectrenos alcove" or \
                    player.current_zone == "altar" or player.current_zone == "fishing alcove":
                nuldar_location.update(eldream_map_button.x_coordinate,
                                       eldream_map_button.y_coordinate,
                                       graphic_dict["nuldar_female"])
            if player.current_zone == "marrow entrance" or player.current_zone == "marrow ramps west" or \
                    player.current_zone == "marrow ramps east" or player.current_zone == "marrow tower west" \
                    or player.current_zone == "marrow tower east" or player.current_zone == "marrow ramps west end" \
                    or player.current_zone == "marrow ramps east end" or player.current_zone == "marrow" \
                    or player.current_zone == "sub marrow":
                nuldar_location.update(marrow_map_button.x_coordinate,
                                       marrow_map_button.y_coordinate,
                                       graphic_dict["nuldar_female"])
            world_map_container.append(nuldar_location)
    if player.race == "sorae":
        if player.gender == "male":
            if player.current_zone == "seldon":
                sorae_location.update(seldon_map_button.x_coordinate,
                                      seldon_map_button.y_coordinate,
                                      graphic_dict["sorae_location"])
            if player.current_zone == "rohir":
                sorae_location.update(seldon_map_button.x_coordinate,
                                      seldon_map_button.y_coordinate - 75,
                                      graphic_dict["sorae_location"])
            if player.current_zone == "stardust":
                sorae_location.update(seldon_map_button.x_coordinate - 75,
                                      seldon_map_button.y_coordinate - 25,
                                      graphic_dict["sorae_location"])
            if (player.current_zone == "korlok" or player.current_zone == "mines" or
                    player.current_zone == "terra trail" or player.current_zone == "fishing hut"
                    or player.current_zone == "reservoir a" or player.current_zone == "reservoir b"
                    or player.current_zone == "reservoir c" or player.current_zone == "forge"
                    or player.current_zone == "fishing hut"):
                sorae_location.update(korlok_map_button.x_coordinate,
                                      korlok_map_button.y_coordinate,
                                      graphic_dict["sorae_location"])
            if player.current_zone == "eldream" or player.current_zone == "ectrenos" or \
                    player.current_zone == "ectrenos left" or player.current_zone == "ectrenos right" or \
                    player.current_zone == "ectrenos front" or player.current_zone == "ectrenos alcove" or \
                    player.current_zone == "altar" or player.current_zone == "fishing alcove":
                sorae_location.update(eldream_map_button.x_coordinate,
                                      eldream_map_button.y_coordinate,
                                      graphic_dict["sorae_location"])
            if player.current_zone == "marrow entrance" or player.current_zone == "marrow ramps west" or \
                    player.current_zone == "marrow ramps east" or player.current_zone == "marrow tower west" \
                    or player.current_zone == "marrow tower east" or player.current_zone == "marrow ramps west end" \
                    or player.current_zone == "marrow ramps east end" or player.current_zone == "marrow" \
                    or player.current_zone == "sub marrow":
                sorae_location.update(marrow_map_button.x_coordinate,
                                      marrow_map_button.y_coordinate,
                                      graphic_dict["sorae_location"])
            world_map_container.append(sorae_location)
        if player.gender == "female":
            if player.current_zone == "seldon":
                sorae_location.update(seldon_map_button.x_coordinate,
                                      seldon_map_button.y_coordinate,
                                      graphic_dict["sorae_b"])
            if player.current_zone == "rohir":
                sorae_location.update(seldon_map_button.x_coordinate,
                                      seldon_map_button.y_coordinate - 75,
                                      graphic_dict["sorae_b"])
            if player.current_zone == "stardust":
                sorae_location.update(seldon_map_button.x_coordinate - 75,
                                      seldon_map_button.y_coordinate - 25,
                                      graphic_dict["sorae_b"])
            if (player.current_zone == "korlok" or player.current_zone == "mines" or
                    player.current_zone == "terra trail" or player.current_zone == "fishing hut"
                    or player.current_zone == "reservoir a" or player.current_zone == "reservoir b"
                    or player.current_zone == "reservoir c" or player.current_zone == "forge"
                    or player.current_zone == "fishing hut"):
                sorae_location.update(korlok_map_button.x_coordinate,
                                      korlok_map_button.y_coordinate,
                                      graphic_dict["sorae_b"])
            if player.current_zone == "eldream" or player.current_zone == "ectrenos" or \
                    player.current_zone == "ectrenos left" or player.current_zone == "ectrenos right" or \
                    player.current_zone == "ectrenos front" or player.current_zone == "ectrenos alcove" or \
                    player.current_zone == "altar" or player.current_zone == "fishing alcove":
                sorae_location.update(eldream_map_button.x_coordinate,
                                      eldream_map_button.y_coordinate,
                                      graphic_dict["sorae_b"])
            if player.current_zone == "marrow entrance" or player.current_zone == "marrow ramps west" or \
                    player.current_zone == "marrow ramps east" or player.current_zone == "marrow tower west" \
                    or player.current_zone == "marrow tower east" or player.current_zone == "marrow ramps west end" \
                    or player.current_zone == "marrow ramps east end" or player.current_zone == "marrow" \
                    or player.current_zone == "sub marrow":
                sorae_location.update(marrow_map_button.x_coordinate,
                                      marrow_map_button.y_coordinate,
                                      graphic_dict["sorae_b"])
            world_map_container.append(sorae_location)
