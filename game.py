import pygame
from Bird import Bird
import game_functions as gf
from pygame.sprite import Group
import Screens as show_screen
from Database import Database


class Game:
    """Where all the magic happens"""
    def __init__(self):
        # Initialize the game's variables
        self.SPLASH_SCREEN = True
        self.GAME_STARTED = False
        self.GAME_LOST = False
        self.database = Database()

        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("flapPY")
        self.bird = Bird(self.screen)
        self.obstacles = Group()
        self.score = 0
        self.scoreFont = pygame.font.Font("impact.ttf", 55)
        self.shadowFont = pygame.font.Font("impact.ttf", 59)

    def run_game(self):
        while True:
            # Checking user's input
            gf.check_events(self.bird, self.obstacles, self.screen)

            # Update the screen
            self.screen.fill((215, 225, 155))

            if self.GAME_STARTED:
                # Bird only starts to fall if the game started
                self.bird.fall()

                # Draws obstacles
                for obstacle in self.obstacles:
                    obstacle.run()
                    obstacle.draw()

                    if obstacle.rect1.x < -10:
                        # Remove any obstacle that has been out of the screen.
                        self.obstacles.remove(obstacle)

                self.bird.draw()

                # Show the scoreboard
                text = self.scoreFont.render(str(self.score), False, (255, 255, 255))
                shadow = self.shadowFont.render(str(self.score), False, (0, 0, 0))
                self.screen.blit(shadow, (400, 40))
                self.screen.blit(text, (400, 40))

            elif self.SPLASH_SCREEN:
                show_screen.splash_screen(self.screen)

            elif self.GAME_LOST:
                if self.database.exists():
                    # Update the high score from the DB.
                    if self.score > self.database.get_highscore():
                        self.database.update_highscore(self.score)
                        print("Score updated: {0}".format(self.database.get_highscore()))
                else:
                    # Create a DB if it doesn't exist
                    self.database.insert_highscore(self.score)
                    print("Score added!")

                show_screen.lost_screen(self.screen, self.score, self.database.get_highscore())

            gf.check_collision(self.bird, self.obstacles)
            gf.score_update(self.obstacles)

            pygame.display.flip()

    def restart_game(self):
        self.GAME_STARTED = True
        self.GAME_LOST = False
        self.bird = Bird(self.screen)
        self.obstacles = Group()
        self.score = 0


game = Game()
game.run_game()

