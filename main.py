import sys
import pygame
from settings import Settings

def run_game():
    pygame.init()

    snabings = Settings()
    screen = pygame.display.set_mode((snabings.screen_width, snabings.screen_height))
    pygame.display.set_caption("Snabe")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(snabings.background_color)

        pygame.display.flip()

run_game()