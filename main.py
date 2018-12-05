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
        "initial": snabings.timer_value,
        "timer": 0,
        "food": -1,
        "wafer": -1,
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

        ####################################
        # Accounts for the amount of ticks #
        # needed to correctly time actions #
        ####################################
        ticks["timer"]+=1
        if ticks["timer"] == tick_rate:
            game_timer.tick()
            ticks["food"] += 1
            ticks["wafer"] += 1
            ticks["timer"] = 0
            ticks["initial"] = snabings.timer_value

        if snabings.timer_value >= 1:
            snabings.timer_value -=1
        else:
            snabings.timer_value = 0
            endScreen()
        ####################################

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

def startScreen():
    pygame.init()

    #settings/constants file
    snabings = Settings()
    screen = pygame.display.set_mode((snabings.screen_width, snabings.screen_height))
    screen_rect = screen.get_rect()
    pygame.display.set_caption("Snabe")
    screen.fill(snabings.background_color)

    clock = pygame.time.Clock()

    snabeSlither = {
        "frame": 1,
        1: "images/menu/snabeSlither1.png",
        2: "images/menu/snabeSlither2.png",
        3: "images/menu/snabeSlither3.png",
        4: "images/menu/snabeSlither4.png",
    }

    snabe_logo = pygame.image.load(snabeSlither[snabeSlither["frame"]])
    logo_rect = snabe_logo.get_rect()
    logo_rect.right = screen_rect.left
    logo_rect.centery = snabings.screen_height // 6

    snabe_text = pygame.image.load("images/menu/nabe.png")
    snabe_text_rect = snabe_text.get_rect()
    snabe_text_rect.left = screen_rect.right
    snabe_text_rect.centery = snabings.screen_height // 4

    while True:
        clock.tick(14)
        screen.fill(snabings.background_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run_game()

        #######################################################################
        # Snabe Slither Animation                                             #
        #######################################################################
        if snabeSlither["frame"] == 4:
            snabeSlither["frame"] = 1
        else:
            snabeSlither["frame"] += 1
        if logo_rect.centerx >= screen_rect.centerx:
            logo_rect.centerx = screen_rect.centerx
        else:
            logo_rect.centerx += 10
        snabe_logo = pygame.image.load(snabeSlither[snabeSlither["frame"]])
        screen.blit(snabe_logo, logo_rect)
        #######################################################################
        pygame.font.init()
        myfont = pygame.font.SysFont('Courier', 30)
        startPrompt = myfont.render('Welcome to Snabe! Press Space to Start!',False, (0,0,0))
        startRect = startPrompt.get_rect()
        startRect.centerx = screen_rect.centerx
        startRect.centery = screen_rect.centery
        screen.blit(startPrompt,startRect)

        pygame.display.flip()
def endScreen():
    pygame.init()

    #settings/constants file
    snabings = Settings()
    screen = pygame.display.set_mode((snabings.screen_width, snabings.screen_height))
    screen_rect = screen.get_rect()
    pygame.display.set_caption("Snabe")
    screen.fill(snabings.background_color)
    pygame.display.flip()
    while True:
        screen.fill(snabings.background_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run_game()
                elif event.key == pygame.K_ESCAPE:
                    startScreen()
        pygame.font.init()

        myfont = pygame.font.SysFont('Courier', 30)
        restartPrompt = myfont.render('Game over! Press Space to Play Again!', False, (0, 0, 0))
        restartRect = restartPrompt.get_rect()
        restartRect.centerx = screen_rect.centerx
        restartRect.centery = screen_rect.centery

        myfont = pygame.font.SysFont('Courier', 20)
        menuPrompt = myfont.render('Press Esc to go back to the main menu', False, (0, 0, 0))
        menuRect = menuPrompt.get_rect()
        menuRect.centerx = screen_rect.centerx
        menuRect.top = restartRect.bottom

        myfont = pygame.font.SysFont('Courier', 45)
        winnerPrompt = myfont.render('Winner!', False, (0, 0, 0))
        winnerRect = winnerPrompt.get_rect()
        winnerRect.centerx = screen_rect.centerx
        winnerRect.bottom = restartRect.top

        screen.blit(restartPrompt,restartRect)
        screen.blit(menuPrompt,menuRect)
        screen.blit(winnerPrompt, winnerRect)
        pygame.display.flip()
startScreen()
run_game()