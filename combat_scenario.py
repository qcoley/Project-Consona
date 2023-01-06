import random
import gameplay_functions


def resting_animation(player, enemy, player_battle_sprite, snake_battle_sprite, ghoul_battle_sprite,
                      chorizon_battle_sprite, muchador_battle_sprite, magmon_battle_sprite, bandile_battle_sprite,
                      chinzilla_battle_sprite, barrier_active, sharp_sense_active, in_battle, in_npc_interaction,
                      graphics):

    if player.race == "amuna":
        if player.role == "mage":
            if barrier_active:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_mage_barrier_amuna_battle"])
            else:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_mage_amuna_battle"])
        if player.role == "fighter":
            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                        player_battle_sprite.y_coordinate,
                                        graphics["player_fighter_amuna_battle"])
        if player.role == "scout":
            if sharp_sense_active:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_scout_sense_amuna_battle"])
            else:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_scout_amuna_battle"])
        if player.role == "":
            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                        player_battle_sprite.y_coordinate,
                                        graphics["player_no_role_amuna_battle"])
    if player.race == "sorae":
        if player.role == "mage":
            if barrier_active:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_mage_barrier_sorae_battle"])
            else:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_mage_sorae_battle"])
        if player.role == "fighter":
            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                        player_battle_sprite.y_coordinate,
                                        graphics["player_fighter_sorae_battle"])
        if player.role == "scout":
            if sharp_sense_active:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_scout_sense_sorae_battle"])
            else:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_scout_sorae_battle"])
        if player.role == "":
            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                        player_battle_sprite.y_coordinate,
                                        graphics["player_no_role_sorae_battle"])
    if player.race == "nuldar":
        if player.role == "mage":
            if barrier_active:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_mage_barrier_nuldar_battle"])
            else:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_mage_nuldar_battle"])
        if player.role == "fighter":
            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                        player_battle_sprite.y_coordinate,
                                        graphics["player_fighter_nuldar_battle"])
        if player.role == "scout":
            if sharp_sense_active:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_scout_sense_nuldar_battle"])
            else:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_scout_nuldar_battle"])
        if player.role == "":
            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                        player_battle_sprite.y_coordinate,
                                        graphics["player_no_role_nuldar_battle"])

    if in_battle and not in_npc_interaction:
        if enemy.kind == "snake":
            snake_battle_sprite.update(715, 250, graphics["snake_battle"])
        if enemy.kind == "ghoul":
            ghoul_battle_sprite.update(698, 280, graphics["ghoul_battle"])
        if enemy.kind == "chorizon":
            chorizon_battle_sprite.update(720, 325, graphics["chorizon_battle"])
        if enemy.kind == "muchador":
            muchador_battle_sprite.update(705, 290, graphics["muchador_battle"])
        if enemy.kind == "magmon":
            magmon_battle_sprite.update(705, 286, graphics["magmon_battle"])
        if enemy.kind == "bandile":
            bandile_battle_sprite.update(695, 300, graphics["bandile_battle"])
        if enemy.kind == "chinzilla":
            chinzilla_battle_sprite.update(700, 300, graphics["chinzilla_battle"])


# update player character and enemy sprites for combat animation
def combat_animation(player, enemy, player_battle_sprite, snake_battle_sprite, ghoul_battle_sprite,
                     chorizon_battle_sprite, muchador_battle_sprite, magmon_battle_sprite, bandile_battle_sprite,
                     chinzilla_battle_sprite, barrier_active, sharp_sense_active, hard_strike, graphics):

    # update player character sprite for combat animation
    if player.race == "amuna":
        if player.role == "mage":
            if barrier_active:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_mage_barrier_amuna_attack"])
            else:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_mage_amuna_attack"])
        if player.role == "fighter":
            if not hard_strike:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_fighter_amuna_attack"])
        if player.role == "scout":
            if sharp_sense_active:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_scout_sense_amuna_attack"])
            else:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_scout_amuna_attack"])
        if player.role == "":
            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                        player_battle_sprite.y_coordinate,
                                        graphics["player_no_role_amuna_attack"])
    if player.race == "sorae":
        if player.role == "mage":
            if barrier_active:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_mage_barrier_sorae_attack"])
            else:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_mage_sorae_attack"])
        if player.role == "fighter":
            if not hard_strike:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_fighter_sorae_attack"])
        if player.role == "scout":
            if sharp_sense_active:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_scout_sense_sorae_attack"])
            else:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_scout_sorae_attack"])
        if player.role == "":
            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                        player_battle_sprite.y_coordinate,
                                        graphics["player_no_role_sorae_attack"])
    if player.race == "nuldar":
        if player.role == "mage":
            if barrier_active:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_mage_barrier_nuldar_attack"])
            else:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_mage_nuldar_attack"])
        if player.role == "fighter":
            if not hard_strike:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_fighter_nuldar_attack"])
        if player.role == "scout":
            if sharp_sense_active:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_scout_sense_nuldar_attack"])
            else:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_scout_nuldar_attack"])
        if player.role == "":
            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                        player_battle_sprite.y_coordinate,
                                        graphics["player_no_role_nuldar_attack"])
    if enemy.kind == "snake":
        snake_battle_sprite.update(715, 250, graphics["snake_attack"])
    if enemy.kind == "ghoul":
        ghoul_battle_sprite.update(698, 280, graphics["ghoul_attack"])
    if enemy.kind == "chorizon":
        chorizon_battle_sprite.update(720, 325, graphics["chorizon_attack"])
    if enemy.kind == "muchador":
        muchador_battle_sprite.update(705, 290, graphics["muchador_attack"])
    if enemy.kind == "magmon":
        magmon_battle_sprite.update(705, 286, graphics["magmon_attack"])
    if enemy.kind == "bandile":
        bandile_battle_sprite.update(695, 300, graphics["bandile_attack"])
    if enemy.kind == "chinzilla":
        chinzilla_battle_sprite.update(700, 300, graphics["chinzilla_attack"])


def fighter(player, player_battle_sprite, current_enemy_battling, snake_battle_sprite,
            ghoul_battle_sprite, chorizon_battle_sprite, muchador_battle_sprite, magmon_battle_sprite,
            bandile_battle_sprite, chinzilla_battle_sprite, player_fighter_amuna_strike, player_fighter_sorae_strike,
            player_fighter_nuldar_strike, snake_battle, ghoul_battle, chorizon_battle, muchador_battle, magmon_battle,
            bandile_battle, chinzilla_battle):

    # update animations for hard strike attack
    if player.race == "amuna":
        if player.role == "fighter":
            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                        player_battle_sprite.y_coordinate,
                                        player_fighter_amuna_strike)
    if player.race == "sorae":
        if player.role == "fighter":
            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                        player_battle_sprite.y_coordinate,
                                        player_fighter_sorae_strike)
    if player.race == "nuldar":
        if player.role == "fighter":
            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                        player_battle_sprite.y_coordinate,
                                        player_fighter_nuldar_strike)

    if current_enemy_battling.kind == "snake":
        snake_battle_sprite.update(715, 250, snake_battle)
    if current_enemy_battling.kind == "ghoul":
        ghoul_battle_sprite.update(698, 280, ghoul_battle)
    if current_enemy_battling.kind == "chorizon":
        chorizon_battle_sprite.update(720, 325, chorizon_battle)
    if current_enemy_battling.kind == "muchador":
        muchador_battle_sprite.update(725, 350, muchador_battle)
    if current_enemy_battling.kind == "magmon":
        magmon_battle_sprite.update(705, 286, magmon_battle)
    if current_enemy_battling.kind == "bandile":
        bandile_battle_sprite.update(695, 300, bandile_battle)
    if current_enemy_battling.kind == "chinzilla":
        chinzilla_battle_sprite.update(700, 300, chinzilla_battle)


def enemy_health_bar(enemys, graphics):
    try:
        enemys.health_bar.update(enemys.health_bar.x_coordinate, enemys.health_bar.y_coordinate,
                                 gameplay_functions.health_bar_update(enemys, graphics))
    except AttributeError:
        pass


def attack_scenario(enemy_combating, combat_event, player, hard_strike_learned, level_up_win, level_up_font, graphics,
                    sharp_sense_active, barrier_active):
    # get the all the stuff that happened in this scenario and return it to main loop via dictionary keys and values
    combat_event_dictionary = {
        "damage done string": 0, "damage taken string": 0, "damage done": 0, "damage taken": 0,
        "item dropped": "", "experience gained": 0, "quest update": "", "enemy defeated": False, "leveled": False,
        "effective player": False, "non effective player": False, "effective enemy": False,
        "non effective enemy": False}

    if combat_event == "attack":
        if enemy_combating.alive_status:
            # returns players damage to the enemy based on level and equipment
            attack_dict = gameplay_functions.attack_enemy(player, enemy_combating, sharp_sense_active)
            combat_event_dictionary["effective player"] = attack_dict["effective"]
            combat_event_dictionary["non effective player"] = attack_dict["non effective"]
            combat_event_dictionary["critical dealt"] = attack_dict["critical"]
            damage_to_enemy = attack_dict["damage"]

            enemy_combating.health = enemy_combating.health - damage_to_enemy
            enemy_health_bar(enemy_combating, graphics)

            # if enemy is not dead yet
            if enemy_combating.health > 0:
                attacked_enemy_string = f" You did {damage_to_enemy} damage to {enemy_combating.kind}."
                combat_event_dictionary["damage done"] = damage_to_enemy
                # add damage to enemy to event dictionary to be returned to main loop
                combat_event_dictionary["damage done string"] = attacked_enemy_string

                # returns total damage output from enemy as attacked_player_health value
                defend_dict = gameplay_functions.attack_player(player, enemy_combating, barrier_active)
                combat_event_dictionary["effective enemy"] = defend_dict["effective"]
                combat_event_dictionary["non effective enemy"] = defend_dict["non effective"]
                combat_event_dictionary["critical received"] = defend_dict["critical"]
                damage_to_player = defend_dict["damage"]

                if damage_to_player > 0:
                    attacked_player_string = f"You take {damage_to_player} damage from {enemy_combating.kind}."
                    player.health = player.health - damage_to_player
                    combat_event_dictionary["damage taken"] = damage_to_player
                    # add damage done to player from enemy to dictionary
                    combat_event_dictionary["damage taken string"] = attacked_player_string

                    # player health is less than or equal to 0, player is dead
                    if player.health <= 0:
                        player.alive_status = False
                    return combat_event_dictionary
                else:
                    enemy_miss_string = f'{enemy_combating.kind} missed.'
                    # add to dictionary that enemy did no damage to player
                    combat_event_dictionary["damage taken string"] = enemy_miss_string
                    return combat_event_dictionary

            # enemy has been defeated, will return an amount of xp based on current levels
            else:
                # if player is on quest to kill snakes
                if enemy_combating.kind == "snake":
                    if player.quest_status["sneaky snakes"]:
                        if player.quest_progress["sneaky snakes"] < 4:
                            player.quest_progress["sneaky snakes"] = player.quest_progress["sneaky snakes"] + 1
                            quest_string = f"{player.quest_progress['sneaky snakes']}/4 snakes"
                            combat_event_dictionary["quest update"] = quest_string
                else:
                    combat_event_dictionary["quest update"] = "No"

                # if player is on quest to kill ghouls
                if enemy_combating.kind == "ghoul":
                    if player.quest_status["ghouled again"]:
                        if player.quest_progress["ghouled again"] < 4:
                            player.quest_progress["ghouled again"] = player.quest_progress["ghouled again"] + 1
                            quest_string = f"{player.quest_status['ghouled again']}/4 ghouls"
                            combat_event_dictionary["quest update"] = quest_string
                else:
                    combat_event_dictionary["quest update"] = "No"

                # if player is on quest to kill magmons
                if enemy_combating.kind == "magmon":
                    if player.quest_status["elementary elementals"]:
                        if player.quest_progress["elementary elementals"] < 4:
                            player.quest_progress["elementary elementals"] = \
                                player.quest_progress["elementary elementals"] + 1
                            quest_string = f"{player.quest_status['elementary elementals']}/4 magmons"
                            combat_event_dictionary["quest update"] = quest_string
                else:
                    combat_event_dictionary["quest update"] = "No"

                # if player is on quest to kill bandiles
                if enemy_combating.kind == "bandile":
                    if player.quest_status["band hammer"]:
                        if player.quest_progress["band hammer"] < 4:
                            player.quest_progress["band hammer"] = \
                                player.quest_progress["band hammer"] + 1
                            quest_string = f"{player.quest_status['band hammer']}/4 bandiles"
                            combat_event_dictionary["quest update"] = quest_string
                else:
                    combat_event_dictionary["quest update"] = "No"

                # if player is on quest to kill bandiles
                if enemy_combating.kind == "chinzilla":
                    if player.quest_status["it's dangerous to go alone"]:
                        if player.quest_progress["it's dangerous to go alone"] < 1:
                            player.quest_progress["it's dangerous to go alone"] = \
                                player.quest_progress["it's dangerous to go alone"] + 1
                            quest_string = str(player.quest_progress["it's dangerous to go alone"]) + "/1 chinzilla"
                            combat_event_dictionary["quest update"] = quest_string
                else:
                    combat_event_dictionary["quest update"] = "No"

                # experienced gained by player from defeating enemy
                if player.level <= enemy_combating.level + 1:
                    experience = int((enemy_combating.level / player.level) * 30)
                    player.experience = player.experience + experience
                    enemy_experience = f"{experience}"
                    # add to dictionary experience given from defeating enemy
                    combat_event_dictionary["experience gained"] = enemy_experience
                # player gains less experience if they're 1 level higher or more than enemy
                if player.level > enemy_combating.level + 1:
                    experience = int((enemy_combating.level / player.level))
                    player.experience = player.experience + experience
                    enemy_experience = f"{experience}"
                    # add to dictionary experience given from defeating enemy
                    combat_event_dictionary["experience gained"] = enemy_experience

                try:
                    drop_chance = random.randrange(1, 10)
                    # 80% chance (roughly?) to drop merchant item sellable by player for rupees at shops
                    if drop_chance > 2:
                        # if item dropped isn't just a placeholder string
                        if enemy_combating.items != "item":
                            # doesn't give item to player if their inventory is full
                            if len(player.items) < 16:
                                player.items.append(enemy_combating.items)
                                enemy_dropped_this = f"{enemy_combating.name} dropped [{enemy_combating.items.name}]."
                                # add to dictionary anything dropped from enemy upon their defeat
                                combat_event_dictionary["item dropped"] = enemy_dropped_this
                            else:
                                combat_event_dictionary["item dropped"] = "Item, but your inventory is full."
                    else:
                        combat_event_dictionary["item dropped"] = "No"
                except AttributeError:
                    combat_event_dictionary["item dropped"] = "No"

                # player will level up if experience greater than or equal to 100
                if player.experience >= 100:
                    gameplay_functions.level_up(player, level_up_win, level_up_font)
                    combat_event_dictionary["leveled"] = True

                enemy_combating.alive_status = False
                enemy_combating.kill()

                # add to dictionary True if enemy has been defeated
                combat_event_dictionary["enemy defeated"] = True
                return combat_event_dictionary

    # active combat skill, if player is fighter and has learned hard strike from the academia
    # same as default attack from above, but attack replaced by hard strike skill
    if combat_event == "skill 1":
        if player.role == "fighter":
            if hard_strike_learned:
                if enemy_combating.alive_status:
                    striked = random.randrange(15, 20)  # hard strike damage
                    enemy_combating.health = enemy_combating.health - striked
                    enemy_health_bar(enemy_combating, graphics)
                    if enemy_combating.health > 0:
                        attacked_enemy_string = f" You did {striked} damage to {enemy_combating.kind}."
                        combat_event_dictionary["damage done"] = striked
                        # add damage to enemy to event dictionary to be returned to main loop
                        combat_event_dictionary["damage done string"] = attacked_enemy_string

                        # returns total damage output from enemy as attacked_player_health value
                        defend_dict = gameplay_functions.attack_player(player, enemy_combating)
                        combat_event_dictionary["effective enemy"] = defend_dict["effective"]
                        combat_event_dictionary["non effective enemy"] = defend_dict["non effective"]
                        damage_to_player = defend_dict["damage"]

                        if damage_to_player > 0:
                            attacked_player_string = f"You take {damage_to_player} damage from {enemy_combating.kind}."
                            player.health = player.health - damage_to_player
                            combat_event_dictionary["damage taken"] = damage_to_player
                            # add damage done to player from enemy to dictionary
                            combat_event_dictionary["damage taken string"] = attacked_player_string

                            # player health is less than or equal to 0, player is dead
                            if player.health <= 0:
                                player.alive_status = False
                            return combat_event_dictionary
                        else:
                            enemy_miss_string = f'{enemy_combating.kind} missed.'
                            # add to dictionary that enemy did no damage to player
                            combat_event_dictionary["damage taken string"] = enemy_miss_string
                            return combat_event_dictionary

                    else:
                        if enemy_combating.kind == "snake":
                            if player.quest_status["sneaky snakes"]:
                                if player.quest_progress["sneaky snakes"] < 4:
                                    player.quest_progress["sneaky snakes"] = player.quest_progress["sneaky snakes"] + 1
                                    quest_string = f"{player.quest_progress['sneaky snakes']}/4 snakes"
                                    combat_event_dictionary["quest update"] = quest_string
                        else:
                            combat_event_dictionary["quest update"] = "No"
                        if enemy_combating.kind == "ghoul":
                            if player.quest_status["ghouled again"]:
                                if player.quest_progress["ghouled again"] < 4:
                                    player.quest_progress["ghouled again"] = player.quest_progress["ghouled again"] + 1
                                    quest_string = f"{player.quest_status['ghouled again']}/4 ghouls"
                                    combat_event_dictionary["quest update"] = quest_string
                        else:
                            combat_event_dictionary["quest update"] = "No"
                        # if player is on quest to kill magmons
                        if enemy_combating.kind == "magmon":
                            if player.quest_status["elementary elementals"]:
                                if player.quest_progress["elementary elementals"] < 4:
                                    player.quest_progress["elementary elementals"] = \
                                        player.quest_progress["elementary elementals"] + 1
                                    quest_string = f"{player.quest_status['elementary elementals']}/4 magmons"
                                    combat_event_dictionary["quest update"] = quest_string
                        else:
                            combat_event_dictionary["quest update"] = "No"
                        # if player is on quest to kill bandiles
                        if enemy_combating.kind == "bandile":
                            if player.quest_status["band hammer"]:
                                if player.quest_progress["band hammer"] < 4:
                                    player.quest_progress["band hammer"] = \
                                        player.quest_progress["band hammer"] + 1
                                    quest_string = f"{player.quest_status['band hammer']}/4 bandiles"
                                    combat_event_dictionary["quest update"] = quest_string
                        else:
                            combat_event_dictionary["quest update"] = "No"
                        # if player is on quest to kill bandiles
                        if enemy_combating.kind == "chinzilla":
                            if player.quest_status["it's dangerous to go alone"]:
                                if player.quest_progress["it's dangerous to go alone"] < 1:
                                    player.quest_progress["it's dangerous to go alone"] = \
                                        player.quest_progress["it's dangerous to go alone"] + 1
                                    quest_string = player.quest_status[
                                                       "it's dangerous to go alone"] + "/1 chinzilla"
                                    combat_event_dictionary["quest update"] = quest_string
                        else:
                            combat_event_dictionary["quest update"] = "No"
                        # experienced gained by player from defeating enemy
                        if player.level <= enemy_combating.level + 1:
                            experience = int((enemy_combating.level / player.level) * 30)
                            player.experience = player.experience + experience
                            enemy_experience = f"{experience}"
                            # add to dictionary experience given from defeating enemy
                            combat_event_dictionary["experience gained"] = enemy_experience
                        # player gains less experience if they're 1 level higher or more than enemy
                        if player.level > enemy_combating.level + 1:
                            experience = int((enemy_combating.level / player.level))
                            player.experience = player.experience + experience
                            enemy_experience = f"{experience}"
                            # add to dictionary experience given from defeating enemy
                            combat_event_dictionary["experience gained"] = enemy_experience
                        try:
                            drop_chance = random.randrange(1, 10)
                            if drop_chance > 2:
                                if enemy_combating.items != "item":
                                    if len(player.items) < 16:
                                        player.items.append(enemy_combating.items)
                                        enemy_dropped_this = f"{enemy_combating.name} dropped " \
                                                             f"[{enemy_combating.items.name}]."
                                        combat_event_dictionary["item dropped"] = enemy_dropped_this
                                    else:
                                        combat_event_dictionary["item dropped"] = "Item, but your inventory is full."
                            else:
                                combat_event_dictionary["item dropped"] = "No"
                        except AttributeError:
                            combat_event_dictionary["item dropped"] = "No"
                        if player.experience >= 100:
                            gameplay_functions.level_up(player, level_up_win, level_up_font)
                            combat_event_dictionary["leveled"] = True
                        enemy_combating.alive_status = False
                        enemy_combating.kill()
                        combat_event_dictionary["enemy defeated"] = True
                        return combat_event_dictionary
