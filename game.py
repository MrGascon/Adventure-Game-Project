""" Project Adventure Functions Module

This module calls upon gamefunctions.py and runs each and every function multiple times.

Author: Jake Gascon
Date: 11.3.2024
Assignment: Project Adventure Functions """
from math import floor
from operator import truediv
from gamefunctions import *

#set global variables for money, gold and max health
gold = 1000
health = 30
maxHealth = 30
user_inventory = [{"name":"fists", "type":"weapon", "power":"1"}]
store_items = []
equipped_weapon = 0

def option_handler(option):
    global maxHealth
    global health
    global gold
    global user_inventory
    global store_items
    global equipped_weapon

    # Fight Monster
    if option == 1:
        temp_inventory = []
        health, gold, temp_inventory, equipped_weapon = fight_monster(health, gold, user_inventory, equipped_weapon)
        user_inventory = temp_inventory
    # Sleep (Restore HP for the cost of 5 gold)
    elif option == 2:
        health, gold = sleep(maxHealth, health, gold)
    elif option == 3:
        #view store
        new_inventory = []
        gold, new_inventory = visit_store(gold, store_items)
        user_inventory.extend(new_inventory)
    elif option == 4:
        #view inventory
        get_user_inventory(user_inventory)
    elif option ==5:
        #print weapons and offer to equip
        equipped_weapon = get_weapons(user_inventory)

def set_store():
    global store_items
    #set the store for this instance
    set_store_items(store_items)

if __name__ == '__main__':
    set_store()
    choice = 0

    #Loop through the game if the player has not quit
    while choice != 6:
        # Get the user fight options and send in the current health and gold values, validate input
        while True:
            get_user_options(health, gold)
            try:
                choice = int(input())
            except ValueError:
                print("Invalid Selection, please try again.\n")
                break

            #validate that the user entered a valid option and if not keep looping
            if choice in range (1, 7):
                break
            else:
                print("Invalid Selection, please try again.\n")

        option_handler(choice)