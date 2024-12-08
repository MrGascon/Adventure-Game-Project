""" Project Adventure Functions Module

This module calls upon gamefunctions.py and runs each and every function multiple times.

Author: Jake Gascon
Date: 12/8/2024
Assignment: Project Adventure Functions - Assignment 12"""

import pygame

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
RED = (255, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Graphics")

# Initial position of the square
square = pygame.Rect(0, 0, GRID_SIZE, GRID_SIZE)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and square.y + GRID_SIZE < SCREEN_HEIGHT:
                square.y += GRID_SIZE
            elif event.key == pygame.K_UP and square.y - GRID_SIZE >= 0:
                square.y -= GRID_SIZE
            elif event.key == pygame.K_RIGHT and square.x + GRID_SIZE < SCREEN_WIDTH:
                square.x += GRID_SIZE
            elif event.key == pygame.K_LEFT and square.x - GRID_SIZE >= 0:
                square.x -= GRID_SIZE
            elif event.key == pygame.K_q:  # Quit when 'q' is pressed
                running = False

    # Draw everything
    screen.fill(WHITE)  # Clear screen
    pygame.draw.rect(screen, RED, square)  # Draw the square

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
