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
            if event.key == pygame.K_w:
                snabe1.moving_up = True
                snabe1.moving_down = False
                snabe1.moving_left = False
                snabe1.moving_right = False
            elif event.key == pygame.K_a:
                snabe1.moving_left = True
                snabe1.moving_right = False
                snabe1.moving_up = False
                snabe1.moving_down = False
            elif event.key == pygame.K_s:
                snabe1.moving_down = True
                snabe1.moving_up = False
                snabe1.moving_left = False
                snabe1.moving_right = False
            elif event.key == pygame.K_d:
                snabe1.moving_right = True
                snabe1.moving_left = False
                snabe1.moving_up = False
                snabe1.moving_down = False

            if event.key == pygame.K_UP:
                snabe2.moving_up = True
                snabe2.moving_down = False
                snabe2.moving_left = False
                snabe2.moving_right = False
            elif event.key == pygame.K_LEFT:
                snabe2.moving_left = True
                snabe2.moving_right = False
                snabe2.moving_up = False
                snabe2.moving_down = False
            elif event.key == pygame.K_DOWN:
                snabe2.moving_down = True
                snabe2.moving_up = False
                snabe2.moving_left = False
                snabe2.moving_right = False
            elif event.key == pygame.K_RIGHT:
                snabe2.moving_right = True
                snabe2.moving_left = False
                snabe2.moving_up = False
                snabe2.moving_down = False






