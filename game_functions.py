# This file contains all the functions of the game to keep the main loop fresh
# and short
import pygame, sys
from Obstacle import Obstacle

NEW_OBS = pygame.USEREVENT + 1
pygame.time.set_timer(NEW_OBS, 1350)


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
                elif not game.GAME_LOST:
                    bird.rise()
        elif event.type == NEW_OBS and game.GAME_STARTED and not game.GAME_LOST:
            # Spawn obstacle every 3 seconds
            new_obstacle = Obstacle(screen)
            obstacles.add(new_obstacle)


def check_collision(bird, obstacles):
    from game import game
    if not game.GAME_LOST:
        for obstacle in obstacles:
            # Check if bird is touching any of the pipes
            if obstacle.rect1.x <= bird.rect.x + bird.width:
                if bird.y - 7 < obstacle.rect1.height or bird.y + 7 > obstacle.rect2.y:
                    game.GAME_LOST = True
                    bird.falling_speed = 25
                    print("Game lost!")


def score_update(obstacles):
    from game import game
    for obstacle in obstacles:
        if obstacle.rect1.x < 69 and not game.GAME_LOST:
            game.score += obstacle.score()
