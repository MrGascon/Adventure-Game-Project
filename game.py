""" Project Adventure Functions Module

This module calls upon gamefunctions.py and runs each and every function multiple times.

Author: Jake Gascon
Date: 9.29.2024
Assignment: Project Adventure Functions """
from gamefunctions import *

if __name__ == '__main__':
    #show that you can afford the full quantity
    num_purchased, leftover_money = purchase_item(2, 20, 5)
    print(f'Quantity Purchased = {num_purchased}')
    print(f'Money Remaining = {leftover_money}')
    print()

    #show that only some items are purchased if you cant afford the full quantity
    num_purchased, leftover_money = purchase_item(2, 5, 3)
    print(f'Quantity Purchased = {num_purchased}')
    print(f'Money Remaining = {leftover_money}')
    print()

    #show that the default value of 1 works
    num_purchased, leftover_money = purchase_item(2, 20)
    print(f'Quantity Purchased = {num_purchased}')
    print(f'Money Remaining = {leftover_money}')
    print()

    #generate random monster
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

    #Print hello centered with the name
    print_welcome('Jake', 15)
    print_welcome('Ember', 20)
    print_welcome('Whiskey', 30)
    print()

    #Print the shop menu
    print_shop_menu("Apple", 31, "Pear", 1.234)
    print_shop_menu("Egg", .23, "Bag of Oats", 12.34)
    print_shop_menu("Pineapple", 3.25, "Chicken", 100.378)