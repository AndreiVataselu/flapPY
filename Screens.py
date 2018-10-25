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


def lost_screen(screen, score):

    yourScoreFont = pygame.font.Font("impact.ttf", 100)
    yourScore = yourScoreFont.render("Your score", False, (255, 255, 255))

    scoreFont = pygame.font.Font("impact.ttf", 158)

    scoreW = scoreFont.render(str(score), False, (255, 255, 255))
    scoreRect = scoreW.get_rect(center=(400, 300))

    descriptionFont = pygame.font.Font("impact.ttf", 70)
    description = descriptionFont.render("Press space bar to start",  False, (255, 255, 255))

    screen.blit(description, (70, 383))
    screen.blit(yourScore, (175, 50))
    screen.blit(scoreW, scoreRect)
