import drawing_functions

sell_item_elements = []


# go through shop items and assign inventory slots (coordinates) to them
def shop_keeper_inventory_draw(npc_amuna_shopkeeper, shopkeeper_items, health_pot_img, energy_pot_img, basic_staff_img,
                               basic_sword_img, basic_bow_img, basic_robes_img, basic_armor_img, basic_tunic_img):
    # if shopkeeper has items in their inventory
    if len(npc_amuna_shopkeeper.items) > 0:
        buy_first_coord = 810
        buy_second_coord = 435
        # ----------------------------------------------------------------------------------
        buy_inventory_counter = 0
        for shop_item in npc_amuna_shopkeeper.items:
            if shop_item.name == "health potion":
                shop_item.update(buy_first_coord, buy_second_coord, health_pot_img)
                shopkeeper_items.append(shop_item)
                buy_inventory_counter += 1
            if shop_item.name == "energy potion":
                shop_item.update(buy_first_coord, buy_second_coord, energy_pot_img)
                shopkeeper_items.append(shop_item)
                buy_inventory_counter += 1
            if shop_item.name == "basic staff":
                shop_item.update(buy_first_coord, buy_second_coord, basic_staff_img)
                shopkeeper_items.append(shop_item)
                buy_inventory_counter += 1
            if shop_item.name == "basic sword":
                shop_item.update(buy_first_coord, buy_second_coord, basic_sword_img)
                shopkeeper_items.append(shop_item)
                buy_inventory_counter += 1
            if shop_item.name == "basic bow":
                shop_item.update(buy_first_coord, buy_second_coord, basic_bow_img)
                shopkeeper_items.append(shop_item)
                buy_inventory_counter += 1
            if shop_item.name == "basic robes":
                shop_item.update(buy_first_coord, buy_second_coord, basic_robes_img)
                shopkeeper_items.append(shop_item)
                buy_inventory_counter += 1
            if shop_item.name == "basic armor":
                shop_item.update(buy_first_coord, buy_second_coord, basic_armor_img)
                shopkeeper_items.append(shop_item)
                buy_inventory_counter += 1
            if shop_item.name == "basic tunic":
                shop_item.update(buy_first_coord, buy_second_coord, basic_tunic_img)
                shopkeeper_items.append(shop_item)
                buy_inventory_counter += 1

            buy_first_coord += 60
            if buy_inventory_counter > 3:
                buy_second_coord += 60
                buy_first_coord = 810
                buy_inventory_counter = 0


def shop_buy_items(player, buy_item, Item, health_pot_img, energy_pot_img, basic_staff_img, basic_sword_img,
                   basic_bow_img, basic_robes_img, basic_armor_img, basic_tunic_img):
    shop_buy_return = {"info 1": "", "info 2": "", "bought": False}
    try:
        # player has clicked health potion. If player has enough rupees it will buy item
        # and add to their inventory. Also subtracts the price from current rupee count
        if buy_item.name == "health potion":
            if len(player.items) < 16:
                if player.rupees > 9:
                    shop_buy_return["info 1"] = "You Bought Health Potion for 10 rupees."
                    shop_buy_return["info 2"] = "Health Potion added to inventory."
                    player.items.append(Item("health potion", "potion", 200, 200, health_pot_img))
                    player.rupees = player.rupees - 10
                    shop_buy_return["bought"] = True
                else:
                    shop_buy_return["info 1"] = "You do not have enough rupees."
                    shop_buy_return["info 2"] = "Health Potion cost 10 rupees."
            else:
                shop_buy_return["info 1"] = "Your inventory is full."
                shop_buy_return["info 2"] = ""
        if buy_item.name == "energy potion":
            if len(player.items) < 16:
                if player.rupees > 9:
                    shop_buy_return["info 1"] = "Bought Energy Potion for 10 rupees."
                    shop_buy_return["info 2"] = "Energy Potion added to inventory."
                    player.items.append(Item("energy potion", "potion", 200, 200,
                                             energy_pot_img))
                    player.rupees = player.rupees - 10
                    shop_buy_return["bought"] = True
                else:
                    shop_buy_return["info 1"] = "You do not have enough rupees."
                    shop_buy_return["info 2"] = "Energy Potion cost 10 rupees."
            else:
                shop_buy_return["info 1"] = "Your inventory is full."
                shop_buy_return["info 2"] = ""
        if buy_item.name == "basic staff":
            if len(player.items) < 16:
                if player.rupees > 19:
                    shop_buy_return["info 1"] = "Bought Basic Staff for 20 rupees."
                    shop_buy_return["info 2"] = "Basic Staff added to inventory."
                    player.items.append(Item("basic staff", "mage", 200, 200,
                                             basic_staff_img))
                    player.rupees = player.rupees - 20
                    shop_buy_return["bought"] = True
                else:
                    shop_buy_return["info 1"] = "You do not have enough rupees."
                    shop_buy_return["info 2"] = "Basic Staff cost 20 rupees."
            else:
                shop_buy_return["info 1"] = "Your inventory is full."
                shop_buy_return["info 2"] = ""
        if buy_item.name == "basic sword":
            if len(player.items) < 16:
                if player.rupees > 19:
                    shop_buy_return["info 1"] = "Bought Basic Sword for 20 rupees."
                    shop_buy_return["info 2"] = "Basic Sword added to inventory."
                    player.items.append(Item("basic sword", "fighter", 200, 200,
                                             basic_sword_img))
                    player.rupees = player.rupees - 20
                    shop_buy_return["bought"] = True
                else:
                    shop_buy_return["info 1"] = "You do not have enough rupees."
                    shop_buy_return["info 2"] = "Basic Sword cost 20 rupees."
            else:
                shop_buy_return["info 1"] = "Your inventory is full."
                shop_buy_return["info 2"] = ""
        if buy_item.name == "basic bow":
            if len(player.items) < 16:
                if player.rupees > 19:
                    shop_buy_return["info 1"] = "Bought Basic Bow for 20 rupees."
                    shop_buy_return["info 2"] = "Basic Bow added to inventory."
                    player.items.append(Item("basic bow", "scout", 200, 200,
                                             basic_bow_img))
                    player.rupees = player.rupees - 20
                    shop_buy_return["bought"] = True
                else:
                    shop_buy_return["info 1"] = "You do not have enough rupees."
                    shop_buy_return["info 2"] = "Basic Bow cost 20 rupees."
            else:
                shop_buy_return["info 1"] = "Your inventory is full."
                shop_buy_return["info 2"] = ""
        if buy_item.name == "basic robes":
            if len(player.items) < 16:
                if player.rupees > 19:
                    shop_buy_return["info 1"] = "Bought Basic Robes for 20 rupees."
                    shop_buy_return["info 2"] = "Basic Robes added to inventory."
                    player.items.append(Item("basic robes", "mage", 200, 200,
                                             basic_robes_img))
                    player.rupees = player.rupees - 20
                    shop_buy_return["bought"] = True
                else:
                    shop_buy_return["info 1"] = "You do not have enough rupees."
                    shop_buy_return["info 2"] = "Basic Robes cost 20 rupees."
            else:
                shop_buy_return["info 1"] = "Your inventory is full."
                shop_buy_return["info 2"] = ""
        if buy_item.name == "basic armor":
            if len(player.items) < 16:
                if player.rupees > 19:
                    shop_buy_return["info 1"] = "Bought Basic Armor for 20 rupees."
                    shop_buy_return["info 2"] = "Basic Armor added to inventory."
                    player.items.append(Item("basic armor", "fighter", 200, 200,
                                             basic_armor_img))
                    player.rupees = player.rupees - 20
                    shop_buy_return["bought"] = True
                else:
                    shop_buy_return["info 1"] = "You do not have enough rupees."
                    shop_buy_return["info 2"] = "Basic Armor cost 20 rupees."
            else:
                shop_buy_return["info 1"] = "Your inventory is full."
                shop_buy_return["info 2"] = ""
        if buy_item.name == "basic tunic":
            if len(player.items) < 16:
                if player.rupees > 19:
                    shop_buy_return["info 1"] = "Bought Basic Tunic for 20 rupees."
                    shop_buy_return["info 2"] = "Basic Tunic added to inventory."
                    player.items.append(Item("basic tunic", "scout", 200, 200,
                                             basic_tunic_img))
                    player.rupees = player.rupees - 20
                    shop_buy_return["bought"] = True
                else:
                    shop_buy_return["info 1"] = "You do not have enough rupees."
                    shop_buy_return["info 2"] = "Basic Tunic cost 20 rupees."
            else:
                shop_buy_return["info 1"] = "Your inventory is full."
                shop_buy_return["info 2"] = ""
    except AttributeError:
        pass

    return shop_buy_return