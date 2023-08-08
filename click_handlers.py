import drawing_functions


# getting event based on user click related to item info
def item_info_button(item_info_event, item_button, pygame, info_window, SCREEN_WIDTH, SCREEN_HEIGHT):
    if item_info_event.type == pygame.MOUSEBUTTONUP:

        init_pos = list(pygame.mouse.get_pos())
        ratio_x = (SCREEN_WIDTH / 1280)
        ratio_y = (SCREEN_HEIGHT / 720)
        item_info_mouse = (init_pos[0] / ratio_x, init_pos[1] / ratio_y)

        if item_button.rect.collidepoint(item_info_mouse):
            if len(drawing_functions.item_info_window) > 0:
                return "yes"
        else:
            if not info_window.rect.collidepoint(item_info_mouse):
                return "no"


# getting item player clicked based on it's name and return the corresponding item. for equipment
def equipment_event_item(player, equipment_event_here, pygame, basic_armor, forged_armor, mythical_armor,
                         legendary_armor, power_gloves, chroma_boots, SCREEN_WIDTH, SCREEN_HEIGHT):

    armor = pygame.Rect((1050, 170), (50, 50))
    gloves = pygame.Rect((1125, 170), (50, 50))
    boots = pygame.Rect((1200, 170), (50, 50))

    if equipment_event_here.type == pygame.MOUSEBUTTONUP:

        init_pos = list(pygame.mouse.get_pos())
        ratio_x = (SCREEN_WIDTH / 1280)
        ratio_y = (SCREEN_HEIGHT / 720)
        equipment_mouse = (init_pos[0] / ratio_x, init_pos[1] / ratio_y)

        if player.equipment["armor"] != "":
            if player.equipment["armor"].name == "basic armor":
                if armor.collidepoint(equipment_mouse):
                    return basic_armor
            if player.equipment["armor"].name == "forged armor":
                if armor.collidepoint(equipment_mouse):
                    return forged_armor
            if player.equipment["armor"].name == "mythical armor":
                if armor.collidepoint(equipment_mouse):
                    return mythical_armor
            if player.equipment["armor"].name == "legendary armor":
                if armor.collidepoint(equipment_mouse):
                    return legendary_armor

        if player.equipment["gloves"] != "":
            if player.equipment["gloves"].name == "power gloves":
                if gloves.collidepoint(equipment_mouse):
                    return power_gloves

        if player.equipment["boots"] != "":
            if player.equipment["boots"].name == "chroma boots":
                if boots.collidepoint(equipment_mouse):
                    return chroma_boots


# handles mouse clicks for equipment sub-screen
def equipment(player, event, pygame, basic_armor, forged_armor, mythical_armor, legendary_armor, power_gloves,
              chroma_boots, sfx_equip, SCREEN_WIDTH, SCREEN_HEIGHT, graphics):
    return_dict = {"equipment message": "", "gear checked": True}
    equipment_item = equipment_event_item(player, event, pygame, basic_armor, forged_armor, mythical_armor,
                                          legendary_armor, power_gloves, chroma_boots, SCREEN_WIDTH, SCREEN_HEIGHT)

    # if player clicks item in equipment sub-screen, un-equip the item and place in inventory, if inventory isn't full
    if equipment_item is not None:
        if equipment_item.name == "basic armor" or equipment_item.name == "forged armor" \
                or equipment_item.name == "mythical armor" or equipment_item.name == "legendary armor":
            if player.race == "amuna":
                if player.gender == "male":
                    if player.role == "mage":
                        player.surf = graphics["player_mage_amuna_male_down_1"]
                    if player.role == "fighter":
                        player.surf = graphics["player_fighter_amuna_male_down_1"]
                    if player.role == "scout":
                        player.surf = graphics["player_scout_amuna_male_down_1"]
                if player.gender == "female":
                    if player.role == "mage":
                        player.surf = graphics["player_mage_amuna_female_down_1"]
                    if player.role == "fighter":
                        player.surf = graphics["player_fighter_amuna_female_down_1"]
                    if player.role == "scout":
                        player.surf = graphics["player_scout_amuna_female_down_1"]
            if player.race == "nuldar":
                if player.gender == "male":
                    if player.role == "mage":
                        player.surf = graphics["player_mage_nuldar_male_down_1"]
                    if player.role == "fighter":
                        player.surf = graphics["player_fighter_nuldar_male_down_1"]
                    if player.role == "scout":
                        player.surf = graphics["player_scout_nuldar_male_down_1"]
                if player.gender == "female":
                    if player.role == "mage":
                        player.surf = graphics["player_mage_nuldar_female_down_1"]
                    if player.role == "fighter":
                        player.surf = graphics["player_fighter_nuldar_female_down_1"]
                    if player.role == "scout":
                        player.surf = graphics["player_scout_nuldar_female_down_1"]
            if player.race == "sorae":
                if player.gender == "male":
                    if player.role == "mage":
                        player.surf = graphics["player_mage_sorae_a_down_1"]
                    if player.role == "fighter":
                        player.surf = graphics["player_fighter_sorae_a_down_1"]
                    if player.role == "scout":
                        player.surf = graphics["player_scout_sorae_a_down_1"]
                if player.gender == "female":
                    if player.role == "mage":
                        player.surf = graphics["player_mage_sorae_b_down_1"]
                    if player.role == "fighter":
                        player.surf = graphics["player_fighter_sorae_b_down_1"]
                    if player.role == "scout":
                        player.surf = graphics["player_scout_sorae_b_down_1"]

        if equipment_item.name == "basic armor":
            if len(player.items) < 16:
                player.items.append(equipment_item)
                player.equipment["armor"] = ""
                pygame.mixer.find_channel(True).play(sfx_equip)
                return_dict["equipment message"] = "Basic Armor un-equipped."
                player.defense = 0
            else:
                return_dict["equipment message"] = "Your inventory is full."
        if equipment_item.name == "forged armor":
            if len(player.items) < 16:
                player.items.append(equipment_item)
                player.equipment["armor"] = ""
                pygame.mixer.find_channel(True).play(sfx_equip)
                return_dict["equipment message"] = "Forged Armor un-equipped."
                player.defense = 0
            else:
                return_dict["equipment message"] = "Your inventory is full."
        if equipment_item.name == "mythical armor":
            if len(player.items) < 16:
                player.items.append(equipment_item)
                player.equipment["armor"] = ""
                pygame.mixer.find_channel(True).play(sfx_equip)
                return_dict["equipment message"] = "Mythical Armor un-equipped."
                player.defense = 0
            else:
                return_dict["equipment message"] = "Your inventory is full."
        if equipment_item.name == "legendary armor":
            if len(player.items) < 16:
                player.items.append(equipment_item)
                player.equipment["armor"] = ""
                pygame.mixer.find_channel(True).play(sfx_equip)
                return_dict["equipment message"] = "Legendary Armor un-equipped."
                player.defense = 0
            else:
                return_dict["equipment message"] = "Your inventory is full."

        if equipment_item.name == "power gloves":
            if len(player.items) < 16:
                player.items.append(equipment_item)
                player.equipment["gloves"] = ""
                pygame.mixer.find_channel(True).play(sfx_equip)
                return_dict["equipment message"] = "Power gloves un-equipped."
            else:
                return_dict["equipment message"] = "Your inventory is full."

        if equipment_item.name == "chroma boots":
            if len(player.items) < 16:
                player.items.append(equipment_item)
                player.equipment["boots"] = ""
                pygame.mixer.find_channel(True).play(sfx_equip)
                return_dict["equipment message"] = "Chroma boots un-equipped."
            else:
                return_dict["equipment message"] = "Your inventory is full."

    return return_dict


# getting item player clicked based on it's name and return the corresponding item. for inventory items
def inventory_event_item(inventory_event_here, pygame, SCREEN_WIDTH, SCREEN_HEIGHT):
    event_return = {"element": "", "clicked": False}
    if inventory_event_here.type == pygame.MOUSEBUTTONUP:

        init_pos = list(pygame.mouse.get_pos())
        ratio_x = (SCREEN_WIDTH / 1280)
        ratio_y = (SCREEN_HEIGHT / 720)
        inventory_mouse = (init_pos[0] / ratio_x, init_pos[1] / ratio_y)

        # list of sprites that collided with mouse cursor rect
        clicked_element = [inventory_element for inventory_element in drawing_functions.player_items
                           if inventory_element.rect.collidepoint(inventory_mouse)]
        # try to get inventory item player clicked based on it's name and return it
        try:
            if clicked_element[0].name == "big health potion":
                event_return["element"] = clicked_element[0]
                event_return["clicked"] = True
            if clicked_element[0].name == "big energy potion":
                event_return["element"] = clicked_element[0]
                event_return["clicked"] = True
            if clicked_element[0].name == "small health potion":
                event_return["element"] = clicked_element[0]
                event_return["clicked"] = True
            if clicked_element[0].name == "small energy potion":
                event_return["element"] = clicked_element[0]
                event_return["clicked"] = True
            if clicked_element[0].name == "super potion":
                event_return["element"] = clicked_element[0]
                event_return["clicked"] = True
            if clicked_element[0].name == "shiny rock":
                event_return["element"] = clicked_element[0]
                event_return["clicked"] = True
            if clicked_element[0].name == "bone dust":
                event_return["element"] = clicked_element[0]
                event_return["clicked"] = True
            if clicked_element[0].name == "cracked ember":
                event_return["element"] = clicked_element[0]
                event_return["clicked"] = True
            if clicked_element[0].name == "broken band":
                event_return["element"] = clicked_element[0]
                event_return["clicked"] = True
            if clicked_element[0].name == "dried fins":
                event_return["element"] = clicked_element[0]
                event_return["clicked"] = True
            if clicked_element[0].name == "oscura pluma":
                event_return["element"] = clicked_element[0]
                event_return["clicked"] = True
            if clicked_element[0].name == "basic armor":
                event_return["element"] = clicked_element[0]
                event_return["clicked"] = True
            if clicked_element[0].name == "forged armor":
                event_return["element"] = clicked_element[0]
                event_return["clicked"] = True
            if clicked_element[0].name == "mythical armor":
                event_return["element"] = clicked_element[0]
                event_return["clicked"] = True
            if clicked_element[0].name == "legendary armor":
                event_return["element"] = clicked_element[0]
                event_return["clicked"] = True
            if clicked_element[0].name == "temporary item":
                event_return["element"] = clicked_element[0]
                event_return["clicked"] = True
            if clicked_element[0].name == "boss key" or clicked_element[0].name == "ramps key":
                event_return["element"] = clicked_element[0]
                event_return["clicked"] = True
            if clicked_element[0].name == "power gloves":
                event_return["element"] = clicked_element[0]
                event_return["clicked"] = True
            if clicked_element[0].name == "chroma boots":
                event_return["element"] = clicked_element[0]
                event_return["clicked"] = True
            if clicked_element[0].name == "pet seed":
                event_return["element"] = clicked_element[0]
                event_return["clicked"] = True
            if clicked_element[0].type == "whistle":
                event_return["element"] = clicked_element[0]
                event_return["clicked"] = True
            if clicked_element[0].name == "pet cookie":
                event_return["element"] = clicked_element[0]
                event_return["clicked"] = True
            if clicked_element[0].name == "pet candy":
                event_return["element"] = clicked_element[0]
                event_return["clicked"] = True
            if clicked_element[0].name == "pet tart":
                event_return["element"] = clicked_element[0]
                event_return["clicked"] = True
            if clicked_element[0].name == "bone shard":
                event_return["element"] = clicked_element[0]
                event_return["clicked"] = True
            if clicked_element[0].name == "prism":
                event_return["element"] = clicked_element[0]
                event_return["clicked"] = True
            if clicked_element[0].name == "casing":
                event_return["element"] = clicked_element[0]
                event_return["clicked"] = True
            if clicked_element[0].name == "smelted casing":
                event_return["element"] = clicked_element[0]
                event_return["clicked"] = True
            if clicked_element[0].name == "enchanted casing":
                event_return["element"] = clicked_element[0]
                event_return["clicked"] = True
            if clicked_element[0].name == "seldon firework" or clicked_element[0].name == "korlok firework" \
                    or clicked_element[0].name == "eldream firework":
                event_return["element"] = clicked_element[0]
                event_return["clicked"] = True
            if clicked_element[0].name == "seldon bait" or clicked_element[0].name == "korlok bait" \
                    or clicked_element[0].name == "eldream bait":
                event_return["element"] = clicked_element[0]
                event_return["clicked"] = True
        except IndexError:
            pass
    return event_return


# handles mouse clicks for inventory sub-screen for items with actions
def inventory(pygame, player, item, sfx_potion, sfx_equip, sfx_whistle, sfx_snack, graphics, width, height,
              sfx_firework):

    return_dict = {"item message": ""}

    try:
        if item.name == "pet cookie":
            for pet in player.pet:
                if pet.name == "kasper":
                    if pet.energy < 100:
                        pygame.mixer.find_channel(True).play(sfx_snack)
                        drawing_functions.player_items.remove(item)
                        player.items.remove(item)
                        pet.energy += 50
                    if pet.energy >= 100:
                        pet.energy = 100
                        return_dict["item message"] = "Your kasper is full of energy."
        if item.name == "pet candy":
            for pet in player.pet:
                if pet.name == "torok":
                    if pet.energy < 100:
                        pygame.mixer.find_channel(True).play(sfx_snack)
                        drawing_functions.player_items.remove(item)
                        player.items.remove(item)
                        pet.energy += 50
                    if pet.energy >= 100:
                        pet.energy = 100
                        return_dict["item message"] = "Your torok is full of energy."
        if item.name == "pet tart":
            for pet in player.pet:
                if pet.name == "iriana":
                    if pet.energy < 100:
                        pygame.mixer.find_channel(True).play(sfx_snack)
                        drawing_functions.player_items.remove(item)
                        player.items.remove(item)
                        pet.energy += 50
                    if pet.energy >= 100:
                        pet.energy = 100
                        return_dict["item message"] = "Your iriana is full of energy."
        if item.name == "pet whistle kasper":
            pygame.mixer.find_channel(True).play(sfx_whistle)
            for pet in player.pet:
                if pet.name == "kasper":
                    match pet.active:
                        case True:
                            pet.active = False
                        case False:
                            pet.active = True
                            pet.update(player.x_coordinate + 25, player.y_coordinate - 25, width, height)
                # set other pets to de-active, so they don't overlap
                else:
                    match pet.active:
                        case True:
                            pet.active = False
        if item.name == "pet whistle torok":
            pygame.mixer.find_channel(True).play(sfx_whistle)
            for pet in player.pet:
                if pet.name == "torok":
                    match pet.active:
                        case True:
                            pet.active = False
                        case False:
                            pet.active = True
                            pet.update(player.x_coordinate + 25, player.y_coordinate - 25, width, height)
                else:
                    match pet.active:
                        case True:
                            pet.active = False
        if item.name == "pet whistle iriana":
            pygame.mixer.find_channel(True).play(sfx_whistle)
            for pet in player.pet:
                if pet.name == "iriana":
                    match pet.active:
                        case True:
                            pet.active = False
                        case False:
                            pet.active = True
                            pet.update(player.x_coordinate + 25, player.y_coordinate - 25, width, height)
                else:
                    match pet.active:
                        case True:
                            pet.active = False

        if item.name == "small health potion":
            if player.health == 100:
                return_dict["item message"] = "You're already at full health."
            else:
                pygame.mixer.find_channel(True).play(sfx_potion)
                player.health = player.health + 25
                if player.health > 100:
                    player.health = 100
                drawing_functions.player_items.remove(item)
                player.items.remove(item)
                return_dict["item message"] = "The potion heals you for 25 hp."
        if item.name == "small energy potion":
            if player.energy == 100:
                return_dict["item message"] = "You're already at full energy."
            else:
                pygame.mixer.find_channel(True).play(sfx_potion)
                player.energy = player.energy + 25
                if player.energy > 100:
                    player.energy = 100
                drawing_functions.player_items.remove(item)
                player.items.remove(item)
                return_dict["item message"] = "The potion energizes you for 25 en."
        if item.name == "big health potion":
            if player.health == 100:
                return_dict["item message"] = "You're already at full health."
            else:
                pygame.mixer.find_channel(True).play(sfx_potion)
                player.health = player.health + 50
                if player.health > 100:
                    player.health = 100
                drawing_functions.player_items.remove(item)
                player.items.remove(item)
                return_dict["item message"] = "The potion heals you for 50 hp."
        if item.name == "big energy potion":
            if player.energy == 100:
                return_dict["item message"] = "You're already at full energy."
            else:
                pygame.mixer.find_channel(True).play(sfx_potion)
                player.energy = player.energy + 50
                if player.energy > 100:
                    player.energy = 100
                drawing_functions.player_items.remove(item)
                player.items.remove(item)
                return_dict["item message"] = "The potion energizes you for 50 en."
        if item.name == "super potion":
            if player.health < 100 or player.energy < 100:
                pygame.mixer.find_channel(True).play(sfx_potion)
                player.health = player.health + 50
                player.energy = player.energy + 50
                if player.energy > 100:
                    player.energy = 100
                if player.health > 100:
                    player.health = 100
                drawing_functions.player_items.remove(item)
                player.items.remove(item)
                return_dict["item message"] = "The potion heals and energizes you."
            else:
                return_dict["item message"] = "You're already full health or energy."

        if item.name == "seldon firework" or item.name == "korlok firework" or item.name == "eldream firework":
            pygame.mixer.find_channel(True).play(sfx_firework)
            return_dict["item message"] = "boom shakalaka."
            return_dict["fireworking"] = True
            if item.name == "seldon firework":
                return_dict["firework_type"] = "seldon"
            if item.name == "korlok firework":
                return_dict["firework_type"] = "korlok"
            if item.name == "eldream firework":
                return_dict["firework_type"] = "eldream"
            drawing_functions.player_items.remove(item)
            player.items.remove(item)
        else:
            return_dict["fireworking"] = False
            return_dict["firework_type"] = ""

        if item.type == "armor":
            if player.equipment["armor"] == "":
                player.equipment["armor"] = item
                drawing_functions.player_items.remove(item)
                player.items.remove(item)
                pygame.mixer.find_channel(True).play(sfx_equip)
                return_dict["item message"] = "Armor equipped. "
                player.defense = item.level

                if player.equipment["armor"].name == "basic armor":
                    if player.race == "amuna":
                        if player.gender == "male":
                            if player.role == "mage":
                                player.surf = graphics["player_mage_amuna_male_down_1_basic"]
                            if player.role == "fighter":
                                player.surf = graphics["player_fighter_amuna_male_down_1_basic"]
                            if player.role == "scout":
                                player.surf = graphics["player_scout_amuna_male_down_1_basic"]
                        if player.gender == "female":
                            if player.role == "mage":
                                player.surf = graphics["player_mage_amuna_female_down_1_basic"]
                            if player.role == "fighter":
                                player.surf = graphics["player_fighter_amuna_female_down_1_basic"]
                            if player.role == "scout":
                                player.surf = graphics["player_scout_amuna_female_down_1_basic"]
                    if player.race == "nuldar":
                        if player.gender == "male":
                            if player.role == "mage":
                                player.surf = graphics["player_mage_nuldar_male_down_1_basic"]
                            if player.role == "fighter":
                                player.surf = graphics["player_fighter_nuldar_male_down_1_basic"]
                            if player.role == "scout":
                                player.surf = graphics["player_scout_nuldar_male_down_1_basic"]
                        if player.gender == "female":
                            if player.role == "mage":
                                player.surf = graphics["player_mage_nuldar_female_down_1_basic"]
                            if player.role == "fighter":
                                player.surf = graphics["player_fighter_nuldar_female_down_1_basic"]
                            if player.role == "scout":
                                player.surf = graphics["player_scout_nuldar_female_down_1_basic"]
                    if player.race == "sorae":
                        if player.gender == "male":
                            if player.role == "mage":
                                player.surf = graphics["player_mage_sorae_a_down_1_basic"]
                            if player.role == "fighter":
                                player.surf = graphics["player_fighter_sorae_a_down_1_basic"]
                            if player.role == "scout":
                                player.surf = graphics["player_scout_sorae_a_down_1_basic"]
                        if player.gender == "female":
                            if player.role == "mage":
                                player.surf = graphics["player_mage_sorae_b_down_1_basic"]
                            if player.role == "fighter":
                                player.surf = graphics["player_fighter_sorae_b_down_1_basic"]
                            if player.role == "scout":
                                player.surf = graphics["player_scout_sorae_b_down_1_basic"]
                if player.equipment["armor"].name == "forged armor":
                    if player.race == "amuna":
                        if player.gender == "male":
                            if player.role == "mage":
                                player.surf = graphics["player_mage_amuna_male_down_1_forged"]
                            if player.role == "fighter":
                                player.surf = graphics["player_fighter_amuna_male_down_1_forged"]
                            if player.role == "scout":
                                player.surf = graphics["player_scout_amuna_male_down_1_forged"]
                        if player.gender == "female":
                            if player.role == "mage":
                                player.surf = graphics["player_mage_amuna_female_down_1_forged"]
                            if player.role == "fighter":
                                player.surf = graphics["player_fighter_amuna_female_down_1_forged"]
                            if player.role == "scout":
                                player.surf = graphics["player_scout_amuna_female_down_1_forged"]
                    if player.race == "nuldar":
                        if player.gender == "male":
                            if player.role == "mage":
                                player.surf = graphics["player_mage_nuldar_male_down_1_forged"]
                            if player.role == "fighter":
                                player.surf = graphics["player_fighter_nuldar_male_down_1_forged"]
                            if player.role == "scout":
                                player.surf = graphics["player_scout_nuldar_male_down_1_forged"]
                        if player.gender == "female":
                            if player.role == "mage":
                                player.surf = graphics["player_mage_nuldar_female_down_1_forged"]
                            if player.role == "fighter":
                                player.surf = graphics["player_fighter_nuldar_female_down_1_forged"]
                            if player.role == "scout":
                                player.surf = graphics["player_scout_nuldar_female_down_1_forged"]
                    if player.race == "sorae":
                        if player.gender == "male":
                            if player.role == "mage":
                                player.surf = graphics["player_mage_sorae_a_down_1_forged"]
                            if player.role == "fighter":
                                player.surf = graphics["player_fighter_sorae_a_down_1_forged"]
                            if player.role == "scout":
                                player.surf = graphics["player_scout_sorae_a_down_1_forged"]
                        if player.gender == "female":
                            if player.role == "mage":
                                player.surf = graphics["player_mage_sorae_b_down_1_forged"]
                            if player.role == "fighter":
                                player.surf = graphics["player_fighter_sorae_b_down_1_forged"]
                            if player.role == "scout":
                                player.surf = graphics["player_scout_sorae_b_down_1_forged"]
                if player.equipment["armor"].name == "mythical armor":
                    if player.race == "amuna":
                        if player.gender == "male":
                            if player.role == "mage":
                                player.surf = graphics["player_mage_amuna_male_down_1_mythic"]
                            if player.role == "fighter":
                                player.surf = graphics["player_fighter_amuna_male_down_1_mythic"]
                            if player.role == "scout":
                                player.surf = graphics["player_scout_amuna_male_down_1_mythic"]
                        if player.gender == "female":
                            if player.role == "mage":
                                player.surf = graphics["player_mage_amuna_female_down_1_mythic"]
                            if player.role == "fighter":
                                player.surf = graphics["player_fighter_amuna_female_down_1_mythic"]
                            if player.role == "scout":
                                player.surf = graphics["player_scout_amuna_female_down_1_mythic"]
                    if player.race == "nuldar":
                        if player.gender == "male":
                            if player.role == "mage":
                                player.surf = graphics["player_mage_nuldar_male_down_1_mythic"]
                            if player.role == "fighter":
                                player.surf = graphics["player_fighter_nuldar_male_down_1_mythic"]
                            if player.role == "scout":
                                player.surf = graphics["player_scout_nuldar_male_down_1_mythic"]
                        if player.gender == "female":
                            if player.role == "mage":
                                player.surf = graphics["player_mage_nuldar_female_down_1_mythic"]
                            if player.role == "fighter":
                                player.surf = graphics["player_fighter_nuldar_female_down_1_mythic"]
                            if player.role == "scout":
                                player.surf = graphics["player_scout_nuldar_female_down_1_mythic"]
                    if player.race == "sorae":
                        if player.gender == "male":
                            if player.role == "mage":
                                player.surf = graphics["player_mage_sorae_a_down_1_mythic"]
                            if player.role == "fighter":
                                player.surf = graphics["player_fighter_sorae_a_down_1_mythic"]
                            if player.role == "scout":
                                player.surf = graphics["player_scout_sorae_a_down_1_mythic"]
                        if player.gender == "female":
                            if player.role == "mage":
                                player.surf = graphics["player_mage_sorae_b_down_1_mythic"]
                            if player.role == "fighter":
                                player.surf = graphics["player_fighter_sorae_b_down_1_mythic"]
                            if player.role == "scout":
                                player.surf = graphics["player_scout_sorae_b_down_1_mythic"]
                if player.equipment["armor"].name == "legendary armor":
                    if player.race == "amuna":
                        if player.gender == "male":
                            if player.role == "mage":
                                player.surf = graphics["player_mage_amuna_male_down_1_legend"]
                            if player.role == "fighter":
                                player.surf = graphics["player_fighter_amuna_male_down_1_legend"]
                            if player.role == "scout":
                                player.surf = graphics["player_scout_amuna_male_down_1_legend"]
                        if player.gender == "female":
                            if player.role == "mage":
                                player.surf = graphics["player_mage_amuna_female_down_1_legend"]
                            if player.role == "fighter":
                                player.surf = graphics["player_fighter_amuna_female_down_1_legend"]
                            if player.role == "scout":
                                player.surf = graphics["player_scout_amuna_female_down_1_legend"]
                    if player.race == "nuldar":
                        if player.gender == "male":
                            if player.role == "mage":
                                player.surf = graphics["player_mage_nuldar_male_down_1_legend"]
                            if player.role == "fighter":
                                player.surf = graphics["player_fighter_nuldar_male_down_1_legend"]
                            if player.role == "scout":
                                player.surf = graphics["player_scout_nuldar_male_down_1_legend"]
                        if player.gender == "female":
                            if player.role == "mage":
                                player.surf = graphics["player_mage_nuldar_female_down_1_legend"]
                            if player.role == "fighter":
                                player.surf = graphics["player_fighter_nuldar_female_down_1_legend"]
                            if player.role == "scout":
                                player.surf = graphics["player_scout_nuldar_female_down_1_legend"]
                    if player.race == "sorae":
                        if player.gender == "male":
                            if player.role == "mage":
                                player.surf = graphics["player_mage_sorae_a_down_1_legend"]
                            if player.role == "fighter":
                                player.surf = graphics["player_fighter_sorae_a_down_1_legend"]
                            if player.role == "scout":
                                player.surf = graphics["player_scout_sorae_a_down_1_legend"]
                        if player.gender == "female":
                            if player.role == "mage":
                                player.surf = graphics["player_mage_sorae_b_down_1_legend"]
                            if player.role == "fighter":
                                player.surf = graphics["player_fighter_sorae_b_down_1_legend"]
                            if player.role == "scout":
                                player.surf = graphics["player_scout_sorae_b_down_1_legend"]
            else:
                return_dict["item message"] = "Un-equip your current gear first."

        if item.name == "power gloves":
            if player.equipment["gloves"] == "":
                player.equipment["gloves"] = item
                pygame.mixer.find_channel(True).play(sfx_equip)
                drawing_functions.player_items.remove(item)
                player.items.remove(item)
                return_dict["item message"] = "Power gloves equipped."
            else:
                return_dict["item message"] = "Un-equip your current gear first."
        if item.name == "chroma boots":
            if player.equipment["boots"] == "":
                player.equipment["boots"] = item
                pygame.mixer.find_channel(True).play(sfx_equip)
                drawing_functions.player_items.remove(item)
                player.items.remove(item)
                return_dict["item message"] = "Chroma boots equipped."
            else:
                return_dict["item message"] = "Un-equip your current gear first."

    except AttributeError:
        pass

    return return_dict


# getting event based on user click related to combat scenario
def combat_event_button(combat_event, no_role_attack, mage_attack, fighter_attack, scout_attack,
                        barrier_button, strike_button, sense_button, pygame, SCREEN_WIDTH, SCREEN_HEIGHT,
                        mirror_button, stun_button, vanish_button):
    if combat_event.type == pygame.MOUSEBUTTONUP:

        init_pos = list(pygame.mouse.get_pos())
        ratio_x = (SCREEN_WIDTH / 1280)
        ratio_y = (SCREEN_HEIGHT / 720)
        combat_mouse = (init_pos[0] / ratio_x, init_pos[1] / ratio_y)

        if no_role_attack.rect.collidepoint(combat_mouse):
            return "attack"
        if mage_attack.rect.collidepoint(combat_mouse):
            return "attack"
        if fighter_attack.rect.collidepoint(combat_mouse):
            return "attack"
        if scout_attack.rect.collidepoint(combat_mouse):
            return "attack"
        if barrier_button.rect.collidepoint(combat_mouse):
            return "skill 1"
        if strike_button.rect.collidepoint(combat_mouse):
            return "skill 1"
        if sense_button.rect.collidepoint(combat_mouse):
            return "skill 1"
        if mirror_button.rect.collidepoint(combat_mouse):
            return "skill 2"
        if stun_button.rect.collidepoint(combat_mouse):
            return "skill 2"
        if vanish_button.rect.collidepoint(combat_mouse):
            return "skill 2"


# getting event based on user click related to npc
def npc_event_button(npc_event, quest_button, leave_button, pygame, sfx_page, SCREEN_WIDTH, SCREEN_HEIGHT):
    if npc_event.type == pygame.MOUSEBUTTONUP:

        init_pos = list(pygame.mouse.get_pos())
        ratio_x = (SCREEN_WIDTH / 1280)
        ratio_y = (SCREEN_HEIGHT / 720)
        npc_mouse = (init_pos[0] / ratio_x, init_pos[1] / ratio_y)

        if quest_button.rect.collidepoint(npc_mouse):
            pygame.mixer.find_channel(True).play(sfx_page)
            return "quest"
        if leave_button.rect.collidepoint(npc_mouse):
            return "leave"


# getting event based on user click related to quest window
def quest_event_button(quest_event, accept_button, decline_button, pygame, SCREEN_WIDTH, SCREEN_HEIGHT):
    if quest_event.type == pygame.MOUSEBUTTONUP:

        init_pos = list(pygame.mouse.get_pos())
        ratio_x = (SCREEN_WIDTH / 1280)
        ratio_y = (SCREEN_HEIGHT / 720)
        quest_mouse = (init_pos[0] / ratio_x, init_pos[1] / ratio_y)

        if accept_button.rect.collidepoint(quest_mouse):
            return "accept"
        if decline_button.rect.collidepoint(quest_mouse):
            return "decline"


def npc_event_button_fishing(npc_event, quest_button, leave_button, pygame, sfx_page, SCREEN_WIDTH, SCREEN_HEIGHT):
    if npc_event.type == pygame.MOUSEBUTTONUP:

        init_pos = list(pygame.mouse.get_pos())
        ratio_x = (SCREEN_WIDTH / 1280)
        ratio_y = (SCREEN_HEIGHT / 720)
        npc_mouse = (init_pos[0] / ratio_x, init_pos[1] / ratio_y)

        if quest_button.rect.collidepoint(npc_mouse):
            pygame.mixer.find_channel(True).play(sfx_page)
            return "quest"
        if leave_button.rect.collidepoint(npc_mouse):
            return "leave"


# getting event based on user click related to quest window
def quest_event_button_fishing(quest_event, accept_button, decline_button, pygame, SCREEN_WIDTH, SCREEN_HEIGHT):
    if quest_event.type == pygame.MOUSEBUTTONUP:

        init_pos = list(pygame.mouse.get_pos())
        ratio_x = (SCREEN_WIDTH / 1280)
        ratio_y = (SCREEN_HEIGHT / 720)
        quest_mouse = (init_pos[0] / ratio_x, init_pos[1] / ratio_y)

        if accept_button.rect.collidepoint(quest_mouse):
            return "accept"
        if decline_button.rect.collidepoint(quest_mouse):
            return "decline"


# getting event based on user click related to shop
def stardust_upgrade_event(stardust_event, offense_button, pygame, SCREEN_WIDTH, SCREEN_HEIGHT):
    if stardust_event.type == pygame.MOUSEBUTTONUP:

        init_pos = list(pygame.mouse.get_pos())
        ratio_x = (SCREEN_WIDTH / 1280)
        ratio_y = (SCREEN_HEIGHT / 720)
        stardust_mouse = (init_pos[0] / ratio_x, init_pos[1] / ratio_y)

        if offense_button.rect.collidepoint(stardust_mouse):
            return "offense"


# getting event based on user click related to shop
def shop_event_button(shop_event, buy_button, leave_button, pygame, sfx_paper, SCREEN_WIDTH, SCREEN_HEIGHT):
    if shop_event.type == pygame.MOUSEBUTTONUP:

        init_pos = list(pygame.mouse.get_pos())
        ratio_x = (SCREEN_WIDTH / 1280)
        ratio_y = (SCREEN_HEIGHT / 720)
        shop_mouse = (init_pos[0] / ratio_x, init_pos[1] / ratio_y)

        if buy_button.rect.collidepoint(shop_mouse):
            pygame.mixer.find_channel(True).play(sfx_paper)
            return "buy"
        if leave_button.rect.collidepoint(shop_mouse):
            return "leave"


# getting event based on user click related to shop
def shop_sell_button(shop_sell_event, yes_button, pygame, info_window, SCREEN_WIDTH, SCREEN_HEIGHT):
    if shop_sell_event.type == pygame.MOUSEBUTTONUP:

        init_pos = list(pygame.mouse.get_pos())
        ratio_x = (SCREEN_WIDTH / 1280)
        ratio_y = (SCREEN_HEIGHT / 720)
        shop_sell_mouse = (init_pos[0] / ratio_x, init_pos[1] / ratio_y)

        if yes_button.rect.collidepoint(shop_sell_mouse):
            return "yes"
        else:
            if not info_window.rect.collidepoint(shop_sell_mouse):
                return "no"


# getting event based on user click related to shop
def shop_buy_button(shop_buy_event, yes_button, pygame, SCREEN_WIDTH, SCREEN_HEIGHT):
    if shop_buy_event.type == pygame.MOUSEBUTTONUP:

        init_pos = list(pygame.mouse.get_pos())
        ratio_x = (SCREEN_WIDTH / 1280)
        ratio_y = (SCREEN_HEIGHT / 720)
        shop_buy_mouse = (init_pos[0] / ratio_x, init_pos[1] / ratio_y)

        if yes_button.rect.collidepoint(shop_buy_mouse):
            return "yes"
        else:
            return "no"


# getting event based on user click related to inn
def inn_event_button(inn_event, rest_button, leave_button, pygame, sfx_sleep, SCREEN_WIDTH, SCREEN_HEIGHT):
    if inn_event.type == pygame.MOUSEBUTTONUP:

        init_pos = list(pygame.mouse.get_pos())
        ratio_x = (SCREEN_WIDTH / 1280)
        ratio_y = (SCREEN_HEIGHT / 720)
        inn_mouse = (init_pos[0] / ratio_x, init_pos[1] / ratio_y)

        if rest_button.rect.collidepoint(inn_mouse):
            pygame.mixer.find_channel(True).play(sfx_sleep)
            return "rest"
        if leave_button.rect.collidepoint(inn_mouse):
            return "leave"


# getting event based on user click related to academia skill buttons
def academia_event_button(academia_event, mage_learn, fighter_learn, scout_learn, leave_button, pygame, sfx_paper,
                          SCREEN_WIDTH, SCREEN_HEIGHT):
    if academia_event.type == pygame.MOUSEBUTTONUP:

        init_pos = list(pygame.mouse.get_pos())
        ratio_x = (SCREEN_WIDTH / 1280)
        ratio_y = (SCREEN_HEIGHT / 720)
        academia_mouse = (init_pos[0] / ratio_x, init_pos[1] / ratio_y)

        if mage_learn.rect.collidepoint(academia_mouse):
            pygame.mixer.find_channel(True).play(sfx_paper)
            return "mage learn"
        if fighter_learn.rect.collidepoint(academia_mouse):
            pygame.mixer.find_channel(True).play(sfx_paper)
            return "fighter learn"
        if scout_learn.rect.collidepoint(academia_mouse):
            pygame.mixer.find_channel(True).play(sfx_paper)
            return "scout learn"
        if leave_button.rect.collidepoint(academia_mouse):
            return "leave"


# getting item player clicked based on it's name and return the corresponding item. for buying items
def buy_event_item(buy_event, shopkeeper_items, pygame, sfx_item, SCREEN_WIDTH, SCREEN_HEIGHT):
    if buy_event.type == pygame.MOUSEBUTTONUP:

        init_pos = list(pygame.mouse.get_pos())
        ratio_x = (SCREEN_WIDTH / 1280)
        ratio_y = (SCREEN_HEIGHT / 720)
        buy_mouse = (init_pos[0] / ratio_x, init_pos[1] / ratio_y)

        # list of sprites that collided with mouse cursor rect
        clicked_element = [buy_element for buy_element in shopkeeper_items if buy_element.rect.collidepoint(buy_mouse)]
        # try to get inventory item player clicked based on it's name and return it
        try:
            if clicked_element[0].name == "small health potion":
                pygame.mixer.find_channel(True).play(sfx_item)
                return clicked_element[0]
            if clicked_element[0].name == "small energy potion":
                pygame.mixer.find_channel(True).play(sfx_item)
                return clicked_element[0]
            if clicked_element[0].name == "shiny rock":
                pygame.mixer.find_channel(True).play(sfx_item)
                return clicked_element[0]
            if clicked_element[0].name == "bone dust":
                pygame.mixer.find_channel(True).play(sfx_item)
                return clicked_element[0]
            if clicked_element[0].name == "basic armor":
                pygame.mixer.find_channel(True).play(sfx_item)
                return clicked_element[0]
            if clicked_element[0].name == "forged armor":
                pygame.mixer.find_channel(True).play(sfx_item)
                return clicked_element[0]
            if clicked_element[0].name == "mythical armor":
                pygame.mixer.find_channel(True).play(sfx_item)
                return clicked_element[0]
            if clicked_element[0].name == "pet cookie":
                pygame.mixer.find_channel(True).play(sfx_item)
                return clicked_element[0]
            if clicked_element[0].name == "pet candy":
                pygame.mixer.find_channel(True).play(sfx_item)
                return clicked_element[0]
            if clicked_element[0].name == "pet tart":
                pygame.mixer.find_channel(True).play(sfx_item)
                return clicked_element[0]
            if clicked_element[0].name == "seldon firework":
                pygame.mixer.find_channel(True).play(sfx_item)
                return clicked_element[0]
            if clicked_element[0].name == "korlok firework":
                pygame.mixer.find_channel(True).play(sfx_item)
                return clicked_element[0]
            if clicked_element[0].name == "eldream firework":
                pygame.mixer.find_channel(True).play(sfx_item)
                return clicked_element[0]
            if clicked_element[0].name == "seldon bait":
                pygame.mixer.find_channel(True).play(sfx_item)
                return clicked_element[0]
            if clicked_element[0].name == "korlok bait":
                pygame.mixer.find_channel(True).play(sfx_item)
                return clicked_element[0]
            if clicked_element[0].name == "eldream bait":
                pygame.mixer.find_channel(True).play(sfx_item)
                return clicked_element[0]

        except IndexError:
            pass


# getting item player clicked based on it's name and return the corresponding item. for selling items
def sell_event_item(sell_event, pygame, sfx_item, SCREEN_WIDTH, SCREEN_HEIGHT):
    if sell_event.type == pygame.MOUSEBUTTONUP:

        init_pos = list(pygame.mouse.get_pos())
        ratio_x = (SCREEN_WIDTH / 1280)
        ratio_y = (SCREEN_HEIGHT / 720)
        sell_mouse = (init_pos[0] / ratio_x, init_pos[1] / ratio_y)

        # list of sprites that collided with mouse cursor rect
        clicked_element = [sell_element for sell_element in drawing_functions.player_items if
                           sell_element.rect.collidepoint(sell_mouse)]
        # try to get inventory item player clicked based on it's name and return it
        try:
            if clicked_element[0].name == "small health potion":
                pygame.mixer.find_channel(True).play(sfx_item)
                return clicked_element[0]
            if clicked_element[0].name == "small energy potion":
                pygame.mixer.find_channel(True).play(sfx_item)
                return clicked_element[0]
            if clicked_element[0].name == "shiny rock":
                pygame.mixer.find_channel(True).play(sfx_item)
                return clicked_element[0]
            if clicked_element[0].name == "bone dust":
                pygame.mixer.find_channel(True).play(sfx_item)
                return clicked_element[0]
            if clicked_element[0].name == "cracked ember":
                pygame.mixer.find_channel(True).play(sfx_item)
                return clicked_element[0]
            if clicked_element[0].name == "broken band":
                pygame.mixer.find_channel(True).play(sfx_item)
                return clicked_element[0]
            if clicked_element[0].name == "dried fins":
                pygame.mixer.find_channel(True).play(sfx_item)
                return clicked_element[0]
            if clicked_element[0].name == "oscura pluma":
                pygame.mixer.find_channel(True).play(sfx_item)
                return clicked_element[0]
            if clicked_element[0].name == "basic armor":
                pygame.mixer.find_channel(True).play(sfx_item)
                return clicked_element[0]
            if clicked_element[0].name == "forged armor":
                pygame.mixer.find_channel(True).play(sfx_item)
                return clicked_element[0]
            if clicked_element[0].name == "mythical armor":
                pygame.mixer.find_channel(True).play(sfx_item)
                return clicked_element[0]
            if clicked_element[0].name == "legendary armor":
                pygame.mixer.find_channel(True).play(sfx_item)
                return clicked_element[0]
            if clicked_element[0].name == "pet cookie":
                pygame.mixer.find_channel(True).play(sfx_item)
                return clicked_element[0]
            if clicked_element[0].name == "pet candy":
                pygame.mixer.find_channel(True).play(sfx_item)
                return clicked_element[0]
            if clicked_element[0].name == "pet tart":
                pygame.mixer.find_channel(True).play(sfx_item)
                return clicked_element[0]
            if clicked_element[0].name == "bone shard":
                pygame.mixer.find_channel(True).play(sfx_item)
                return clicked_element[0]
            if clicked_element[0].name == "seldon firework":
                pygame.mixer.find_channel(True).play(sfx_item)
                return clicked_element[0]
            if clicked_element[0].name == "korlok firework":
                pygame.mixer.find_channel(True).play(sfx_item)
                return clicked_element[0]
            if clicked_element[0].name == "eldream firework":
                pygame.mixer.find_channel(True).play(sfx_item)
                return clicked_element[0]
            if clicked_element[0].name == "seldon bait":
                pygame.mixer.find_channel(True).play(sfx_item)
                return clicked_element[0]
            if clicked_element[0].name == "korlok bait":
                pygame.mixer.find_channel(True).play(sfx_item)
                return clicked_element[0]
            if clicked_element[0].name == "eldream bait":
                pygame.mixer.find_channel(True).play(sfx_item)
                return clicked_element[0]

        except IndexError:
            pass


# getting item player clicked based on it's name and return the corresponding item
def skill_learn_event_item(skill_learn_event, skill_learn_items, pygame, SCREEN_WIDTH, SCREEN_HEIGHT):
    if skill_learn_event.type == pygame.MOUSEBUTTONUP:

        init_pos = list(pygame.mouse.get_pos())
        ratio_x = (SCREEN_WIDTH / 1280)
        ratio_y = (SCREEN_HEIGHT / 720)
        skill_learn_mouse = (init_pos[0] / ratio_x, init_pos[1] / ratio_y)

        # list of sprites that collided with mouse cursor rect
        skill_learn_element = [skill_learn_element for skill_learn_element in skill_learn_items if
                               skill_learn_element.rect.collidepoint(skill_learn_mouse)]
        # try to get skill player clicked based on it's name and return it
        try:
            if skill_learn_element[0].name == "barrier learn button":
                return skill_learn_element[0]
            if skill_learn_element[0].name == "hard strike learn button":
                return skill_learn_element[0]
            if skill_learn_element[0].name == "sharp sense learn button":
                return skill_learn_element[0]
            if skill_learn_element[0].name == "mirror learn button":
                return skill_learn_element[0]
            if skill_learn_element[0].name == "stun learn button":
                return skill_learn_element[0]
            if skill_learn_element[0].name == "vanish learn button":
                return skill_learn_element[0]

            if skill_learn_element[0].name == "close button":
                return skill_learn_element[0]
        except IndexError:
            pass
