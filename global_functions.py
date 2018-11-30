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
            if event.key == pygame.K_w and not snabe1.moving_down:
                snabe1.moving_up = True
                snabe1.moving_down = False
                snabe1.moving_left = False
                snabe1.moving_right = False

                # tells each segment to turn in this direction if the snabe is moving in a different direction
                if snabe1_notFirstMove:
                    turning_point_x = snabe1.rect.centerx
                    turning_point_y = snabe1.rect.centery
                    for x in snabe1.segments:
                        x.set_turning_point("UP", turning_point_x, turning_point_y)
                # used at beginning when snabe isnt moving: starts motion in selected direction
                else:
                    for x in snabe1.segments:
                        x.moving_up = True
                        x.moving_down = False
                        x.moving_left = False
                        x.moving_right = False

            elif event.key == pygame.K_a and not snabe1.moving_right:
                snabe1.moving_left = True
                snabe1.moving_right = False
                snabe1.moving_up = False
                snabe1.moving_down = False

                # tells each segment to turn in this direction if the snabe is moving in a different direction
                turning_point_x = snabe1.rect.centerx
                turning_point_y = snabe1.rect.centery
                for x in snabe1.segments:
                    if not snabe1_notFirstMove:
                        x.moving_up = True
                    x.set_turning_point("LEFT", turning_point_x, turning_point_y)

            elif event.key == pygame.K_s and not snabe1.moving_up:
                snabe1.moving_down = True
                snabe1.moving_up = False
                snabe1.moving_left = False
                snabe1.moving_right = False

                # tells each segment to turn in this direction if the snabe is moving in a different direction
                turning_point_x = snabe1.rect.centerx
                turning_point_y = snabe1.rect.centery
                for x in snabe1.segments:
                    x.set_turning_point("DOWN", turning_point_x, turning_point_y)

            elif event.key == pygame.K_d and not snabe1.moving_left:
                snabe1.moving_right = True
                snabe1.moving_left = False
                snabe1.moving_up = False
                snabe1.moving_down = False

                # tells each segment to turn in this direction if the snabe is moving in a different direction
                turning_point_x = snabe1.rect.centerx
                turning_point_y = snabe1.rect.centery
                for x in snabe1.segments:
                    if not snabe1_notFirstMove:
                        x.moving_up = True
                    x.set_turning_point("RIGHT", turning_point_x, turning_point_y)

            if event.key == pygame.K_UP and not snabe2.moving_down:
                snabe2.moving_up = True
                snabe2.moving_down = False
                snabe2.moving_left = False
                snabe2.moving_right = False

                # tells each segment to turn in this direction if the snabe is moving in a different direction
                if snabe2_notFirstMove:
                    turning_point_x = snabe2.rect.centerx
                    turning_point_y = snabe2.rect.centery
                    for x in snabe2.segments:
                        x.set_turning_point("UP", turning_point_x, turning_point_y)
                # used at beginning when snabe isnt moving: starts motion in selected direction
                else:
                    for x in snabe2.segments:
                        x.moving_up = True
                        x.moving_down = False
                        x.moving_left = False
                        x.moving_right = False

            elif event.key == pygame.K_LEFT and not snabe2.moving_right:
                snabe2.moving_left = True
                snabe2.moving_right = False
                snabe2.moving_up = False
                snabe2.moving_down = False

                # tells each segment to turn in this direction if the snabe is moving in a different direction
                turning_point_x = snabe2.rect.centerx
                turning_point_y = snabe2.rect.centery
                for x in snabe2.segments:
                    if not snabe2_notFirstMove:
                        x.moving_up = True
                    x.set_turning_point("LEFT", turning_point_x, turning_point_y)

            elif event.key == pygame.K_DOWN and not snabe2.moving_up:
                snabe2.moving_down = True
                snabe2.moving_up = False
                snabe2.moving_left = False
                snabe2.moving_right = False

                # tells each segment to turn in this direction if the snabe is moving in a different direction
                if snabe2_notFirstMove:
                    turning_point_x = snabe2.rect.centerx
                    turning_point_y = snabe2.rect.centery
                    for x in snabe2.segments:
                        x.set_turning_point("DOWN", turning_point_x, turning_point_y)

            elif event.key == pygame.K_RIGHT and not snabe2.moving_left:
                snabe2.moving_right = True
                snabe2.moving_left = False
                snabe2.moving_up = False
                snabe2.moving_down = False

                # tells each segment to turn in this direction if the snabe is moving in a different direction
                turning_point_x = snabe2.rect.centerx
                turning_point_y = snabe2.rect.centery
                for x in snabe2.segments:
                    if not snabe2_notFirstMove:
                        x.moving_up = True
                    x.set_turning_point("RIGHT", turning_point_x, turning_point_y)






