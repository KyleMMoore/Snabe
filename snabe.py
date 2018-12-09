import pygame
from body import Body
from food import Food
from wafer import Wafer

class Snabe():
    def __init__(self, screen, snabings, player_num):
        self.screen = screen
        self.snabings = snabings
        self.player_num = player_num
        self.speed = snabings.base_speed
        self.score = 5  # all players will start with base score of 5
        self.turns = dict()
        
        self.power_start_time = -1

        # movement flags
        # only one flag should be "True" at a time: this keeps movement locked to a grid
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

        # Flipped to True when sword powerup is active
        self.canDamage = False
        # Flipped to False while shield powerup is active
        self.isVulnerable = True
        # Flipped to True while canDamage = False and player is colliding with opponent
        self.stunned = False

        self.head_sprite = pygame.image.load("images/dummy.bmp")
        self.rect = self.head_sprite.get_rect()

        self.screen_rect = screen.get_rect()

        # set locations: both will be in the same y plane, but x plane will depend on player_num
        if self.player_num == 1:
            self.rect.centerx = 100
        else:
            self.rect.centerx = self.screen_rect.right - 100
        self.rect.bottom = self.screen_rect.centery

        # float values for centers, allows us to do math easily
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # help track the head
        self.lastLoc = (self.rect.centerx, self.rect.centery)
        self.lastDirection = "NONE"

        self.drawSnabe()

        # Add head to the global entity list
        self.snabings.entities.append(self)

        # a list to keep track of body segments
        self.segments = list()
        for x in range(self.score + 1):
            self.segments.append(Body(self.screen, self.snabings, self, x))

    def update(self):
        self.move()

        # update the center values that the rect holds with the newly modified float versions
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

        self.lastLoc = (self.rect.centerx, self.rect.centery)
        self.lastDirection = self.get_direction()

        self.drawSnabe()

        self.check_powerups()
        self.check_collisions()

        for x in self.segments:
            x.update()

    def move(self):
        if self.stunned:
            pass

        # snabe moves in the direction that the flags indicate
        elif self.rect.top > 0 and self.rect.bottom < self.screen_rect.bottom and self.rect.left > 0 \
                and self.rect.right < self.screen_rect.right:
            if self.moving_up:
                self.centery -= self.speed
            if self.moving_down:
                self.centery += self.speed
            if self.moving_left:
                self.centerx -= self.speed
            if self.moving_right:
                self.centerx += self.speed

        else:
            self.collision("WALL")

    def check_collisions(self):
        colliding_entity = self.rect.collidelist([x.rect for x in self.snabings.entities])
        if self.snabings.entities[colliding_entity] is self:
            self.stunned = False
            self.set_direction(self.lastDirection)
        else:
            print(colliding_entity)
            self.collision(self.snabings.entities[colliding_entity])

    def blitme(self):
        # draws snabe head at its current location
        self.screen.blit(self.head_sprite, self.rect)
        for x in self.segments:
            x.screen.blit(x.segment_sprite, x.rect)

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

    def is_moving(self):
        return not self.stunned

    def get_direction(self):
        if self.moving_up:
            return "UP"
        if self.moving_down:
            return "DOWN"
        if self.moving_left:
            return "LEFT"
        if self.moving_right:
            return "RIGHT"

    def set_direction(self, new_direction):
        self.moving_up = new_direction == "UP"
        self.moving_down = new_direction == "DOWN"
        self.moving_left = new_direction == "LEFT"
        self.moving_right = new_direction == "RIGHT"

    def collision(self, target):
        # If player collides with another Snabe head
        if type(target) is Snabe:
            pass

        # If player collides with a food pellet
        elif type(target) is Food:
            self.augment_score(1)
            target.destroy()

        # If player collides with a powerup wafer
        elif type(target) is Wafer:
            self.do_powerup(target.get_type())
            target.destroy()

        # If player collides with a body segment
        elif type(target) is Body:
            if target in self.segments and target.segment_number != 0:
                if self.moving_up and target.centery < self.centery:
                    self.reduce_score(self.score - target.segment_number)
                elif self.moving_down and target.centery > self.centery:
                    self.reduce_score(self.score - target.segment_number)
                elif self.moving_left and target.centerx < self.centerx:
                    self.reduce_score(self.score - target.segment_number)
                elif self.moving_right and target.centerx > self.centerx:
                    self.reduce_score(self.score - target.segment_number)

            elif target.head != self:
                if self.canDamage and target.head.isVulnerable:
                    target.head.reduce_score(target.head.score - target.segment_number)
                else:
                    self.stunned = True

        # If player collides with screen boundaries
        elif target == "WALL":
            # Sets user score to 2
            self.reduce_score(self.score - 2)

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

        # This occurs when no collision is detected
        # Required to restart movement when an invulnerable enemy finishes moving past
        else:
            self.stunned = False
            self.set_direction(self.lastDirection)
            for x in self.segments:
                x.set_direction(x.lastDirection)

    def augment_score(self, amount):
        self.score += amount
        for x in range(amount):
            self.segments.append(Body(self.screen, self.snabings, self, self.score - amount + x + 1))

    def reduce_score(self, amount):
        self.score -= amount
        for x in range(amount):
            self.segments[-1].destroy()

    def stun(self):
        self.stunned = True

    def do_powerup(self, type):
        self.power_start_time = self.snabings.timer_value
        if type == "SWORD":
            self.canDamage = True
        if type == "SHIELD":
            self.isVulnerable = False

    def check_powerups(self):
        if self.canDamage:
            if self.snabings.timer_value == self.power_start_time - self.snabings.sword_time:
                self.canDamage = False
        if not self.isVulnerable:
            if self.snabings.timer_value == self.power_start_time - self.snabings.shield_time:
                self.isVulnerable = True

    def first_move(self):
        return self.moving_down == self.moving_up == self.moving_left == self.moving_right == self.stunned
