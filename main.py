import sys
import pygame
from settings import Settings
from snabe import Snabe
from Timer import Timer
from food import Food

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

    food = Food(screen)

    game_timer = Timer(screen, snabings.game_length)
    clock = pygame.time.Clock()

    timerThread = snabings.game_length * snabings.tick_rate
    tick_rate = snabings.tick_rate
    game_length = snabings.game_length

    while True:

        clock.tick(tick_rate)

        gf.check_events(snabe1, snabe2)
        gf.update_screen(snabings, screen, snabe1, snabe2, game_timer, food)

        snabe1.move()
        snabe2.move()

        if timerThread % game_length == 0:
            game_timer.tick()
        if timerThread >=1:
            food.feed()
            timerThread-=1
        else:
            timerThread = 0

run_game()