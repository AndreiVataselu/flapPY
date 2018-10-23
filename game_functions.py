# This file contains all the functions of the game to keep the main loop fresh
# and short
import pygame, sys


def check_events(bird):
    from game import game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not game.GAME_STARTED:
                    game.GAME_STARTED = True
                    bird.rise()
                else:
                    bird.rise()
