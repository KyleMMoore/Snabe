import sys
import pygame
from global_toolbox import GlobalSettings, GlobalFunctions, GlobalVars
from snabe import Snabe
from Timer import Timer
from food import Food
from wafer import Wafer

def run_game():
    pygame.init()

    #settings/constants file
    snabings = GlobalSettings()
    gv = GlobalVars()
    gf = GlobalFunctions(gv)

    screen = pygame.display.set_mode((snabings.screen_width, snabings.screen_height))
    pygame.display.set_caption("Snabe")
    pygame.display.set_icon(pygame.image.load("images/menu/snabeSlither4.png"))


    snabe1 = Snabe(screen, gv, 1)
    snabe2 = Snabe(screen, gv, 2)

    # list of food pellets to be displayed
    gv.food_list.append(Food(screen, gv))
    gv.food_list[0].setLocation(snabings.screen_width//2, snabings.screen_height//2)

    # timer class object
    game_timer = Timer(screen, snabings.game_length)

    #established to regulate game speed
    clock = pygame.time.Clock()

    # global tick rate established in settings.py
    tick_rate = snabings.tick_rate

    # keeps track of tick counts
    ticks = {
        "initial": gv.timer_value,
        "timer": 0,
        "food": -1,
        "wafer": -1,
    }

    while gv.timer_value != 0 and snabe1.score != 0 and snabe2.score != 0:
        # establishes tick rate for game
        clock.tick(tick_rate)

        gf.check_events(snabe1, snabe2)

        snabe1.update()
        snabe2.update()

        gf.update_screen(screen, game_timer)

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
            ticks["initial"] = gv.timer_value

        if gv.timer_value >= 1:
            gv.timer_value -= 1
        else:
            gv.timer_value = 0

        ####################################

        # this segment is responsible for spawning food
        # every n seconds
        if ticks["food"] == snabings.food_spawn_rate:
            gv.food_list.append((Food(screen, gv)))
            ticks["food"] = 0

        # this segment spawns a power-up wafer
        # every n seconds
        if ticks["wafer"] == snabings.wafer_spawn_rate:
            gv.wafer_list.append(Wafer(screen, gv))
            ticks["wafer"] = 0
    endScreen()


def startScreen():
    pygame.init()

    #settings/constants file
    snabings = GlobalSettings()
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
        screen.blit(startPrompt, startRect)

        pygame.display.flip()


def endScreen():
    pygame.init()

    #settings/constants file
    snabings = GlobalSettings()
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
