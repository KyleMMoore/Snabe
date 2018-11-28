import pygame
from settings import Settings

class Snabe():
    def __init__(self, screen, settings, player_num):
        self.screen = screen
        self.settings = settings
        self.player_num = player_num
        self.speed = settings.base_speed

        # load head sprite, get rect
        self.head_sprite = pygame.image.load("images/head.bmp")
        self.head_rect = self.head_sprite.get_rect()
        self.screen_rect = screen.get_rect()

        # set locations: both will be in the same y plane, but x plane will depend on player_num
        if player_num == 1:
            self.head_rect.centerx = 100
        else:
            self.head_rect.centerx = 700
        self.head_rect.bottom = self.screen_rect.centery

        # float values for centers, allows us to do math easily
        self.centerx = float(self.head_rect.centerx)
        self.centery = float(self.head_rect.centery)

        # movement flags
        # only one flag should be "True" at a time: this keeps movement locked to a grid
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def move(self):
        # snabe moves in the direction that the flags indicate
        if self.moving_up and self.head_rect.top > 0:
            self.centery -= self.speed
        if self.moving_down and self.head_rect.bottom < self.screen_rect.bottom:
            self.centery += self.speed
        if self.moving_left and self.head_rect.left > 0:
            self.centerx -= self.speed
        if self.moving_right and self.head_rect.right < self.screen_rect.right:
            self.centerx += self.speed

        # update the center values that the rect holds with the newly modified float versions
        self.head_rect.centerx = self.centerx
        self.head_rect.centery = self.centery

    def blitme(self):
        # draws snabe head at its current location
        self.screen.blit(self.head_sprite, self.head_rect)
