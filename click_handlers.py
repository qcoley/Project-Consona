import drawing_functions


# getting event based on user click related to item info
def item_info_button(item_info_event, item_button, pygame, info_window):
    if item_info_event.type == pygame.MOUSEBUTTONUP:
        item_info_mouse = pygame.mouse.get_pos()
        if item_button.rect.collidepoint(item_info_mouse):
            return "yes"
        else:
            if not info_window.rect.collidepoint(item_info_mouse):
                return "no"


# getting item player clicked based on it's name and return the corresponding item. for equipment
def equipment_event_item(equipment_event_here, pygame):
    if equipment_event_here.type == pygame.MOUSEBUTTONUP:
        equipment_mouse = pygame.mouse.get_pos()
        # list of sprites that collided with mouse cursor rect
        clicked_element = [equipment_element for equipment_element in drawing_functions.player_equipment
                           if equipment_element.rect.collidepoint(equipment_mouse)]
        # try to get equipment item player clicked based on it's name and return it
        try:
            if clicked_element[0].name == "basic staff":
                return clicked_element[0]
            if clicked_element[0].name == "basic sword":
                return clicked_element[0]
            if clicked_element[0].name == "basic bow":
                return clicked_element[0]
            if clicked_element[0].name == "basic robes":
                return clicked_element[0]
            if clicked_element[0].name == "basic armor":
                return clicked_element[0]
            if clicked_element[0].name == "basic tunic":
                return clicked_element[0]
            if clicked_element[0].name == "power gloves":
                return clicked_element[0]
        except IndexError:
            pass


# handles mouse clicks for equipment sub-screen
def equipment(player, event, pygame, offense_upgraded, defense_upgraded, player_no_role_amuna_down_1,
              player_no_role_nuldar_down_1, player_no_role_sorae_down_1):
    return_dict = {"equipment message": "", "gear checked": True, "weapon checked": True}
    equipment_item = equipment_event_item(event, pygame)

    # if player clicks item in equipment sub-screen, un-equip the item and place in inventory, if inventory isn't full
    try:
        if equipment_item.name == "basic staff":
            if len(player.items) < 15:
                player.items.append(equipment_item)
                player.equipment["weapon"] = ""
                # remove gear along with weapon when weapon is clicked. Add both to inventory
                if player.equipment["torso"] != "":
                    player.items.append(player.equipment["torso"])
                    player.equipment["torso"] = ""
                return_dict["equipment message"] = "Basic Staff weapon un-equipped."
                # set players role to none when weapon is unequipped. adjust stats accordingly
                player.role = ""
                if player.race == "amuna":
                    player.surf = player_no_role_amuna_down_1
                if player.race == "nuldar":
                    player.surf = player_no_role_nuldar_down_1
                if player.race == "sorae":
                    player.surf = player_no_role_sorae_down_1
                player.offense = 0
                player.defense = 0
                if offense_upgraded == 1:
                    player.offense += 10
                if defense_upgraded == 1:
                    player.defense += 4
            else:
                return_dict["equipment message"] = "You need two open inventory slots."
        if equipment_item.name == "basic sword":
            if len(player.items) < 15:
                player.items.append(equipment_item)
                player.equipment["weapon"] = ""
                if player.equipment["torso"] != "":
                    player.items.append(player.equipment["torso"])
                    player.equipment["torso"] = ""
                return_dict["equipment message"] = "Basic Sword weapon un-equipped."
                player.role = ""
                if player.race == "amuna":
                    player.surf = player_no_role_amuna_down_1
                if player.race == "nuldar":
                    player.surf = player_no_role_nuldar_down_1
                if player.race == "sorae":
                    player.surf = player_no_role_sorae_down_1
                player.offense = 0
                player.defense = 0
                if offense_upgraded == 1:
                    player.offense += 10
                if defense_upgraded == 1:
                    player.defense += 4
            else:
                return_dict["equipment message"] = "You need two open inventory slots."
        if equipment_item.name == "basic bow":
            if len(player.items) < 15:
                player.items.append(equipment_item)
                player.equipment["weapon"] = ""
                if player.equipment["torso"] != "":
                    player.items.append(player.equipment["torso"])
                    player.equipment["torso"] = ""
                return_dict["equipment message"] = "Basic Bow weapon un-equipped."
                player.role = ""
                if player.race == "amuna":
                    player.surf = player_no_role_amuna_down_1
                if player.race == "nuldar":
                    player.surf = player_no_role_nuldar_down_1
                if player.race == "sorae":
                    player.surf = player_no_role_sorae_down_1
                player.offense = 0
                player.defense = 0
                if offense_upgraded == 1:
                    player.offense += 10
                if defense_upgraded == 1:
                    player.defense += 4
            else:
                return_dict["equipment message"] = "You need two open inventory slots."
        if equipment_item.name == "basic robes":
            if len(player.items) < 16:
                player.items.append(equipment_item)
                player.equipment["torso"] = ""
                return_dict["equipment message"] = "Basic Robes torso un-equipped."
                player.defense = 0
                if defense_upgraded == 1:
                    player.defense += 4
            else:
                return_dict["equipment message"] = "Your inventory is full."
        if equipment_item.name == "basic armor":
            if len(player.items) < 16:
                player.items.append(equipment_item)
                player.equipment["torso"] = ""
                return_dict["equipment message"] = "Basic Armor torso un-equipped."
                player.defense = 0
                if defense_upgraded == 1:
                    player.defense += 4
            else:
                return_dict["equipment message"] = "Your inventory is full."
        if equipment_item.name == "basic tunic":
            if len(player.items) < 16:
                player.items.append(equipment_item)
                player.equipment["torso"] = ""
                return_dict["equipment message"] = "Basic Tunic torso un-equipped."
                player.defense = 0
                if defense_upgraded == 1:
                    player.defense += 4
            else:
                return_dict["equipment message"] = "Your inventory is full."
        if equipment_item.name == "power gloves":
            if len(player.items) < 16:
                player.items.append(equipment_item)
                player.equipment["gloves"] = ""
                return_dict["equipment message"] = "Power gloves un-equipped."
            else:
                return_dict["equipment message"] = "Your inventory is full."
    except AttributeError:
        pass

    return return_dict


# getting item player clicked based on it's name and return the corresponding item. for inventory items
def inventory_event_item(inventory_event_here, pygame):
    event_return = {"element": "", "clicked": False}
    if inventory_event_here.type == pygame.MOUSEBUTTONUP:
        inventory_mouse = pygame.mouse.get_pos()
        # list of sprites that collided with mouse cursor rect
        clicked_element = [inventory_element for inventory_element in drawing_functions.player_items
                           if inventory_element.rect.collidepoint(inventory_mouse)]
        # try to get inventory item player clicked based on it's name and return it
        try:
            if clicked_element[0].name == "health potion":
                event_return["element"] = clicked_element[0]
                event_return["clicked"] = True
            if clicked_element[0].name == "energy potion":
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
            if clicked_element[0].name == "basic staff":
                event_return["element"] = clicked_element[0]
                event_return["clicked"] = True
            if clicked_element[0].name == "basic sword":
                event_return["element"] = clicked_element[0]
                event_return["clicked"] = True
            if clicked_element[0].name == "basic bow":
                event_return["element"] = clicked_element[0]
                event_return["clicked"] = True
            if clicked_element[0].name == "basic robes":
                event_return["element"] = clicked_element[0]
                event_return["clicked"] = True
            if clicked_element[0].name == "basic armor":
                event_return["element"] = clicked_element[0]
                event_return["clicked"] = True
            if clicked_element[0].name == "basic tunic":
                event_return["element"] = clicked_element[0]
                event_return["clicked"] = True
            if clicked_element[0].name == "temporary item":
                event_return["element"] = clicked_element[0]
                event_return["clicked"] = True
            if clicked_element[0].name == "boss key":
                event_return["element"] = clicked_element[0]
                event_return["clicked"] = True
            if clicked_element[0].name == "power gloves":
                event_return["element"] = clicked_element[0]
                event_return["clicked"] = True
        except IndexError:
            pass
    return event_return


# handles mouse clicks for inventory sub-screen
def inventory(player, item, offense_upgraded, defense_upgraded, player_mage_amuna_down_1,
              player_mage_nuldar_down_1, player_mage_sorae_down_1, player_fighter_amuna_down_1,
              player_fighter_nuldar_down_1, player_fighter_sorae_down_1, player_scout_amuna_down_1,
              player_scout_nuldar_down_1, player_scout_sorae_down_1):

    return_dict = {"item message": ""}

    try:
        if item.name == "health potion":
            if player.health == 100:
                return_dict["item message"] = "You're already at full health."
            else:
                player.health = player.health + 40
                if player.health > 100:
                    player.health = 100
                drawing_functions.player_items.remove(item)
                player.items.remove(item)
                return_dict["item message"] = "The potion heals you for 40 hp."
        elif item.name == "energy potion":
            if player.energy == 100:
                return_dict["item message"] = "You're already at full energy."
            else:
                player.energy = player.energy + 40
                if player.energy > 100:
                    player.energy = 100
                drawing_functions.player_items.remove(item)
                player.items.remove(item)
                return_dict["item message"] = "The potion energizes you for 40 en."
        elif item.name == "shiny rock":
            return_dict["item message"] = "Oh, shiny. Maybe you can sell it?"
        elif item.name == "bone dust":
            return_dict["item message"] = "Eh, dusty. Maybe you can sell it?"
        elif item.name == "temporary item":
            return_dict["item message"] = "Tell my designer to finish me!"

        elif item.name == "basic staff":
            if player.equipment["weapon"] == "":
                player.equipment["weapon"] = item
                drawing_functions.player_items.remove(item)
                player.items.remove(item)
                player.role = "mage"
                if player.race == "amuna":
                    player.surf = player_mage_amuna_down_1
                if player.race == "nuldar":
                    player.surf = player_mage_nuldar_down_1
                if player.race == "sorae":
                    player.surf = player_mage_sorae_down_1
                player.offense = 25
                if offense_upgraded == 1:
                    player.offense += 10
                return_dict["item message"] = "Basic Staff weapon equipped"
            else:
                return_dict["item message"] = "Un-equip your current weapon first."
        elif item.name == "basic sword":
            if player.equipment["weapon"] == "":
                player.equipment["weapon"] = item
                drawing_functions.player_items.remove(item)
                player.items.remove(item)
                player.role = "fighter"
                if player.race == "amuna":
                    player.surf = player_fighter_amuna_down_1
                if player.race == "nuldar":
                    player.surf = player_fighter_nuldar_down_1
                if player.race == "sorae":
                    player.surf = player_fighter_sorae_down_1
                player.offense = 15
                if offense_upgraded == 1:
                    player.offense += 10
                return_dict["item message"] = "Basic Sword weapon equipped"
            else:
                return_dict["item message"] = "Un-equip your current weapon first."
        elif item.name == "basic bow":
            if player.equipment["weapon"] == "":
                player.equipment["weapon"] = item
                drawing_functions.player_items.remove(item)
                player.items.remove(item)
                player.role = "scout"
                if player.race == "amuna":
                    player.surf = player_scout_amuna_down_1
                if player.race == "nuldar":
                    player.surf = player_scout_nuldar_down_1
                if player.race == "sorae":
                    player.surf = player_scout_sorae_down_1
                player.offense = 20
                if offense_upgraded == 1:
                    player.offense += 10
                return_dict["item message"] = "Basic Bow weapon equipped"
            else:
                return_dict["item message"] = "Un-equip your current weapon first."
        elif item.name == "basic robes":
            if player.equipment["torso"] == "":
                if player.role == "mage":
                    player.equipment["torso"] = item
                    drawing_functions.player_items.remove(item)
                    player.items.remove(item)
                    player.defense = 4
                    if defense_upgraded == 1:
                        player.defense += 4
                    return_dict["item message"] = "Basic Robes torso equipped"
                else:
                    return_dict["item message"] = "Only mages wear light armor."
            else:
                return_dict["item message"] = "Un-equip your current gear first."
        elif item.name == "basic armor":
            if player.equipment["torso"] == "":
                if player.role == "fighter":
                    player.equipment["torso"] = item
                    drawing_functions.player_items.remove(item)
                    player.items.remove(item)
                    player.defense = 12
                    if defense_upgraded == 1:
                        player.defense += 4
                    return_dict["item message"] = "Basic Armor torso equipped"
                else:
                    return_dict["item message"] = "Only fighters wear heavy armor."
            else:
                return_dict["item message"] = "Un-equip your current gear first."
        elif item.name == "basic tunic":
            if player.equipment["torso"] == "":
                if player.role == "scout":
                    player.equipment["torso"] = item
                    drawing_functions.player_items.remove(item)
                    player.items.remove(item)
                    player.defense = 8
                    if defense_upgraded == 1:
                        player.defense += 4
                    return_dict["item message"] = "Basic Tunic torso equipped"
                else:
                    return_dict["item message"] = "Only scouts wear medium armor."
            else:
                return_dict["item message"] = "Un-equip your current gear first."
        elif item.name == "power gloves":
            if player.equipment["gloves"] == "":
                player.equipment["gloves"] = item
                drawing_functions.player_items.remove(item)
                player.items.remove(item)
                return_dict["item message"] = "Power gloves equipped."

            else:
                return_dict["item message"] = "Un-equip your current gear first."
    except AttributeError:
        pass

    return return_dict


# getting event based on user click related to combat scenario
def combat_event_button(combat_event, no_role_attack, mage_attack, fighter_attack, scout_attack,
                        barrier_button, strike_button, sense_button, pygame):
    if combat_event.type == pygame.MOUSEBUTTONUP:
        combat_mouse = pygame.mouse.get_pos()
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


# getting event based on user click related to npc
def npc_event_button(npc_event, quest_button, leave_button, pygame):
    if npc_event.type == pygame.MOUSEBUTTONUP:
        npc_mouse = pygame.mouse.get_pos()
        if quest_button.rect.collidepoint(npc_mouse):
            return "quest"
        if leave_button.rect.collidepoint(npc_mouse):
            return "leave"


# getting event based on user click related to quest window
def quest_event_button(quest_event, accept_button, decline_button, pygame):
    if quest_event.type == pygame.MOUSEBUTTONUP:
        quest_mouse = pygame.mouse.get_pos()
        if accept_button.rect.collidepoint(quest_mouse):
            return "accept"
        if decline_button.rect.collidepoint(quest_mouse):
            return "decline"


# getting event based on user click related to shop
def stardust_upgrade_event(stardust_event, offense_button, defense_button, pygame):
    if stardust_event.type == pygame.MOUSEBUTTONUP:
        stardust_mouse = pygame.mouse.get_pos()
        if offense_button.rect.collidepoint(stardust_mouse):
            return "offense"
        if defense_button.rect.collidepoint(stardust_mouse):
            return "defense"


# getting event based on user click related to shop
def shop_event_button(shop_event, buy_button, leave_button, pygame):
    if shop_event.type == pygame.MOUSEBUTTONUP:
        shop_mouse = pygame.mouse.get_pos()
        if buy_button.rect.collidepoint(shop_mouse):
            return "buy"
        if leave_button.rect.collidepoint(shop_mouse):
            return "leave"


# getting event based on user click related to shop
def shop_sell_button(shop_sell_event, yes_button, pygame, info_window):
    if shop_sell_event.type == pygame.MOUSEBUTTONUP:
        shop_sell_mouse = pygame.mouse.get_pos()
        if yes_button.rect.collidepoint(shop_sell_mouse):
            return "yes"
        else:
            if not info_window.rect.collidepoint(shop_sell_mouse):
                return "no"


# getting event based on user click related to shop
def shop_buy_button(shop_buy_event, yes_button, pygame):
    if shop_buy_event.type == pygame.MOUSEBUTTONUP:
        shop_buy_mouse = pygame.mouse.get_pos()
        if yes_button.rect.collidepoint(shop_buy_mouse):
            return "yes"
        else:
            return "no"


# getting event based on user click related to inn
def inn_event_button(inn_event, rest_button, leave_button, pygame):
    if inn_event.type == pygame.MOUSEBUTTONUP:
        inn_mouse = pygame.mouse.get_pos()
        if rest_button.rect.collidepoint(inn_mouse):
            return "rest"
        if leave_button.rect.collidepoint(inn_mouse):
            return "leave"


# getting event based on user click related to academia skill buttons
def academia_event_button(academia_event, mage_learn, fighter_learn, scout_learn, leave_button, pygame):
    if academia_event.type == pygame.MOUSEBUTTONUP:
        academia_mouse = pygame.mouse.get_pos()
        if mage_learn.rect.collidepoint(academia_mouse):
            return "mage learn"
        if fighter_learn.rect.collidepoint(academia_mouse):
            return "fighter learn"
        if scout_learn.rect.collidepoint(academia_mouse):
            return "scout learn"
        if leave_button.rect.collidepoint(academia_mouse):
            return "leave"


# getting item player clicked based on it's name and return the corresponding item. for buying items
def buy_event_item(buy_event, shopkeeper_items, pygame):
    if buy_event.type == pygame.MOUSEBUTTONUP:
        buy_mouse = pygame.mouse.get_pos()
        # list of sprites that collided with mouse cursor rect
        clicked_element = [buy_element for buy_element in shopkeeper_items if buy_element.rect.collidepoint(buy_mouse)]
        # try to get inventory item player clicked based on it's name and return it
        try:
            if clicked_element[0].name == "health potion":
                return clicked_element[0]
            if clicked_element[0].name == "energy potion":
                return clicked_element[0]
            if clicked_element[0].name == "shiny rock":
                return clicked_element[0]
            if clicked_element[0].name == "bone dust":
                return clicked_element[0]
            if clicked_element[0].name == "basic staff":
                return clicked_element[0]
            if clicked_element[0].name == "basic sword":
                return clicked_element[0]
            if clicked_element[0].name == "basic bow":
                return clicked_element[0]
            if clicked_element[0].name == "basic robes":
                return clicked_element[0]
            if clicked_element[0].name == "basic armor":
                return clicked_element[0]
            if clicked_element[0].name == "basic tunic":
                return clicked_element[0]
        except IndexError:
            pass


# getting item player clicked based on it's name and return the corresponding item. for selling items
def sell_event_item(sell_event, pygame):
    if sell_event.type == pygame.MOUSEBUTTONUP:
        sell_mouse = pygame.mouse.get_pos()
        # list of sprites that collided with mouse cursor rect
        clicked_element = [sell_element for sell_element in drawing_functions.player_items if
                           sell_element.rect.collidepoint(sell_mouse)]
        # try to get inventory item player clicked based on it's name and return it
        try:
            if clicked_element[0].name == "health potion":
                return clicked_element[0]
            if clicked_element[0].name == "energy potion":
                return clicked_element[0]
            if clicked_element[0].name == "shiny rock":
                return clicked_element[0]
            if clicked_element[0].name == "bone dust":
                return clicked_element[0]
            if clicked_element[0].name == "cracked ember":
                return clicked_element[0]
            if clicked_element[0].name == "broken band":
                return clicked_element[0]
            if clicked_element[0].name == "basic staff":
                return clicked_element[0]
            if clicked_element[0].name == "basic sword":
                return clicked_element[0]
            if clicked_element[0].name == "basic bow":
                return clicked_element[0]
            if clicked_element[0].name == "basic robes":
                return clicked_element[0]
            if clicked_element[0].name == "basic armor":
                return clicked_element[0]
            if clicked_element[0].name == "basic tunic":
                return clicked_element[0]
            if clicked_element[0].name == "temporary item":
                return clicked_element[0]
        except IndexError:
            pass


# getting item player clicked based on it's name and return the corresponding item
def skill_learn_event_item(skill_learn_event, skill_learn_items, pygame):
    if skill_learn_event.type == pygame.MOUSEBUTTONUP:
        skill_learn_mouse = pygame.mouse.get_pos()
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
            if skill_learn_element[0].name == "close button":
                return skill_learn_element[0]
        except IndexError:
            pass
