import pygame
from body import Body
from food import Food
from wafer import Wafer
from global_toolbox import GlobalSettings

class Snabe():
    def __init__(self, screen, global_vars, player_num):
        # Useful game elements
        self.screen = screen
        self.snabings = GlobalSettings()
        self.gv = global_vars
        # Allows us to calculate locations based on the screen edges
        self.screen_rect = screen.get_rect()

        # Adjust screen rect to encompass only the playable area
        self.screen_rect.height = self.snabings.screen_height - self.snabings.play_area_height
        self.screen_rect.top = self.snabings.play_area_height
        self.screen_rect.bottom = self.snabings.screen_height

        #Info and stats
        self.player_num = player_num
        self.speed = self.snabings.base_speed
        self.score = 5  # all players will start with base score of 5

        # Flipped to True when sword powerup is active
        self.canDamage = False
        # Flipped to False while shield powerup is active
        self.isVulnerable = True
        # Flipped to True while canDamage = False and player is colliding with opponent
        self.stunned = False

        # Used when a powerup is activated, stores the time at which it is picked up
        self.power_start_time = -1

        # movement flags
        # only one flag should be "True" at a time: this keeps movement locked to a grid
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

        # Keeps track of turning points
        self.turns = dict()

        # Proper sprite and rect are assigned at first call of drawSprite
        # This merely creates the fields for later use
        self.head_sprite = pygame.image.load("images/dummy.bmp")
        self.rect = self.head_sprite.get_rect()

        # Sets initial locations
        # Both will be in the same y plane, but x plane will depend on player_num
        if self.player_num == 1:
            self.rect.centerx = 100
        else:
            self.rect.centerx = self.screen_rect.right - 100
        self.rect.bottom = self.screen_rect.centery

        # Float values for centers, allows us to do math easily
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # Values that help keep track of the head
        # Useful when recovering from a stun
        self.lastLoc = (self.rect.centerx, self.rect.centery)
        self.lastDirection = "UP"

        # Picks the correct sprite for the snabe and creates the rect
        self.drawSnabe()

        # Add head to the global entity list
        self.gv.entities.append(self)

        # Creates a list to keep track of body segments
        self.segments = list()
        # Creates one extra, so the tail is always present
        for x in range(self.score + 1):
            self.segments.append(Body(self.screen, self, self.gv, x))

    ######################
    # Core functionality #
    ######################
    def update(self):
        self.move()

        # Updates the center values that the rect matches the float versions
        # We do this because "move()" modifies the float versions
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

        # Updates the position tracking fields
        self.lastLoc = (self.rect.centerx, self.rect.centery)
        self.lastDirection = self.get_direction()

        # Select the proper sprite after movement
        # Allows for new sprites when turns occur
        self.drawSnabe()

        # Check for special events
        self.check_powerups()
        self.check_collisions()

        # Update all segments once the head is taken care of
        for x in self.segments:
            x.update()

    # Draws the head at its current location
    def blitme(self):
        self.screen.blit(self.head_sprite, self.rect)

    # Picks the appropriate sprite based on
    # player_num, current direction, and active powerups
    def drawSnabe(self):
        sprite_path = "images/"
        if self.player_num == 1:
            sprite_path += "green/"
        else:
            sprite_path += "blue/"

        if self.canDamage:
            sprite_path += "headSword"
        elif not self.isVulnerable:
            sprite_path += "headShield"
        else:
            sprite_path += "head"

        if self.moving_down:
            sprite_path += "DT.png"
        elif self.moving_left:
            sprite_path += "LT.png"
        elif self.moving_right:
            sprite_path += "RT.png"
        else:
            sprite_path += ".png"

        try:
            self.head_sprite = pygame.image.load(sprite_path)
        except:
            print("Failed to load head sprite for player " + str(self.player_num))
            print("Falling back on dummy.bmp")
            self.head_sprite = pygame.image.load("images/dummy.bmp")
        finally:
            self.rect = self.head_sprite.get_rect(center=self.lastLoc)

    #################
    # Movement code #
    #################
    def move(self):
        if self.stunned:
            pass

        # snabe moves in the direction that the flags indicate
        elif self.rect.top > self.screen_rect.top \
                and self.rect.bottom < self.screen_rect.bottom \
                and self.rect.left > self.screen_rect.left \
                and self.rect.right < self.screen_rect.right:
            if self.moving_up:
                self.centery -= self.speed
            if self.moving_down:
                self.centery += self.speed
            if self.moving_left:
                self.centerx -= self.speed
            if self.moving_right:
                self.centerx += self.speed

        # Triggered when head reaches the edges of the screen
        else:
            self.collision("WALL")

    # Collisions with walls and no-damage head-on collisions with the opponent call this
    # Causes player to move in a new direction based on location and current direction of movement
    def bounce_off(self):
        if self.moving_up or self.moving_down:
            if self.rect.centerx > self.snabings.screen_width / 2:
                self.set_direction("LEFT")
            elif self.rect.centerx <= self.snabings.screen_width / 2:
                self.set_direction("RIGHT")

        else:
            if self.rect.centery > self.snabings.screen_height / 2:
                self.set_direction("UP")
            elif self.rect.centery <= self.snabings.screen_height / 2:
                self.set_direction("DOWN")

        self.lastLoc = (self.rect.centerx, self.rect.centery)
        self.turns[self.lastLoc] = self.get_direction()

    # Sets the current direction to the value specified
    # If the new direction does not match the old,
    # adds the location and new direction to the turns dict
    def set_direction(self, new_direction):
        fm = self.first_move()

        self.moving_up = new_direction == "UP"
        self.moving_down = new_direction == "DOWN"
        self.moving_left = new_direction == "LEFT"
        self.moving_right = new_direction == "RIGHT"

        if new_direction != self.lastDirection and not (new_direction == "UP" and fm):
            self.turns[self.lastLoc] = new_direction

    ####################
    # Check for events #
    ####################
    def check_collisions(self):
        # Locally recreates list of entities without self and first segment
        entities = list()
        for x in self.gv.entities:
            if x != self and x != self.segments[0]:
                entities.append(x)

        # Stores the index of the entity that is being collided with in the local list
        # collidelist works with a list of rects, so a list comp is used to get said list
        colliding_entity = self.rect.collidelist([x.rect for x in entities])

        # To make sure snabe restarts after a no damage collision with the opponent,
        # we have to make sure the stun flag is always false and the direction is always set
        # when a collision is not occuring
        if colliding_entity == -1:
            self.stunned = False
            self.set_direction(self.lastDirection)
        else:
            self.collision(entities[colliding_entity])

    # Checks to see if powerups have expired yet
    # Toggles flags to false when their durations have passed
    def check_powerups(self):
        if self.canDamage:
            if self.gv.timer_value == self.power_start_time - self.snabings.sword_time:
                self.canDamage = False
        if not self.isVulnerable:
            if self.gv.timer_value == self.power_start_time - self.snabings.shield_time:
                self.isVulnerable = True

    ######################################
    # Request information from the snabe #
    ######################################
    def is_moving(self):
        return not self.stunned

    # Returns the current direction as an all caps string
    def get_direction(self):
        if self.moving_up:
            return "UP"
        if self.moving_down:
            return "DOWN"
        if self.moving_left:
            return "LEFT"
        if self.moving_right:
            return "RIGHT"

    # Returns True if the player has not started moving yet
    def first_move(self):
        return self.moving_down == self.moving_up == self.moving_left == self.moving_right == self.stunned

    # Returns True if snabe collides with the enemy head on
    def head_on(self, enemy):
        return (self.moving_up and enemy.moving_down)\
                or (self.moving_left and enemy.moving_right)\
                or (self.moving_down and enemy.moving_up)\
                or (self.moving_right and enemy.moving_left)

    #########################
    # Handle special events #
    #########################
    def collision(self, target):
        # If player collides with another Snabe head
        if type(target) is Snabe:
            if self.canDamage and target.isVulnerable:
                target -= target.score
            elif self.head_on(target):
                self.bounce_off()

        # If player collides with a food pellet
        elif type(target) is Food:
            self += 1
            target.destroy()

        # If player collides with a powerup wafer
        elif type(target) is Wafer:
            self.do_powerup(target.get_type())
            target.destroy()

        # If player collides with a body segment
        elif type(target) is Body:
            # If target is one of the player's own segments,
            # remove every segment from the target back
            if target in self.segments and target.segment_number != 0:
                if self.moving_up and target.centery < self.centery:
                    self -= self.score - target.segment_number
                elif self.moving_down and target.centery > self.centery:
                    self -= self.score - target.segment_number
                elif self.moving_left and target.centerx < self.centerx:
                    self -= self.score - target.segment_number
                elif self.moving_right and target.centerx > self.centerx:
                    self -= self.score - target.segment_number

            # If target is an enemy segment and damage is possible,
            # remove every segment from the target back
            # Otherwise, stop and wait until the enemy has passed
            elif target.head != self:
                if self.canDamage and target.head.isVulnerable:
                    target.head -= target.head.score - target.segment_number
                else:
                    self.stunned = True

        # If player collides with screen boundaries
        elif target == "WALL":
            # Sets user score to 2
            if self.isVulnerable:
                self -= self.score - 2
            self.bounce_off()

    # Sets stun to True, causing the snabe to stop moving
    def stun(self):
        self.stunned = True

    # Stores time of powerup activation and sets flags appropriately
    def do_powerup(self, type):
        self.power_start_time = self.gv.timer_value
        if type == "SWORD":
            self.canDamage = True
        if type == "SHIELD":
            self.isVulnerable = False

    #########################
    # Overloading operators #
    #########################

    # Allows for adding to the snabe length with the + operator
    # Creates a new segment for each point added, augments player score
    def __add__(self, amount):
        self.score += amount
        for x in range(amount):
            self.segments.append(Body(self.screen, self, self.gv, self.score - amount + x + 1))
        return self

    # Allows for reducing score with the - operator
    # Removes a segment from the end of the snabe for each point removed, decrements player score
    def __sub__(self, amount):
        self.score -= amount
        # Due to a strange positioning bug that refuses to go away,
        # the tail will only connect if we remove an extra segment and recreate it
        for x in range(amount + 1):
            self.segments[-1].destroy()
        self.segments.append(Body(self.screen, self, self.gv, self.score))
        return self

    # When snabe instance is printed, will return its type, last location,
    # and index in the global entity list
    def __repr__(self):
        return str(type(self)) + ": " + str(self.lastLoc) + ": " + str(self.gv.entities.index(self))

