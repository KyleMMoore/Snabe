import pygame
#from snabe import Snabe


class Body():
    def __init__(self, screen, settings, head, segment_number):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = settings
        self.speed = settings.base_speed
        self.turning_point_x = -1
        self.turning_point_y = -1
        self.new_direction = ""

        # store previous segment for future reference
        if segment_number == 0:
            self.previous_segment = head
        else:
            self.previous_segment = head.segments[segment_number - 1]

        # if this segment is the end piece, give it the end sprite
        if segment_number == head.score:
            if head.player_num == 1:
                self.segment_sprite = pygame.image.load("images/green/greenSnabeTail.bmp")
            elif head.player_num == 2:
                self.segment_sprite = pygame.image.load("images/blue/blueSnabeTail.bmp")

        # otherwise give it a body sprite
        else:
            if head.player_num == 1:
                self.segment_sprite = pygame.image.load("images/green/greenSnabeBody.bmp")
            elif head.player_num == 2:
                self.segment_sprite = pygame.image.load("images/blue/blueSnabeBody.bmp")

        self.segment_rect = self.segment_sprite.get_rect()

        if self.previous_segment == head:
            self.segment_rect.top = self.previous_segment.head_rect.bottom
            self.segment_rect.centerx = self.previous_segment.head_rect.centerx
        else:
            self.segment_rect.top = self.previous_segment.segment_rect.bottom
            self.segment_rect.centerx = self.previous_segment.segment_rect.centerx

        # float values for centers, allows us to do math easily
        self.centerx = float(self.segment_rect.centerx)
        self.centery = float(self.segment_rect.centery)

        # movement flags
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def move(self):
        # snabe moves in the direction that the flags indicate
        if self.moving_up and self.segment_rect.top > 0:
            self.centery -= self.speed
        if self.moving_down and self.segment_rect.bottom < self.screen_rect.bottom:
            self.centery += self.speed
        if self.moving_left and self.segment_rect.left > 0:
            self.centerx -= self.speed
        if self.moving_right and self.segment_rect.right < self.screen_rect.right:
            self.centerx += self.speed

        # update the center values that the rect holds with the newly modified float versions
        self.segment_rect.centerx = self.centerx
        self.segment_rect.centery = self.centery

    def set_turning_point(self, direction, x_pos, y_pos):
        self.turning_point_x = x_pos
        self.turning_point_y = y_pos
        self.new_direction = direction

    def turn(self):
        if self.segment_rect.centerx == self.turning_point_x and self.segment_rect.centery == self.turning_point_y:
            if self.new_direction == "UP":
                self.moving_up = True
                self.moving_down = False
                self.moving_left = False
                self.moving_right = False

            if self.new_direction == "DOWN":
                self.moving_up = False
                self.moving_down = True
                self.moving_left = False
                self.moving_right = False

            if self.new_direction == "LEFT":
                self.moving_up = False
                self.moving_down = False
                self.moving_left = True
                self.moving_right = False

            if self.new_direction == "RIGHT":
                self.moving_up = False
                self.moving_down = False
                self.moving_left = False
                self.moving_right = True

            self.turning_point_x = -1
            self.turning_point_y = -1




