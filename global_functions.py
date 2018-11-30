import sys
import pygame

def update_screen(snabings, screen, snabe1, snabe2, timer, food):
    screen.fill(snabings.background_color)
    snabe1.blitme()
    snabe2.blitme()
    timer.blitme()
    food.blitme()

    pygame.display.flip()


def check_events(snabe1, snabe2):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            snabe1_notFirstMove = snabe1.is_moving()
            snabe2_notFirstMove = snabe2.is_moving()
            if event.key == pygame.K_w and not snabe1.moving_down and not snabe1.moving_up:
                snabe1.moving_up = True
                snabe1.moving_down = False
                snabe1.moving_left = False
                snabe1.moving_right = False

                # tells each segment to turn in this direction if the snabe is moving in a different direction
                if snabe1_notFirstMove:
                    snabe1.turning_points.append((snabe1.rect.centerx, snabe1.rect.centery))
                # used at beginning when snabe isnt moving: starts motion in selected direction
                else:
                    for x in snabe1.segments:
                        x.moving_up = True
                        x.moving_down = False
                        x.moving_left = False
                        x.moving_right = False

            elif event.key == pygame.K_a and not snabe1.moving_right and not snabe1.moving_left:
                snabe1.moving_left = True
                snabe1.moving_right = False
                snabe1.moving_up = False
                snabe1.moving_down = False

                # tells each segment to turn in this direction if the snabe is moving in a different direction
                snabe1.turning_points.append((snabe1.rect.centerx, snabe1.rect.centery))
                if not snabe1_notFirstMove:
                    for x in snabe1.segments:
                        x.moving_up = True

            elif event.key == pygame.K_s and not snabe1.moving_up and not snabe1.moving_down and snabe1_notFirstMove:
                snabe1.moving_down = True
                snabe1.moving_up = False
                snabe1.moving_left = False
                snabe1.moving_right = False

                # tells each segment to turn in this direction if the snabe is moving in a different direction
                snabe1.turning_points.append((snabe1.rect.centerx, snabe1.rect.centery))

            elif event.key == pygame.K_d and not snabe1.moving_left and not snabe1.moving_right:
                snabe1.moving_right = True
                snabe1.moving_left = False
                snabe1.moving_up = False
                snabe1.moving_down = False

                # tells each segment to turn in this direction if the snabe is moving in a different direction
                snabe1.turning_points.append((snabe1.rect.centerx, snabe1.rect.centery))
                if not snabe1_notFirstMove:
                    for x in snabe1.segments:
                        x.moving_up = True

            if event.key == pygame.K_UP and not snabe2.moving_down and not snabe2.moving_up:
                snabe2.moving_up = True
                snabe2.moving_down = False
                snabe2.moving_left = False
                snabe2.moving_right = False

                # tells each segment to turn in this direction if the snabe is moving in a different direction
                if snabe2_notFirstMove:
                    snabe2.turning_points.append((snabe2.rect.centerx, snabe2.rect.centery))
                # used at beginning when snabe isnt moving: starts motion in selected direction
                else:
                    for x in snabe2.segments:
                        x.moving_up = True
                        x.moving_down = False
                        x.moving_left = False
                        x.moving_right = False

            elif event.key == pygame.K_LEFT and not snabe2.moving_right and not snabe2.moving_left:
                snabe2.moving_left = True
                snabe2.moving_right = False
                snabe2.moving_up = False
                snabe2.moving_down = False

                # tells each segment to turn in this direction if the snabe is moving in a different direction
                snabe2.turning_points.append((snabe2.rect.centerx, snabe2.rect.centery))
                if not snabe2_notFirstMove:
                    for x in snabe2.segments:
                        x.moving_up = True

            elif event.key == pygame.K_DOWN and not snabe2.moving_up and not snabe2.moving_down and snabe2_notFirstMove:
                snabe2.moving_down = True
                snabe2.moving_up = False
                snabe2.moving_left = False
                snabe2.moving_right = False

                # tells each segment to turn in this direction if the snabe is moving in a different direction
                snabe2.turning_points.append((snabe2.rect.centerx, snabe2.rect.centery))

            elif event.key == pygame.K_RIGHT and not snabe2.moving_left and not snabe2.moving_right:
                snabe2.moving_right = True
                snabe2.moving_left = False
                snabe2.moving_up = False
                snabe2.moving_down = False

                # tells each segment to turn in this direction if the snabe is moving in a different direction
                snabe2.turning_points.append((snabe2.rect.centerx, snabe2.rect.centery))
                if not snabe2_notFirstMove:
                    for x in snabe2.segments:
                        x.moving_up = True






