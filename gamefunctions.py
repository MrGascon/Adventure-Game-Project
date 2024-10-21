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
Date: 9.29.2024
Assignment: Project Adventure Functions """

import random
import math

def purchase_item(itemPrice: float, startingMoney: float, quantityToPurchase=1):
    """Determine if the character can purchase all the items they wish with the money
       they have or if it's a reduced amount.

    :param itemPrice: The current cost of a single item
    :param startingMoney: The amount of money the character has to spend
    :param quantityToPurchase: The amount of items the character would like to purchase
    :return: The amount of items the character could purchase and any remaining currency
    """
    quantity_purchased = 0
    money_remaining = 0.0

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
        "health": random.randint(5, 10),
        "power": random.randint(1, 3),
        "money": format(random.random() * 10, ".2f")
    }
    gargoyle_dict = {
        "name": "Gargoyle",
        "description": "Perched on a ruined tower, the gargoyle’s eyes glow red as it awakens. It spreads its wings and dives at you, claws extended.",
        "health": random.randint(50, 70),
        "power": random.randint(50, 100),
        "money": format(random.random() * 100, ".2f")
    }
    hydra_dict = {
        "name": "Hydra",
        "description": "A two-headed hydra slithers from the swamp, each head snapping with razor-sharp teeth. Its scaly body coils, ready to strike from both sides.",
        "health": random.randint(200, 450),
        "power": random.randint(150, 300),
        "money": format(random.random() * 10000, ".2f")
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

def print_shop_menu(item1Name: str, item1Price: float, item2Name: str, item2Price: float):
    """print the current items in the shop formatted properly

    :param item1Name: First item in the shop
    :param item1Price: Price of the first item
    :param item2Name: Second item in the shop
    :param item2Price: Price of the second item
    :output: print the shop formatted properly
    """
    #itemname has 12 char
    #itemprice has 8 char
    len_item1Name = len(item1Name)
    len_item2Name = len(item2Name)
    item1Price = "${:.2f}".format(item1Price)
    item2Price = "${:.2f}".format(item2Price)

    if len_item1Name < 12:
        #item1Name needs padding
        padnum = 12-len_item1Name
        item1Name = item1Name + (" " * padnum)
    elif len_item1Name > 12:
        #item1Name needs cut
        item1Name = item1Name[:12]


    if len_item2Name < 12:
        # item2Name needs padding
        padnum = 12 - len_item2Name
        item2Name = item2Name + (" " * padnum)
    elif len_item2Name > 12:
        # item2Name needs cut
        item2Name = item2Name[:12]

    print("/----------------------\\")
    print("|{:<10}".format(item1Name), end="")
    print("{:>10}|".format(item1Price))
    print("|{:<10}".format(item2Name), end="")
    print("{:>10}|".format(item2Price))
    print("\\----------------------/")

def test_functions():
    # show that you can afford the full quantity
    num_purchased, leftover_money = purchase_item(2, 20, 5)
    print(f'Quantity Purchased = {num_purchased}')
    print(f'Money Remaining = {leftover_money}')
    print()

    # show that only some items are purchased if you cant afford the full quantity
    num_purchased, leftover_money = purchase_item(2, 5, 3)
    print(f'Quantity Purchased = {num_purchased}')
    print(f'Money Remaining = {leftover_money}')
    print()

    # show that the default value of 1 works
    num_purchased, leftover_money = purchase_item(2, 20)
    print(f'Quantity Purchased = {num_purchased}')
    print(f'Money Remaining = {leftover_money}')
    print()

    # generate random monster
    my_monster = new_random_monster()
    print(my_monster['name'])
    print(my_monster['description'])
    print(my_monster['health'])
    print(my_monster['power'])
    print(my_monster['money'])
    print()

    # generate random monster
    my_monster = new_random_monster()
    print(my_monster['name'])
    print(my_monster['description'])
    print(my_monster['health'])
    print(my_monster['power'])
    print(my_monster['money'])
    print()

    # generate random monster
    my_monster = new_random_monster()
    print(my_monster['name'])
    print(my_monster['description'])
    print(my_monster['health'])
    print(my_monster['power'])
    print(my_monster['money'])
    print()

    # Print hello centered with the name
    print_welcome('Jake', 15)
    print_welcome('Ember', 20)
    print_welcome('Whiskey', 30)
    print()

    # Print the shop menu
    print_shop_menu("Apple", 31, "Pear", 1.234)
    print_shop_menu("Egg", .23, "Bag of Oats", 12.34)
    print_shop_menu("Pineapple", 3.25, "Chicken", 100.378)

if __name__ == '__main__':
    test_functions()

