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
    #entities = list()

    # Creates a dict where keys are entity centerpoints and values are entity rects
    #entities_rects = list()

    snabe1 = Snabe(screen, snabings, 1)
    snabe2 = Snabe(screen, snabings,2)

    # list of food pellets to be displayed
    snabings.food_list.append(Food(screen, snabings))
    snabings.food_list[0].setLocation(snabings.screen_width//2,snabings.screen_height//2)

    # timer class object
    game_timer = Timer(screen, snabings.game_length)

    #established to regulate game speed
    clock = pygame.time.Clock()

    # global tick rate established in settings.py
    tick_rate = snabings.tick_rate

    # length to be displayed on timer
    game_length = snabings.game_length

    # keeps track of tick counts
    ticks = {
        "timer" : -1,
        "food" : -1,
        "wafer" : -1,
    }

    while True:
        # establishes tick rate for game
        clock.tick(tick_rate)

        gf.check_events(snabe1, snabe2)

        #TODO: use the global entities list to update the screen?
        # -Kyle
        #TODO: store EVERYTHING in settings.py? That way all we pass is snabings
        # -Kyle pt. 2
        gf.update_screen(snabings, screen, snabe1, snabe2, game_timer)

        snabe1.update()
        snabe2.update()

        #TODO: Try and fix this to regulate the game clock and timer
        #if ticks["timer"] == snabings.tick_rate:
        #    game_timer.tick()
        #    ticks["food"] += 1
        #    ticks["wafer"] += 1
        #    ticks["timer"] = 0

        # regulates when the timer should tick in accordance
        # to game tick rate
        if snabings.timer_value % game_length == 0:
            game_timer.tick()
            ticks["food"] += 1
            ticks["wafer"] += 1
        if snabings.timer_value >= 1:
            snabings.timer_value -=1
        else:
            snabings.timer_value = 0
            sys.exit()

        # this segment is responsible for spawning food
        # every n seconds
        if ticks["food"] == snabings.food_spawn_rate:
            snabings.food_list.append((Food(screen, snabings)))
            ticks["food"] = 0

        # this segment spawns a power-up wafer
        # every n seconds
        if ticks["wafer"] == snabings.wafer_spawn_rate:
            snabings.wafer_list.append(Wafer(screen, snabings))
            ticks["wafer"] = 0

run_game()