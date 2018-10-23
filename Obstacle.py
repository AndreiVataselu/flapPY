import pygame
from pygame.sprite import Sprite


class Obstacle(Sprite):

    def __init__(self, screen):
        super().__init__()

        self.screen = screen
        self.y = 0
        self.x = 800
        self.width = 35

        self.color = (50, 205, 50)

        self.rect = pygame.Rect(self.x, self.y, self.width, 600)

    def run(self):
        self.rect.x -= 5

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
