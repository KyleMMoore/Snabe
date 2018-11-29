import sys
import pygame

def update_screen(snabings, screen, snabe1, snabe2):
    screen.fill(snabings.background_color)
    snabe1.blitme()
    snabe2.blitme()

    pygame.display.flip()


def check_events(snabe1, snabe2):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and not snabe1.moving_down:
                snabe1.moving_up = True
                snabe1.moving_down = False
                snabe1.moving_left = False
                snabe1.moving_right = False
            elif event.key == pygame.K_a and not snabe1.moving_right:
                snabe1.moving_left = True
                snabe1.moving_right = False
                snabe1.moving_up = False
                snabe1.moving_down = False
            elif event.key == pygame.K_s and not snabe1.moving_up:
                snabe1.moving_down = True
                snabe1.moving_up = False
                snabe1.moving_left = False
                snabe1.moving_right = False
            elif event.key == pygame.K_d and not snabe1.moving_left:
                snabe1.moving_right = True
                snabe1.moving_left = False
                snabe1.moving_up = False
                snabe1.moving_down = False

            if event.key == pygame.K_UP and not snabe2.moving_down:
                snabe2.moving_up = True
                snabe2.moving_down = False
                snabe2.moving_left = False
                snabe2.moving_right = False
            elif event.key == pygame.K_LEFT and not snabe2.moving_right:
                snabe2.moving_left = True
                snabe2.moving_right = False
                snabe2.moving_up = False
                snabe2.moving_down = False
            elif event.key == pygame.K_DOWN and not snabe2.moving_up:
                snabe2.moving_down = True
                snabe2.moving_up = False
                snabe2.moving_left = False
                snabe2.moving_right = False
            elif event.key == pygame.K_RIGHT and not snabe2.moving_left:
                snabe2.moving_right = True
                snabe2.moving_left = False
                snabe2.moving_up = False
                snabe2.moving_down = False






