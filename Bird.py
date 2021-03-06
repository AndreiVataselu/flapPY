import pygame


class Bird:

    def __init__(self, screen):
        # Initialize the bird
        self.x = 70
        self.y = 280
        self.width = 35
        self.screen = screen

        self.color = (0, 0, 0)

        self.falling_speed = 6
        # Create the rect of the bird
        self.rect = pygame.Rect(self.x, self.y, self.width, self.width)

    def draw(self):
        # Draws the bird every frame
        pygame.draw.circle(self.screen, self.color, [self.x, self.y], self.width)

    def fall(self):
        # Causes the bird to fall if SPACE KEY is not pressed.
        self.y += self.falling_speed

    def rise(self):
        # Triggers whenever the SPACE KEY is pressed.
        if self.y - 75 < 35:
            self.y -= self.y - 15
        else:
            self.y -= 75
