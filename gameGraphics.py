""" Project Adventure Functions Module

This module calls upon gamefunctions.py and runs each and every function multiple times.

Author: Jake Gascon
Date: 12/8/2024
Assignment: Project Adventure Functions - Assignment 14"""

import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 320
SCREEN_HEIGHT = 320
GRID_SIZE = 32
GRID_ROWS = 10
GRID_COLS = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Graphics")

# Load images
try:
    knight_img = pygame.image.load("Knight.png")
    knight_img = pygame.transform.scale(knight_img, (GRID_SIZE, GRID_SIZE))
except:
    knight_img = None

try:
    dragon_img = pygame.image.load("Dragon.png")
    dragon_img = pygame.transform.scale(dragon_img, (GRID_SIZE, GRID_SIZE))
except:
    dragon_img = None

# Initial position of the player square
player = pygame.Rect(0, 0, GRID_SIZE, GRID_SIZE)


# Wandering Monster Class
class WanderingMonster:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)

    def move(self):
        """Move the monster randomly in one of four directions, if within grid."""
        direction = random.choice(["up", "down", "left", "right"])
        if direction == "up" and self.rect.y - GRID_SIZE >= 0:
            self.rect.y -= GRID_SIZE
        elif direction == "down" and self.rect.y + GRID_SIZE < SCREEN_HEIGHT:
            self.rect.y += GRID_SIZE
        elif direction == "left" and self.rect.x - GRID_SIZE >= 0:
            self.rect.x -= GRID_SIZE
        elif direction == "right" and self.rect.x + GRID_SIZE < SCREEN_WIDTH:
            self.rect.x += GRID_SIZE


# Initialize monsters
monsters = [WanderingMonster(random.randint(0, GRID_COLS - 1) * GRID_SIZE,
                              random.randint(0, GRID_ROWS - 1) * GRID_SIZE)]

# Game loop
running = True
player_moves = 0  # Track player moves to alternate monster movement

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and player.y + GRID_SIZE < SCREEN_HEIGHT:
                player.y += GRID_SIZE
            elif event.key == pygame.K_UP and player.y - GRID_SIZE >= 0:
                player.y -= GRID_SIZE
            elif event.key == pygame.K_RIGHT and player.x + GRID_SIZE < SCREEN_WIDTH:
                player.x += GRID_SIZE
            elif event.key == pygame.K_LEFT and player.x - GRID_SIZE >= 0:
                player.x -= GRID_SIZE
            elif event.key == pygame.K_q:  # Quit when 'q' is pressed
                running = False

            # Increment player move count
            player_moves += 1

            # Move monsters every other player move
            if player_moves % 2 == 0:
                for monster in monsters:
                    monster.move()

    # Check for encounters
    for monster in monsters:
        if player.colliderect(monster.rect):
            print("Encounter! You found a monster!")
            monsters.remove(monster)

    # If all monsters are gone, spawn two new ones
    if not monsters:
        print("You cleared the monsters! Two new monsters appear!")
        monsters = [WanderingMonster(random.randint(0, GRID_COLS - 1) * GRID_SIZE,
                                      random.randint(0, GRID_ROWS - 1) * GRID_SIZE)
                    for _ in range(2)]

    # Draw everything
    screen.fill(WHITE)  # Clear screen

    # Draw the player
    if knight_img:
        screen.blit(knight_img, (player.x, player.y))
    else:
        pygame.draw.rect(screen, BLACK, player)

    # Draw each monster
    for monster in monsters:
        if dragon_img:
            screen.blit(dragon_img, (monster.rect.x, monster.rect.y))
        else:
            pygame.draw.rect(screen, RED, monster.rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()


