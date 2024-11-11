""" Project Adventure Functions Module

This module contains several utility functions designed for a text-based adventure game. It handles in-game
transactions, randomly generates monsters, displays welcome messages, and formats shop menus.

Key features include:
purchase_item: Determines the quantity of items a character can purchase with their current funds.
new_random_monster: Generates a random monster with varying attributes like health, power, and monetary rewards.
print_welcome: Prints a welcome message with the player's name centered according to a specified width.
print_shop_menu: Displays a formatted shop menu showing items and their respective prices.
getParity: Checks if a given integer is even or odd.

Author: Jake Gascon
Date: 11.3.2024
Assignment: Project Adventure Functions """

import random
import math

def purchase_item(itemPrice: int, startingMoney: int, quantityToPurchase=1):
    """Determine if the character can purchase all the items they wish with the money
       they have or if it's a reduced amount.

    :param itemPrice: The current cost of a single item
    :param startingMoney: The amount of money the character has to spend
    :param quantityToPurchase: The amount of items the character would like to purchase
    :return: The amount of items the character could purchase and any remaining currency
    """
    quantity_purchased = 0
    money_remaining = 0

    #calculate the total to be spent if whole quantity is purchased
    total_spend = itemPrice * quantityToPurchase

    #if the whole quantity can be afforded
    if total_spend <= startingMoney:
        quantity_purchased = quantityToPurchase
        money_remaining = startingMoney - total_spend
    # if the total quantity cant be afforded
    else:
        #find the quantity that can be purchased
        quantity_purchased = math.floor(startingMoney / itemPrice)
        #calculate how much money remains after buying what can be afforded
        money_remaining = startingMoney - (itemPrice * quantity_purchased)
    return quantity_purchased, money_remaining

def new_random_monster():
    """Create a random monster using three preset types of monsters.

    :return: A dictionary containing a random monster
    """
    #Create three different monster types and allow for variation.
    spider_dict = {
        "name": "Spider",
        "description": "A giant spider with dripping fangs and glowing eyes. It moves toward you silently, its legs tapping the ground as it prepares to strike.",
        "health": random.randint(1, 5),
        "power": random.randint(1, 1),
        "money": int(random.random() * 10)
    }
    gargoyle_dict = {
        "name": "Gargoyle",
        "description": "Perched on a ruined tower, the gargoyle’s eyes glow red as it awakens. It spreads its wings and dives at you, claws extended.",
        "health": random.randint(20, 50),
        "power": random.randint(3, 5),
        "money": int(random.random() * 100)
    }
    hydra_dict = {
        "name": "Hydra",
        "description": "A two-headed hydra slithers from the swamp, each head snapping with razor-sharp teeth. Its scaly body coils, ready to strike from both sides.",
        "health": random.randint(30, 150),
        "power": random.randint(5, 7),
        "money": int(random.random() * 300)
    }

    #add the three monster types to the monster list
    monster_list = [spider_dict, gargoyle_dict, hydra_dict]

    #return a random monster dictionary with random values
    return monster_list[random.randint(0, 2)]

def print_welcome(name: str, width: int):
    """print welcome with the provided name centered on a width

    :param name: The provided name to be displayed
    :param width: How wide/long the text should be
    :return: Hello with the name provided centered on a provided width
    """
    output = f"Hello, {name}"
    print(output.center(width, " "))

def print_shop_menu(store_items):
    """print the current items in the shop formatted properly

    :param store_items: Dictionary holding the store items and values
    :output: print the shop formatted properly
    """
    print("/----------------------\\")
    for item in store_items:
        #itemname has 12 char
        #itemprice has 8 char
        len_itemName = len(item["name"])
        itemPrice = item["price"]
        print_name = ""

        if len_itemName < 12:
            #item1Name needs padding
            padnum = 12-len_itemName
            print_name = item["name"] + (" " * padnum)
        elif len_itemName > 12:
            #item1Name needs cut
            print_name = item["name"][:12]

        print("|{:<10}".format(print_name), end="")
        print("{:>10}|".format(itemPrice))

    print("\\----------------------/")

def get_user_options(hp, gold):
    print(f"\nCurrent HP: {hp}, Current Gold: {gold}")
    print("What would you like to do?\n")
    print("1) Fight Monster")
    print("2) Sleep (Restore HP for 5 Gold)")
    print("3) Visit Store")
    print("4) View Inventory")
    print("5) Equip Weapon")
    print("6) Save & Quit")
    print("7) Quit")

def fight_monster(health, gold, user_inventory, weapon: int):
    #generate a new random monster from my list
    my_monster = new_random_monster()
    print(f"Watch out! A {my_monster['name']} appears!")


    #fight the monster
    while True:
        print(f"Your equipped weapon is {user_inventory[weapon]["name"]}")
        print("Would you like to:")
        print(f"1) Fight this {my_monster['name']}")
        print(f"2) Change weapons")
        print(f"3) Run away")
        s_count = 0
        special = None
        for item in user_inventory:
            if item['name'] == "death dart":
                special = s_count
                break
            s_count += 1

        if special != None:
            print(f"4) Use Death Dart")

        valid_choice = True
        try:
            fight_run_choice = int(input(""))
        except ValueError:
            print("Invalid input")
            valid_choice = False

        if valid_choice:
            if fight_run_choice == 1:
                #calculate your hit
                damage_dealt = int(random.random() * (10*int(user_inventory[weapon]["power"])))
                #calculate opponents hit
                damage_taken = int(random.random() * my_monster['power'])
                my_monster['health'] -= damage_dealt

                if user_inventory[weapon]["name"] != "fists":
                    user_inventory[weapon]["currentDurability"] -= 1
                    if user_inventory[weapon]["currentDurability"] <= 0:
                        print("Ohh no your weapon has broken, back to your fists")
                        user_inventory.pop(weapon)
                        weapon = 0
                #player strikes first so if the monster is dead the player wins
                if my_monster['health'] <= 0:
                    #calculate money earned
                    money_earned = my_monster['money']
                    #give money to the player
                    gold += money_earned
                    print(f"You killed the {my_monster['name']} and earned {money_earned} gold!")
                    break

                #check if the player died
                health -= damage_taken
                if health <= 0:
                    print("Ohh no, you died...")
                    break
                #print totals
                display_fight_statistics(damage_dealt, damage_taken, health, my_monster['health'], my_monster['name'])
            elif fight_run_choice == 2:
                weapon = get_weapons(user_inventory)
            elif fight_run_choice == 4 and special != None:
                # calculate money earned
                money_earned = my_monster['money']
                # give money to the player
                gold += money_earned
                print(f"You killed the {my_monster['name']} with the death dart and earned {money_earned} gold!")
                user_inventory.pop(special)
                break
            else:
                print("You run away!")
                break
    return health, gold, user_inventory, weapon

def sleep(maxHealth, health, gold):
    """
    Sleep and restore health for 5 gold
    :param maxHealth: player max health
    :param health: player current health
    :param gold: player gold
    :return:
    """

    #check if player has the gold
    if gold >= 5:
        print("\nYou feel refreshed, however your pockets feel a little more empty than before...")
        health = maxHealth
        gold -= 5
        print(gold)
    else:
        print("\nSleeping is not an option, get back in and fight!")
    return health, gold

def display_fight_statistics(damage_dealt, damage_taken, player_health, monster_health, monster_name):
    """
    Display the current fight statistics
    :param damage_dealt: damage dealt to the monster
    :param damage_taken: damage taken by the monster
    :param player_health: player current health
    :param monster_health: monster current health
    :param monster_name: current monster
    :return:
    """
    print(f"You hit a {damage_dealt} while the {monster_name} hit a {damage_taken} on you.")
    print(f"Your health is now at {player_health}. The {monster_name}'s health is now at {monster_health}.")

def get_user_inventory(inventory):
    """
    return the inventory of the user
    :param inventory: current inventory of the user
    """
    print("\nYour inventory contains:")

    #Loop through the inventory and print what is in it.
    for item in inventory:
        if item["name"] != "fists":
            if item["type"] == "weapon":
                print(f"{item["name"]} remaining durability = {item["currentDurability"]}")
            else:
                print(f"{item["name"]}")

def set_store_items(store_items_dict):
    """
    Create the store items
    :param store_items_dict: dictionary holding all of the items avaliable for purchase in the store
    :return: none
    """
    store_items_dict.extend([
        {
            "name": "sword",
            "type": "weapon",
            "power": 2,
            "maxDurability": 10,
            "currentDurability": 10,
            "price": 10
        },
        {
            "name": "scimitar",
            "type": "weapon",
            "power": 3,
            "maxDurability": 20,
            "currentDurability": 20,
            "price": 50
        },
        {
            "name": "death dart",
            "type": "special",
            "note": "defeats any monster, destroyed on use",
            "price": 100
        }
    ])

def visit_store(gold, store_items):
    """
    Provide a store interface and allow purchases
    :param gold: players gold
    :param store_items: items in the store
    :return: nothing
    """
    inventory_out = []
    num_purchased = 0
    leftover_money = 0
    while True:
        count = 1
        print_shop_menu(store_items)
        print(f"You have {gold} gold to spend.")
        for item in store_items:
            print(f"{count}) Purchase {item['name']}")
            count+=1
        print(f"{count}) Leave Store")
        valid_input = True

        try:
            item_pick = int(input(""))
        except ValueError:
            print("Invalid Selection, please try again.\n")
            valid_input = False

        if valid_input:
            match item_pick:
                case 1:
                    num_purchased, leftover_money = purchase_item(store_items[0]["price"], gold, 1)
                    if num_purchased == 1:
                        gold = leftover_money
                        inventory_out.append(store_items[0].copy())
                        print(f"You purchased a {store_items[0]["name"]}")
                case 2:
                    num_purchased, leftover_money = purchase_item(store_items[1]["price"], gold, 1)
                    if num_purchased == 1:
                        gold = leftover_money
                        inventory_out.append(store_items[1].copy())
                        print(f"You purchased a {store_items[1]["name"]}")
                case 3:
                    num_purchased, leftover_money = purchase_item(store_items[2]["price"], gold, 1)
                    if num_purchased == 1:
                        gold = leftover_money
                        inventory_out.append(store_items[2].copy())
                        print(f"You purchased a {store_items[2]["name"]}")
                case 4:
                    break
                case _:
                    print("Please enter a valid selection 1-4")
    return gold, inventory_out

def get_weapons(inventory):
    """
    get the weapons that the player has in their inventory
    :param inventory: players inventory
    :return: weapon choice or 0 for fists
    """
    count = 0
    if len(inventory) > 0:
        print("\nWhich weapon would you like to select?:")
        print(f"{count}) Unequip weapons")
        for item in inventory:
            if item["name"] != "fists":
                if item["type"] == "weapon":
                    print(f"{count}) {item["name"]} remaining durability = {item["currentDurability"]}")
            count += 1
        valid_choice = True
        try:
            choice = int(input(""))
        except ValueError:
            print("Invalid Selection, please try again.\n")
            valid_choice = False
        if valid_choice:
            if choice in range (1,(len(inventory)+1)):
                print(f"You selected the {inventory[choice]["name"]} with {inventory[choice]["currentDurability"]} durability remaining")
                return choice
            elif choice == 0:
                print("You have unequipped your weapon and will now use your fists.")
                return 0
            else:
                print("Your selection was out of bounds, no weapon was equipped")
                return 0
    else:
        print("You have no weapons to select.")
        return 0