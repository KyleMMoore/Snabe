import pygame


class Body():
    def __init__(self, screen, settings, head, segment_number):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = settings
        self.speed = settings.base_speed
        self.head = head
        self.segment_number = segment_number
        self.is_last_segment = self.segment_number == self.head.score

        # store previous segment for future reference
        if self.segment_number == 0:
            self.previous_segment = head
        else:
            self.previous_segment = head.segments[segment_number - 1]

        # if this segment is the end piece, give it the end sprite
        if self.segment_number == head.score:
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

        self.rect = self.segment_sprite.get_rect()

        self.rect.top = self.previous_segment.rect.bottom
        self.rect.centerx = self.previous_segment.rect.centerx

        # float values for centers, allows us to do math easily
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.lastLoc = (self.centerx, self.centery)

        # movement flags
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def move(self):
        if self.head.is_moving():
            if self.moving_up:
                self.centery -= self.speed
            if self.moving_down:
                self.centery += self.speed
            if self.moving_left:
                self.centerx -= self.speed
            if self.moving_right:
                self.centerx += self.speed
        else:
            self.moving_up = self.moving_down = self.moving_left = self.moving_right = False

        # update the center values that the rect holds with the newly modified float versions
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

        if (self.centerx, self.centery) in self.head.turning_points:
            self.turn(self.previous_segment.get_direction())

        self.drawSegment()

    def drawSegment(self):
        if self.head.player_num == 1:
            if self.moving_up or self.moving_down:
                if self.is_last_segment:
                    if self.moving_up:
                        self.segment_sprite = pygame.image.load("images/green/greenSnabeTail.bmp")
                    else:
                        self.segment_sprite = pygame.image.load("images/green/greenSnabeTailDT.bmp")
                    self.rect = self.segment_sprite.get_rect(center=(self.previous_segment.rect.centerx, self.centery))
                else:
                    self.segment_sprite = pygame.image.load("images/green/greenSnabeBody.bmp")
            if self.moving_left or self.moving_right:
                if self.is_last_segment:
                    if self.moving_left:
                        self.segment_sprite = pygame.image.load("images/green/greenSnabeTailLT.bmp")
                    else:
                        self.segment_sprite = pygame.image.load("images/green/greenSnabeTailRT.bmp")
                    self.rect = self.segment_sprite.get_rect(center=(self.centerx, self.previous_segment.rect.centery))
                else:
                    self.segment_sprite = pygame.image.load("images/green/greenSnabeBodyTurned.bmp")
        else:
            if self.moving_up or self.moving_down:
                if self.is_last_segment:
                    if self.moving_up:
                        self.segment_sprite = pygame.image.load("images/blue/blueSnabeTail.bmp")
                    else:
                        self.segment_sprite = pygame.image.load("images/blue/blueSnabeTailDT.bmp")
                    self.rect = self.segment_sprite.get_rect(center=(self.previous_segment.rect.centerx, self.centery))
                else:
                    self.segment_sprite = pygame.image.load("images/blue/blueSnabeBody.bmp")
            if self.moving_left or self.moving_right:
                if self.is_last_segment:
                    if self.moving_left:
                        self.segment_sprite = pygame.image.load("images/blue/blueSnabeTailLT.bmp")
                    else:
                        self.segment_sprite = pygame.image.load("images/blue/blueSnabeTailRT.bmp")
                    self.rect = self.segment_sprite.get_rect(center=(self.centerx, self.previous_segment.rect.centery))
                else:
                    self.segment_sprite = pygame.image.load("images/blue/blueSnabeBodyTurned.bmp")

    def turn(self, new_direction):
        if new_direction == "UP":
            self.moving_up = True
            self.moving_down = False
            self.moving_left = False
            self.moving_right = False

        if new_direction == "DOWN":
            self.moving_up = False
            self.moving_down = True
            self.moving_left = False
            self.moving_right = False

        if new_direction == "LEFT":
            self.moving_up = False
            self.moving_down = False
            self.moving_left = True
            self.moving_right = False

        if new_direction == "RIGHT":
            self.moving_up = False
            self.moving_down = False
            self.moving_left = False
            self.moving_right = True

        if self.is_last_segment:
            self.head.turning_points.remove((self.centerx, self.centery))

    def get_direction(self):
        if self.moving_up:
            return "UP"
        if self.moving_down:
            return "DOWN"
        if self.moving_left:
            return "LEFT"
        if self.moving_right:
            return "RIGHT"









