import pygame
from body import Body
from food import Food
from wafer import Wafer


class Snabe():
    def __init__(self, screen, settings, entities, player_num):
        self.screen = screen
        self.settings = settings
        self.player_num = player_num
        self.speed = settings.base_speed
        self.score = 5  # all players will start with base score of 1
        self.turns = dict()
        self.entities = entities

        # Flipped to True when sword powerup is active
        self.canDamage = False
        # Flipped to False while shield powerup is active
        self.isVulnerable = True

        # load head sprite, get rect
        try:
            if self.player_num == 1:
                self.head_sprite = pygame.image.load("images/green/greenHead.bmp")
            elif self.player_num == 2:
                self.head_sprite = pygame.image.load("images/blue/blueHead.bmp")
        except:
            print("Failed to load head sprite for player " + self.player_num + ": falling back on dummy.bmp")
            self.head_sprite = pygame.image.load("images/dummy.bmp")
        finally:
            self.rect = self.head_sprite.get_rect()

        self.screen_rect = screen.get_rect()
        self.entities[self] = self.rect
        # set locations: both will be in the same y plane, but x plane will depend on player_num
        if self.player_num == 1:
            self.rect.centerx = 100
        else:
            self.rect.centerx = self.screen_rect.right - 100
        self.rect.bottom = self.screen_rect.centery

        # float values for centers, allows us to do math easily
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # movement flags
        # only one flag should be "True" at a time: this keeps movement locked to a grid
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

        # help track the head
        self.lastLoc = (self.centerx, self.centery)

        # a list to keep track of body segments
        self.segments = list()
        for x in range(self.score + 1):
            self.segments.append(Body(self.screen, self.settings, self, self.entities, x))

    def move(self):
        # snabe moves in the direction that the flags indicate
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.speed
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.speed

        # update the center values that the rect holds with the newly modified float versions
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

        self.drawSnabe()

        for x in self.segments:
            x.move()

        colliding_entity = self.rect.collidedict(self.entities)
        if colliding_entity != None:
            self.collision(colliding_entity[0])



    def blitme(self):
        # draws snabe head at its current location
        self.screen.blit(self.head_sprite, self.rect)
        for x in self.segments:
            x.screen.blit(x.segment_sprite, x.rect)

    def drawSnabe(self):
        if self.player_num == 1:
            if self.moving_up:
                self.head_sprite = pygame.image.load("images/green/greenHead.bmp")
            elif self.moving_down:
                self.head_sprite = pygame.image.load("images/green/greenHeadDW.bmp")
            elif self.moving_left:
                self.head_sprite = pygame.image.load("images/green/greenHeadLT.bmp")
            elif self.moving_right:
                self.head_sprite = pygame.image.load("images/green/greenHeadRT.bmp")
        elif self.player_num == 2:
            if self.moving_up:
                self.head_sprite = pygame.image.load("images/blue/blueHead.bmp")
            elif self.moving_down:
                self.head_sprite = pygame.image.load("images/blue/blueHeadDW.bmp")
            elif self.moving_left:
                self.head_sprite = pygame.image.load("images/blue/blueHeadLT.bmp")
            elif self.moving_right:
                self.head_sprite = pygame.image.load("images/blue/blueHeadRT.bmp")
        self.rect = self.head_sprite.get_rect(center=(self.centerx, self.centery))

    def is_moving(self):
        return self.moving_up or self.moving_down or self.moving_left or self.moving_right

    def get_last_turn(self):
        return self.turning_points[-1]

    def get_direction(self):
        if self.moving_up:
            return "UP"
        if self.moving_down:
            return "DOWN"
        if self.moving_left:
            return "LEFT"
        if self.moving_right:
            return "RIGHT"

    def collision(self, target):
        if type(target) is Snabe:
            if target.isVulnerable and self.canDamage:
                target.reduce_score(target.score)
            elif not target.isVulnerable:
                self.stun()
        elif type(target) is Food:
            self.augment_score(self, 1)
            self.entities.remove(target)
            target.destroy()
        elif type(target) is Wafer:
            self.do_powerup(type(target))
            target.destroy()
        elif type(target) is pygame.display:
            self.reduce_score(self.score - 2)
            if self.moving_up or self.moving_down:
                self.moving_up = self.moving_down = False
                self.moving_left = self.rect.centerx > self.settings.screen_width / 2
                self.moving_right = self.rect.centerx <= self.settings.screen_width / 2
                self.turns[self.lastLoc] = self.get_direction()
            else:
                self.moving_left = self.moving_right = False
                self.moving_up = self.rect.centery > self.settings.screen_height / 2
                self.moving_down = self.rect.centery <= self.settings.screen_height / 2
                self.turns[self.lastLoc] = self.get_direction()


    def augment_score(self, amount):
        for x in range(amount):
            self.segments.append(Body(self.screen, self.settings, self, self.entities, self.score + x))
        self.score += amount

    def reduce_score(self, amount):
        self.score -= amount
        for x in range(amount):
            self.segments.remove(self.segments[x])

    def stun(self):
        pass