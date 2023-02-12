import drawing_functions


# go through shop items and assign inventory slots (coordinates) to them
def shop_keeper_inventory_draw(npc_amuna_shopkeeper, shopkeeper_items, health_pot_img, energy_pot_img, basic_armor,
                               forged_armor, mythical_armor, cookie, candy, tart):

    # if shopkeeper has items in their inventory
    if len(npc_amuna_shopkeeper.items) > 0:
        buy_first_coord = 810
        buy_second_coord = 435

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
            if shop_item.name == "basic armor":
                shop_item.update(buy_first_coord, buy_second_coord, basic_armor)
                shopkeeper_items.append(shop_item)
                buy_inventory_counter += 1
            if shop_item.name == "forged armor":
                shop_item.update(buy_first_coord, buy_second_coord, forged_armor)
                shopkeeper_items.append(shop_item)
                buy_inventory_counter += 1
            if shop_item.name == "mythical armor":
                shop_item.update(buy_first_coord, buy_second_coord, mythical_armor)
                shopkeeper_items.append(shop_item)
                buy_inventory_counter += 1
            if shop_item.name == "pet cookie":
                shop_item.update(buy_first_coord, buy_second_coord, cookie)
                shopkeeper_items.append(shop_item)
                buy_inventory_counter += 1
            if shop_item.name == "pet candy":
                shop_item.update(buy_first_coord, buy_second_coord, candy)
                shopkeeper_items.append(shop_item)
                buy_inventory_counter += 1
            if shop_item.name == "pet tart":
                shop_item.update(buy_first_coord, buy_second_coord, tart)
                shopkeeper_items.append(shop_item)
                buy_inventory_counter += 1

            buy_first_coord += 60
            if buy_inventory_counter > 3:
                buy_second_coord += 60
                buy_first_coord = 810
                buy_inventory_counter = 0


def sell_items(pygame, player, sell_choice, current_sell_item, sfx_sell):
    sell_return = {"info 1": "", "info 2": "", "sold": False}
    if sell_choice == "yes":
        # ensures sell confirmation button can only be selected when confirmation window is drawn
        if len(drawing_functions.sell_info_window) > 0:
            try:
                if current_sell_item.name == "health potion":
                    sell_return["info 1"] = "Sold Health Potion for 5 rupees."
                    sell_return["info 2"] = "Health Potion removed from inventory."
                    player.items.remove(current_sell_item)
                    drawing_functions.player_items.remove(current_sell_item)
                    pygame.mixer.Sound.play(sfx_sell)
                    player.rupees = player.rupees + 5
                    sell_return["sold"] = True
                    drawing_functions.sell_info_window.clear()
                if current_sell_item.name == "energy potion":
                    sell_return["info 1"] = "Sold Energy Potion for 5 rupees."
                    sell_return["info 2"] = "Energy Potion removed from inventory."
                    player.items.remove(current_sell_item)
                    drawing_functions.player_items.remove(current_sell_item)
                    pygame.mixer.Sound.play(sfx_sell)
                    player.rupees = player.rupees + 5
                    sell_return["sold"] = True
                    drawing_functions.sell_info_window.clear()
                if current_sell_item.name == "shiny rock":
                    sell_return["info 1"] = "Sold Shiny Rock for 5 rupees."
                    sell_return["info 2"] = "Shiny Rock removed from inventory."
                    player.items.remove(current_sell_item)
                    drawing_functions.player_items.remove(current_sell_item)
                    pygame.mixer.Sound.play(sfx_sell)
                    player.rupees = player.rupees + 5
                    sell_return["sold"] = True
                    drawing_functions.sell_info_window.clear()
                if current_sell_item.name == "bone dust":
                    sell_return["info 1"] = "Sold Bone Dust for 10 rupees."
                    sell_return["info 2"] = "Bone Dust removed from inventory."
                    player.items.remove(current_sell_item)
                    drawing_functions.player_items.remove(current_sell_item)
                    pygame.mixer.Sound.play(sfx_sell)
                    player.rupees = player.rupees + 10
                    sell_return["sold"] = True
                    drawing_functions.sell_info_window.clear()
                if current_sell_item.name == "cracked ember":
                    sell_return["info 1"] = "Sold Cracked Ember for 25 rupees."
                    sell_return["info 2"] = "Cracked Ember removed from inventory."
                    player.items.remove(current_sell_item)
                    drawing_functions.player_items.remove(current_sell_item)
                    pygame.mixer.Sound.play(sfx_sell)
                    player.rupees = player.rupees + 25
                    sell_return["sold"] = True
                    drawing_functions.sell_info_window.clear()
                if current_sell_item.name == "broken band":
                    sell_return["info 1"] = "Sold Broken Band for 20 rupees."
                    sell_return["info 2"] = "Broken Band removed from inventory."
                    player.items.remove(current_sell_item)
                    drawing_functions.player_items.remove(current_sell_item)
                    pygame.mixer.Sound.play(sfx_sell)
                    player.rupees = player.rupees + 20
                    sell_return["sold"] = True
                    drawing_functions.sell_info_window.clear()
                if current_sell_item.name == "dried fins":
                    sell_return["info 1"] = "Sold Dried Fins for 40 rupees."
                    sell_return["info 2"] = "Dried Fins removed from inventory."
                    player.items.remove(current_sell_item)
                    drawing_functions.player_items.remove(current_sell_item)
                    pygame.mixer.Sound.play(sfx_sell)
                    player.rupees = player.rupees + 40
                    sell_return["sold"] = True
                    drawing_functions.sell_info_window.clear()
                if current_sell_item.name == "oscura pluma":
                    sell_return["info 1"] = "Sold Oscura Pluma for 45 rupees."
                    sell_return["info 2"] = "Oscura Pluma removed from inventory."
                    player.items.remove(current_sell_item)
                    drawing_functions.player_items.remove(current_sell_item)
                    pygame.mixer.Sound.play(sfx_sell)
                    player.rupees = player.rupees + 45
                    sell_return["sold"] = True
                    drawing_functions.sell_info_window.clear()
                if current_sell_item.name == "basic armor":
                    sell_return["info 1"] = "Sold Basic Armor for 25 rupees."
                    sell_return["info 2"] = "Basic Armor removed from inventory."
                    player.items.remove(current_sell_item)
                    drawing_functions.player_items.remove(current_sell_item)
                    pygame.mixer.Sound.play(sfx_sell)
                    player.rupees = player.rupees + 25
                    sell_return["sold"] = True
                    drawing_functions.sell_info_window.clear()
                if current_sell_item.name == "forged armor":
                    sell_return["info 1"] = "Sold Forged Armor for 100 rupees."
                    sell_return["info 2"] = "Forged Armor removed from inventory."
                    player.items.remove(current_sell_item)
                    drawing_functions.player_items.remove(current_sell_item)
                    pygame.mixer.Sound.play(sfx_sell)
                    player.rupees = player.rupees + 100
                    sell_return["sold"] = True
                    drawing_functions.sell_info_window.clear()
                if current_sell_item.name == "mythical armor":
                    sell_return["info 1"] = "Sold Mythical Armor for 250 rupees."
                    sell_return["info 2"] = "Mythical Armor removed from inventory."
                    player.items.remove(current_sell_item)
                    drawing_functions.player_items.remove(current_sell_item)
                    pygame.mixer.Sound.play(sfx_sell)
                    player.rupees = player.rupees + 250
                    sell_return["sold"] = True
                    drawing_functions.sell_info_window.clear()
                if current_sell_item.name == "pet cookie":
                    sell_return["info 1"] = "Sold Blueberry Cookie for 10 rupees."
                    sell_return["info 2"] = "Blueberry Cookie removed from inventory."
                    player.items.remove(current_sell_item)
                    drawing_functions.player_items.remove(current_sell_item)
                    pygame.mixer.Sound.play(sfx_sell)
                    player.rupees = player.rupees + 10
                    sell_return["sold"] = True
                    drawing_functions.sell_info_window.clear()
                if current_sell_item.name == "pet candy":
                    sell_return["info 1"] = "Sold Rock Candy for 10 rupees."
                    sell_return["info 2"] = "Rock Candy removed from inventory."
                    player.items.remove(current_sell_item)
                    drawing_functions.player_items.remove(current_sell_item)
                    pygame.mixer.Sound.play(sfx_sell)
                    player.rupees = player.rupees + 10
                    sell_return["sold"] = True
                    drawing_functions.sell_info_window.clear()
                if current_sell_item.name == "pet tart":
                    sell_return["info 1"] = "Sold Peach Tart for 10 rupees."
                    sell_return["info 2"] = "Peach Tart removed from inventory."
                    player.items.remove(current_sell_item)
                    drawing_functions.player_items.remove(current_sell_item)
                    pygame.mixer.Sound.play(sfx_sell)
                    player.rupees = player.rupees + 10
                    sell_return["sold"] = True
                    drawing_functions.sell_info_window.clear()
            except AttributeError:
                pass
    if sell_choice == "no":
        drawing_functions.sell_info_window.clear()

    return sell_return


def buy_items(pygame, player, buy_choice, current_buy_item, Item, health_pot_img, energy_pot_img, basic_armor,
              forged_armor, mythical_armor, cookie, candy, tart, sfx_buy):
    buy_return = {"info 1": "", "info 2": "", "bought": False}

    if buy_choice == "yes":
        if current_buy_item.name == "health potion":
            if len(player.items) < 16:
                if player.rupees > 9:
                    buy_return["info 1"] = "You Bought Health Potion for 10 rupees."
                    buy_return["info 2"] = "Health Potion added to inventory."
                    player.items.append(Item("health potion", "potion", 200, 200, health_pot_img, 0))
                    player.rupees = player.rupees - 10
                    pygame.mixer.Sound.play(sfx_buy)
                    buy_return["bought"] = True
                    drawing_functions.buy_info_window.clear()
                else:
                    buy_return["info 1"] = "You do not have enough rupees."
                    buy_return["info 2"] = "Health Potion cost 10 rupees."
            else:
                buy_return["info 1"] = "Your inventory is full."
                buy_return["info 2"] = ""

        if current_buy_item.name == "energy potion":
            if len(player.items) < 16:
                if player.rupees > 9:
                    buy_return["info 1"] = "Bought Energy Potion for 10 rupees."
                    buy_return["info 2"] = "Energy Potion added to inventory."
                    player.items.append(Item("energy potion", "potion", 200, 200, energy_pot_img, 0))
                    player.rupees = player.rupees - 10
                    pygame.mixer.Sound.play(sfx_buy)
                    buy_return["bought"] = True
                    drawing_functions.buy_info_window.clear()
                else:
                    buy_return["info 1"] = "You do not have enough rupees."
                    buy_return["info 2"] = "Energy Potion cost 10 rupees."
            else:
                buy_return["info 1"] = "Your inventory is full."
                buy_return["info 2"] = ""

        if current_buy_item.name == "basic armor":
            if len(player.items) < 16:
                if player.rupees > 49:
                    buy_return["info 1"] = "Bought Basic Armor for 50 rupees."
                    buy_return["info 2"] = "Basic Armor added to inventory."
                    player.items.append(Item("basic armor", "armor", 200, 200, basic_armor, 1))
                    player.rupees = player.rupees - 50
                    pygame.mixer.Sound.play(sfx_buy)
                    buy_return["bought"] = True
                    drawing_functions.buy_info_window.clear()
                else:
                    buy_return["info 1"] = "You do not have enough rupees."
                    buy_return["info 2"] = "Basic Armor cost 50 rupees."
            else:
                buy_return["info 1"] = "Your inventory is full."
                buy_return["info 2"] = ""

        if current_buy_item.name == "forged armor":
            if len(player.items) < 16:
                if player.rupees > 149:
                    buy_return["info 1"] = "Bought Forged Armor for 150 rupees."
                    buy_return["info 2"] = "Forged Armor added to inventory."
                    player.items.append(Item("forged armor", "armor", 200, 200, forged_armor, 2))
                    player.rupees = player.rupees - 150
                    pygame.mixer.Sound.play(sfx_buy)
                    buy_return["bought"] = True
                    drawing_functions.buy_info_window.clear()
                else:
                    buy_return["info 1"] = "You do not have enough rupees."
                    buy_return["info 2"] = "Forged Armor cost 200 rupees."
            else:
                buy_return["info 1"] = "Your inventory is full."
                buy_return["info 2"] = ""

        if current_buy_item.name == "mythical armor":
            if len(player.items) < 16:
                if player.rupees > 499:
                    buy_return["info 1"] = "Bought Mythical Armor for 500 rupees."
                    buy_return["info 2"] = "Mythical Armor added to inventory."
                    player.items.append(Item("mythical armor", "armor", 200, 200, mythical_armor, 3))
                    player.rupees = player.rupees - 500
                    pygame.mixer.Sound.play(sfx_buy)
                    buy_return["bought"] = True
                    drawing_functions.buy_info_window.clear()
                else:
                    buy_return["info 1"] = "You do not have enough rupees."
                    buy_return["info 2"] = "Mythical Armor cost 500 rupees."
            else:
                buy_return["info 1"] = "Your inventory is full."
                buy_return["info 2"] = ""

        if current_buy_item.name == "pet cookie":
            if len(player.items) < 16:
                if player.rupees > 19:
                    buy_return["info 1"] = "Bought Blueberry Cookie for 20 rupees."
                    buy_return["info 2"] = "Blueberry Cookie added to inventory."
                    player.items.append(Item("pet cookie", "cookie", 1078, 197, cookie, 1))
                    player.rupees = player.rupees - 20
                    pygame.mixer.Sound.play(sfx_buy)
                    buy_return["bought"] = True
                    drawing_functions.buy_info_window.clear()
                else:
                    buy_return["info 1"] = "You do not have enough rupees."
                    buy_return["info 2"] = "Blueberry Cookie cost 20 rupees."
            else:
                buy_return["info 1"] = "Your inventory is full."
                buy_return["info 2"] = ""

        if current_buy_item.name == "pet candy":
            if len(player.items) < 16:
                if player.rupees > 19:
                    buy_return["info 1"] = "Bought Rock Candy for 20 rupees."
                    buy_return["info 2"] = "Rock Candy added to inventory."
                    player.items.append(Item("pet candy", "candy", 1078, 197, candy, 1))
                    player.rupees = player.rupees - 20
                    pygame.mixer.Sound.play(sfx_buy)
                    buy_return["bought"] = True
                    drawing_functions.buy_info_window.clear()
                else:
                    buy_return["info 1"] = "You do not have enough rupees."
                    buy_return["info 2"] = "Rock Candy cost 20 rupees."
            else:
                buy_return["info 1"] = "Your inventory is full."
                buy_return["info 2"] = ""

        if current_buy_item.name == "pet tart":
            if len(player.items) < 16:
                if player.rupees > 19:
                    buy_return["info 1"] = "Bought Peach Tart for 20 rupees."
                    buy_return["info 2"] = "Peach Tart added to inventory."
                    player.items.append(Item("pet tart", "tart", 1078, 197, tart, 1))
                    player.rupees = player.rupees - 20
                    pygame.mixer.Sound.play(sfx_buy)
                    buy_return["bought"] = True
                    drawing_functions.buy_info_window.clear()
                else:
                    buy_return["info 1"] = "You do not have enough rupees."
                    buy_return["info 2"] = "Peach Tart cost 20 rupees."
            else:
                buy_return["info 1"] = "Your inventory is full."
                buy_return["info 2"] = ""

    if buy_choice == "no":
        drawing_functions.buy_info_window.clear()

    return buy_return
