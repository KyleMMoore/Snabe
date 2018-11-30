import sys
import pygame
from settings import Settings
from snabe import Snabe
from Timer import Timer
import global_functions as gf
from threading import Thread

def run_game():
    pygame.init()

    #settings/constants file
    snabings = Settings()
    screen = pygame.display.set_mode((snabings.screen_width, snabings.screen_height))
    pygame.display.set_caption("Snabe")

    snabe1 = Snabe(screen, snabings, 1)
    snabe2 = Snabe(screen, snabings, 2)

    game_clock = pygame.time.Clock()
    game_time = Timer(screen, 60)

    while game_time.time != 0:
        gf.check_events(snabe1, snabe2)
        gf.update_screen(snabings, screen, snabe1, snabe2, game_time)
        snabe1.move()
        snabe2.move()

run_game()