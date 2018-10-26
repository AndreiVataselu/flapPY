import pygame


def splash_screen(screen):
    # Configure title and description
    titleFont = pygame.font.Font("impact.ttf", 150)
    titleFont_shadow = pygame.font.Font("impact.ttf", 152)
    title = titleFont.render("flapPY", False, (255, 255, 255))
    title_shadow = titleFont_shadow.render("flapPY", False, (0, 0, 0))

    descriptionFont = pygame.font.Font("impact.ttf", 70)
    descriptionFont_shadow = pygame.font.Font("impact.ttf", 70)
    description = descriptionFont.render("Press space bar to start",  False, (255, 255, 255))
    description_shadow = descriptionFont_shadow.render("Press space bar to start", False, (0, 0, 0))

    screen.blit(title_shadow, (197, 95))
    screen.blit(title, (200, 100))
    screen.blit(description_shadow, (68, 380))
    screen.blit(description, (70, 383))


def lost_screen(screen, score, highscore):

    yourScoreFont = pygame.font.Font("impact.ttf", 70)
    yourScore = yourScoreFont.render("Your score: {0}".format(str(score)), False, (255, 255, 255))

    highScoreFont = pygame.font.Font("impact.ttf", 70)
    highScore = highScoreFont.render("High score: {0}".format(str(highscore)), False, (255, 255, 255))

    descriptionFont = pygame.font.Font("impact.ttf", 70)
    description = descriptionFont.render("Press space to restart",  False, (255, 255, 255))

    screen.blit(description, (85, 383))
    screen.blit(yourScore, (200, 100))
    screen.blit(highScore, (200, 200))
