import pygame
from Bird import Bird
import game_functions as gf
from pygame.sprite import Group


class Game:
    """Where all the magic happens"""
    def __init__(self):
        # Initialize the game's variables
        self.GAME_STARTED = False
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("flapPY")
        self.bird = Bird(self.screen)
        self.obstacles = Group()

    def run_game(self):
        while True:
            # Checking user's input
            gf.check_events(self.bird, self.obstacles, self.screen)

            # Update the screen
            self.screen.fill((215, 225, 155))

            if self.GAME_STARTED:
                # Bird only starts to fall if the game started
                self.bird.fall()

            for obstacle in self.obstacles:
                obstacle.run()
                obstacle.draw()

            self.bird.draw()
            pygame.display.flip()


game = Game()
game.run_game()

