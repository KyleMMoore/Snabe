import sys
import pygame


# A file for all global information

# Contains constants about game operation
# These values should never change during runtime
# Therefore each class creates its own instance of this class
class GlobalSettings:
    """Snabe settings and constants"""

    def __init__(self):
        """Init the game settings"""
        # screen settings
        self.screen_width = 800
        self.screen_height = 800
        self.background_color = (255, 255, 255)

        self.play_area_height = 140

        self.background_image = pygame.image.load("images/background/background.png")
        self.background_rect = self.background_image.get_rect()

        #snabe speed
        self.base_speed = 1

        #constants for calculating game speed:time
        # MAX GAME LENGTH IS 99, ANYTHING HIGHER IS SET TO 99
        # Minimum playable game time is 1, anything lower and the game goes straight to end menu
        self.tick_rate = 150
        self.game_length = 60

        #constants to determine spawn rates (per n seconds)
        self.food_spawn_rate = 1
        self.wafer_spawn_rate = 7

        #constants to determine each power-up's active time
        self.sword_time = 6
        self.shield_time = 10

        #constants to determine each power-up's spawn rate
        #value is displayed as a percentage of 100
        self.sword_rate = 75
        self.shield_rate = 25

        #calculations that regulate seconds:tick rate
        self.sword_time = self.sword_time * self.tick_rate
        self.shield_time = self.shield_time * self.tick_rate

        #sets location of background image
        self.background_rect.centerx = self.screen_width//2
        self.background_rect.centery = self.screen_height//2


# Contains some functions used by the game itself
class GlobalFunctions:
    def __init__(self, global_vars):
        self.snabings = GlobalSettings()
        self.gv = global_vars

    # Keeps things drawn on the screen
    def update_screen(self, screen, timer):
        screen.fill(self.snabings.background_color)
        screen.blit(self.snabings.background_image,self.snabings.background_rect)
        timer.blitme()
        for x in self.gv.entities:
            x.blitme()

        pygame.display.flip()

    def check_events(self, snabe1, snabe2):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                ############
                # Player 1 #
                ############
                # All segments must start off moving upward
                # If the head moves in a different direction to start,
                # the segments will turn at the head's starting point.
                # Makes sure keypresses belong to that snabe and first move can't be down
                if snabe1.first_move() \
                        and (event.key == pygame.K_w or event.key == pygame.K_a or event.key == pygame.K_d):
                    for x in snabe1.segments:
                        x.set_direction("UP")

                # Move up if W key is pressed
                # Also protects against turning 180 degrees or "turning" in the direction you're currently moving
                if event.key == pygame.K_w and not snabe1.moving_down and not snabe1.moving_up:
                    snabe1.set_direction("UP")

                elif event.key == pygame.K_a and not snabe1.moving_right and not snabe1.moving_left:
                    snabe1.set_direction("LEFT")

                # Makes sure that this doesn't work if this is the snabe's first move
                elif event.key == pygame.K_s and not snabe1.moving_up and not snabe1.moving_down\
                        and not snabe1.first_move():
                    snabe1.set_direction("DOWN")

                elif event.key == pygame.K_d and not snabe1.moving_left and not snabe1.moving_right:
                    snabe1.set_direction("RIGHT")

                ############
                # Player 2 #
                ############
                # This all works the same as the Player 1 code
                # except for which keys are checked
                if snabe2.first_move() \
                        and (event.key == pygame.K_UP or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                    for x in snabe2.segments:
                        x.set_direction("UP")

                if event.key == pygame.K_UP and not snabe2.moving_down and not snabe2.moving_up:
                    snabe2.set_direction("UP")

                elif event.key == pygame.K_LEFT and not snabe2.moving_right and not snabe2.moving_left:
                    snabe2.set_direction("LEFT")

                elif event.key == pygame.K_DOWN and not snabe2.moving_up and not snabe2.moving_down \
                        and not snabe2.first_move():
                    snabe2.set_direction("DOWN")

                elif event.key == pygame.K_RIGHT and not snabe2.moving_left and not snabe2.moving_right:
                    snabe2.set_direction("RIGHT")
                print(snabe2.turns)



# Stores global variables
# Unlike settings, this needs to be created once in main and then passed to all objects
# Otherwise each class has its own instance and the values get desynced
class GlobalVars:
    def __init__(self):
        # Allows access to game time settings for the timer value
        snabings = GlobalSettings()

        # Stores the active food and wafer objects
        self.food_list = []
        self.wafer_list = []

        # stores remaining time in game session
        self.timer_value = snabings.game_length * snabings.tick_rate

        # Stores all entities
        self.entities = list()
