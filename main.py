import sys
import pygame
from settings import Settings
from snabe import Snabe
from Timer import Timer
from food import Food
from wafer import Wafer

import global_functions as gf
from threading import Thread

def run_game():
    pygame.init()

    #settings/constants file
    snabings = Settings()
    screen = pygame.display.set_mode((snabings.screen_width, snabings.screen_height))
    screen_rect = screen.get_rect()
    pygame.display.set_caption("Snabe")

    # Creates a dict to hold all currently existing entities as values and their rects as keys
    entities = list()

    # Creates a dict where keys are entity centerpoints and values are entity rects
    entities_rects = list()

    snabe1 = Snabe(screen, snabings, entities, entities_rects, 1)
    snabe2 = Snabe(screen, snabings, entities, entities_rects, 2)

    # list of food pellets to be displayed
    snabings.food_list.append(Food(screen, snabings, entities, entities_rects))

    # timer class object
    game_timer = Timer(screen, snabings.game_length)

    #established to regulate game speed
    clock = pygame.time.Clock()

    # stores total number of ticks required for the length of game
    timerThread = snabings.game_length * snabings.tick_rate

    # global tick rate established in settings.py
    tick_rate = snabings.tick_rate

    # length to be displayed on timer
    game_length = snabings.game_length

    # keeps track of each timer tick
    # starts at -1 because timer starts at 0
    food_ticks = -1

    # keeps track of each timer tick
    # in relevance to power-up spawns
    wafer_ticks = -1

    while True:
        # establishes tick rate for game
        clock.tick(tick_rate)

        gf.check_events(snabe1, snabe2)
        gf.update_screen(snabings, screen, snabe1, snabe2, game_timer)

        snabe1.move()
        snabe2.move()

        # regulates when the timer should tick in accordance
        # to game tick rate
        if timerThread % game_length == 0:
            game_timer.tick()
            food_ticks +=1
            wafer_ticks +=1
        if timerThread >=1:
            timerThread-=1
        else:
            timerThread = 0
            sys.exit()

        # this segment is responsible for spawning food
        # every n seconds
        if food_ticks == snabings.food_spawn_rate:
            snabings.food_list.append(Food(screen, snabings, entities, entities_rects))
            food_ticks = 0

        # this segment spawns a power-up wafer
        # every n seconds
        if wafer_ticks == snabings.wafer_spawn_rate:
            snabings.wafer_list.append(Wafer(screen, snabings, entities, entities_rects))
            wafer_ticks = 0

run_game()