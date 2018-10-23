import pygame
from Bird import Bird
import game_functions as gf


class Game:
    """Where all the magic happens"""
    def __init__(self):
        # Initialize the game's variables
        self.GAME_STARTED = False
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("flapPY")
        self.bird = Bird(self.screen)

    def run_game(self):
        while True:
            # Checking user's input
            gf.check_events(self.bird)

            # Update the screen
            self.screen.fill((215, 225, 155))

            if self.GAME_STARTED:
                # Bird only starts to fall if the game started
                self.bird.fall()

            self.bird.draw()
            pygame.display.flip()


game = Game()
game.run_game()

