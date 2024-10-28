""" Project Adventure Functions Module

This module calls upon gamefunctions.py and runs each and every function multiple times.

Author: Jake Gascon
Date: 10.27.2024
Assignment: Project Adventure Functions """
from math import floor
from operator import truediv
from gamefunctions import *

#set global variables for money, gold and max health
gold = 10
health = 30
maxHealth = 30

def option_handler(option):
    # Fight Monster
    if option == 1:
        fight_monster()
    # Sleep (Restore HP for the cost of 5 gold)
    elif option == 2:
        sleep()

def fight_monster():
    global health
    global gold
    #generate a new random monster from my list
    my_monster = new_random_monster()
    print(f"Watch out! A {my_monster['name']} appears!")

    #fight the monster
    while True:
        fight_run_choice = int(input(f"Would you like to fight this {my_monster['name']} (1) or run away (2)?"))
        if fight_run_choice == 1:
            #calculate your hit
            damage_dealt = int(random.random() * 10)
            #calculate opponents hit
            damage_taken = int(random.random() * my_monster['power'])
            my_monster['health'] -= damage_dealt
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
            display_fight_statistics(damage_dealt, damage_taken, health, my_monster['health'], {my_monster['name']})
        else:
            print("You run away!")
            break

def display_fight_statistics(damage_dealt, damage_taken, player_health, monster_health, monster_name):
    print(f"You hit a {damage_dealt} while the {monster_name} hit a {damage_taken} on you.")
    print(f"Your health is now at {player_health}. The {monster_name}'s health is now at {monster_health}.")

def sleep():
    global gold
    global health
    if gold >= 5:
        print("\nYou feel refreshed, however your pockets feel a little more empty than before...")
        health = maxHealth
        gold -= 5
        print(gold)
    else:
        print("\nSleeping is not an option, get back in and fight!")

if __name__ == '__main__':
    choice = 0
    #Loop through the game if the player has not quit
    while choice != 3:
        # Get the user fight options and send in the current health and gold values, validate input
        while True:
            get_user_options(health, gold)
            choice = int(input())

            #validate that the user entered a valid option and if not keep looping
            if choice in range (1, 4):
                break
            else:
                print("Invalid Selection, please try again.\n")

        option_handler(choice)