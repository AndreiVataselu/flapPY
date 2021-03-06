import pygame
from pygame.sprite import Sprite
from random import randint


class Obstacle(Sprite):

    def __init__(self, screen):
        super().__init__()

        self.screen = screen

        # Default attributes for obstacle
        self.width = 35
        self.x = 800
        self.color = (50, 205, 50)

        # Creates the obstacle rect around the passing gate
        self.y1 = 0
        self.random = randint(20, 380)
        self.y2 = self.random + 210 # random + height of the gate

        self.rect1 = pygame.Rect(self.x, self.y1, self.width, self.random)
        self.rect2 = pygame.Rect(self.x, self.y2, self.width, 600-self.y2)

        # Passing flag. If the bird passed the obstacle, give score 1.
        self.passed = False

    def run(self):
        self.rect1.x -= 7
        self.rect2.x -= 7

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect1)
        pygame.draw.rect(self.screen, self.color, self.rect2)

    def score(self):
        if not self.passed:
            self.passed = True
            return 1
        return 0
