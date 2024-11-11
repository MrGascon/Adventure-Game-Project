""" Project Adventure Functions Module

This module calls upon gamefunctions.py and runs each and every function multiple times.

Author: Jake Gascon
Date: 11.3.2024
Assignment: Project Adventure Functions """
import json
from math import floor
from operator import truediv
from gamefunctions import *

#set global variables for money, gold and max health
gold = 1000
health = 30
maxHealth = 30
user_inventory = [{"name":"fists", "type":"weapon", "power":"1"}]
store_items = []
save = []
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
    elif option == 5:
        #print weapons and offer to equip
        equipped_weapon = get_weapons(user_inventory)
    elif option == 6:
        global save

        #save data
        save = [
            gold,
            health,
            user_inventory,
            equipped_weapon
        ]
        file_path = './last_session.json'
        with open(file_path, 'w') as output_file:
            json.dump(save, output_file, indent=2)

def set_store():
    global store_items
    #set the store for this instance
    set_store_items(store_items)

def play_loop():
    choice = 0
    # Loop through the game if the player has not quit
    while choice != 6 and choice != 7:
        # Get the user fight options and send in the current health and gold values, validate input
        while True:
            get_user_options(health, gold)
            try:
                choice = int(input())
            except ValueError:
                print("Invalid Selection, please try again.\n")
                break

            #validate that the user entered a valid option and if not keep looping
            if choice in range (1, 8):
                break
            else:
                print("Invalid Selection, please try again.\n")

        option_handler(choice)

def load_save():
    global save
    global health
    global gold
    global user_inventory
    global equipped_weapon

    #read the json and write the prior values
    with open('./last_session.json', 'r') as file:
        save = json.load(file)

    gold = save[0]
    health = save[1]
    user_inventory = save[2]
    equipped_weapon = save[3]

if __name__ == '__main__':
    set_store()
    #load game or start new
    load_new = 0
    valid_choice = False
    while not valid_choice:
        try:
            load_new = int(input("1) Start a new game\n2) Load prior save\n"))
            valid_choice = True
        except ValueError:
            print("Invalid input")

    if load_new == 1:
        play_loop()
    else:
        load_save()
        play_loop()

