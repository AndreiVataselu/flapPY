# This file contains all the functions of the game to keep the main loop fresh
# and short
import pygame, sys
from Obstacle import Obstacle

NEW_OBS = pygame.USEREVENT+1
pygame.time.set_timer(NEW_OBS, 1250)


def check_events(bird, obstacles, screen):
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
        elif event.type == NEW_OBS and game.GAME_STARTED:
            # Spawn obstacle every 3 seconds
            new_obstacle = Obstacle(screen)
            obstacles.add(new_obstacle)
