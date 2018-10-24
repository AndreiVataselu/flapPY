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
        self.y2 = self.random + 200

        self.rect1 = pygame.Rect(self.x, self.y1, self.width, self.random)
        self.rect2 = pygame.Rect(self.x, self.y2, self.width, 600-self.y2)

    def run(self):
        self.rect1.x -= 5
        self.rect2.x -= 5

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect1)
        pygame.draw.rect(self.screen, self.color, self.rect2)
