import sys
import pygame
from settings import Settings

settings = Settings()

def update_screen(snabings, screen, snabe1, snabe2, timer):
    screen.fill(snabings.background_color)
    snabe1.blitme()
    snabe2.blitme()
    timer.blitme()
    # blits everything in food list
    for a in snabings.food_list:
        a.blitme()
    # blits everything in wafer list
    for b in snabings.wafer_list:
        b.blitme()

    pygame.display.flip()


def check_events(snabe1, snabe2):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            # Store info on whether or not this event occurs before either snabe has started moving
            s1_firstmove = snabe1.first_move()
            s2_firstmove = snabe2.first_move()

            if event.key == pygame.K_w and not snabe1.moving_down and not snabe1.moving_up:
                snabe1.set_direction("UP")

                # tells each segment to turn in this direction if the snabe is moving in a different direction
                if not s1_firstmove:
                    snabe1.turns[(snabe1.rect.centerx, snabe1.rect.centery)] = snabe1.get_direction()
                # used at beginning when snabe isnt moving: starts motion in selected direction
                else:
                    for x in snabe1.segments:
                        x.set_direction("UP")

            elif event.key == pygame.K_a and not snabe1.moving_right and not snabe1.moving_left:
                snabe1.set_direction("LEFT")

                # tells each segment to turn in this direction if the snabe is moving in a different direction
                snabe1.turns[(snabe1.rect.centerx, snabe1.rect.centery)] = snabe1.get_direction()
                if s1_firstmove:
                    for x in snabe1.segments:
                        x.set_direction("UP")

            elif event.key == pygame.K_s and not snabe1.moving_up and not snabe1.moving_down and not s1_firstmove:
                snabe1.set_direction("DOWN")

                # tells each segment to turn in this direction if the snabe is moving in a different direction
                snabe1.turns[(snabe1.rect.centerx, snabe1.rect.centery)] = snabe1.get_direction()

            elif event.key == pygame.K_d and not snabe1.moving_left and not snabe1.moving_right:
                snabe1.set_direction("RIGHT")

                # tells each segment to turn in this direction if the snabe is moving in a different direction
                snabe1.turns[(snabe1.rect.centerx, snabe1.rect.centery)] = snabe1.get_direction()
                if s1_firstmove:
                    for x in snabe1.segments:
                        x.set_direction("UP")

            if event.key == pygame.K_UP and not snabe2.moving_down and not snabe2.moving_up:
                snabe2.set_direction("UP")

                # tells each segment to turn in this direction if the snabe is moving in a different direction
                if not s2_firstmove:
                    snabe2.turns[(snabe2.rect.centerx, snabe2.rect.centery)] = snabe2.get_direction()
                # used at beginning when snabe isnt moving: starts motion in selected direction
                else:
                    for x in snabe2.segments:
                        x.set_direction("UP")

            elif event.key == pygame.K_LEFT and not snabe2.moving_right and not snabe2.moving_left:
                snabe2.set_direction("LEFT")

                # tells each segment to turn in this direction if the snabe is moving in a different direction
                snabe2.turns[(snabe2.rect.centerx, snabe2.rect.centery)] = snabe2.get_direction()
                if s2_firstmove:
                    for x in snabe2.segments:
                        x.set_direction("UP")

            elif event.key == pygame.K_DOWN and not snabe2.moving_up and not snabe2.moving_down and not s2_firstmove:
                snabe2.set_direction("DOWN")

                # tells each segment to turn in this direction if the snabe is moving in a different direction
                snabe2.turns[(snabe2.rect.centerx, snabe2.rect.centery)] = snabe2.get_direction()

            elif event.key == pygame.K_RIGHT and not snabe2.moving_left and not snabe2.moving_right:
                snabe2.set_direction("RIGHT")

                # tells each segment to turn in this direction if the snabe is moving in a different direction
                snabe2.turns[(snabe2.rect.centerx, snabe2.rect.centery)] = snabe2.get_direction()

                if s2_firstmove:
                    for x in snabe2.segments:
                        x.set_direction("UP")
