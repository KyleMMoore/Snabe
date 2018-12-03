import pygame


class Body():
    def __init__(self, screen, settings, head, entities, entities_rects, segment_number):
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
        if self.is_last_segment:
            if self.head.player_num == 1:
                self.segment_sprite = pygame.image.load("images/green/SnabeTail.bmp")
            elif self.head.player_num == 2:
                self.segment_sprite = pygame.image.load("images/blue/SnabeTail.bmp")

        # otherwise give it a body sprite
        else:
            if self.head.player_num == 1:
                self.segment_sprite = pygame.image.load("images/green/SnabeBody.bmp")
            elif self.head.player_num == 2:
                self.segment_sprite = pygame.image.load("images/blue/SnabeBody.bmp")

        self.rect = self.segment_sprite.get_rect()

        self.rect.top = self.previous_segment.rect.bottom
        self.rect.centerx = self.previous_segment.rect.centerx

        # float values for centers, allows us to do math easily
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.lastLoc = (self.centerx, self.centery)

        # Stores segment and rect in the global dict
        entities[self] = self.rect
        # Stores segment location and rect in the global dict
        entities_rects[self.lastLoc] = self.rect

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

            # update the center values that the rect holds with the newly modified float versions
            self.rect.centerx = self.centerx
            self.rect.centery = self.centery
            self.lastLoc = (self.centerx, self.centery)
            self.drawSegment()
            if self.lastLoc in self.head.turns:
                self.turn(self.head.turns[self.lastLoc])
        else:
            self.moving_up = self.moving_down = self.moving_left = self.moving_right = False

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
            del self.head.turns[(self.centerx, self.centery)]

    def get_direction(self):
        if self.moving_up:
            return "UP"
        if self.moving_down:
            return "DOWN"
        if self.moving_left:
            return "LEFT"
        if self.moving_right:
            return "RIGHT"

    def drawSegment(self):
        sprite_path = "images/"
        if self.head.player_num == 1:
            sprite_path += "green/"
        else:
            sprite_path += "blue/"

        if self.is_last_segment:
            if self.moving_up:
                sprite_path += "SnabeTail.bmp"
            elif self.moving_down:
                sprite_path += "SnabeTailDT.bmp"
            elif self.moving_left:
                sprite_path += "SnabeTailLT.bmp"
            else:
                sprite_path += "SnabeTailRT.bmp"
        else:
            if self.lastLoc in self.head.turns:
                new_direction = self.head.turns[self.lastLoc]
                if self.moving_up:
                    if new_direction == "LEFT":
                        sprite_path += "SnabeTurnRD.bmp"
                    elif new_direction == "RIGHT":
                        sprite_path += "SnabeTurnLD.bmp"
                elif self.moving_down:
                    if new_direction == "LEFT":
                        sprite_path += "SnabeTurnRU.bmp"
                    elif new_direction == "RIGHT":
                        sprite_path += "SnabeTurnLU.bmp"
                elif self.moving_left:
                    if new_direction == "UP":
                        sprite_path += "SnabeTurnLU.bmp"
                    elif new_direction == "DOWN":
                        sprite_path += "SnabeTurnLD.bmp"
                elif self.moving_right:
                    if new_direction == "UP":
                        sprite_path += "SnabeTurnRU.bmp"
                    elif new_direction == "DOWN":
                        sprite_path += "SnabeTurnRD.bmp"
            else:
                if self.moving_up or self.moving_down:
                    sprite_path += "SnabeBody.bmp"
                else:
                    sprite_path += "SnabeBodyTurned.bmp"

        try:
            self.segment_sprite = pygame.image.load(sprite_path)
        except:
            print("Error loading sprite at '" + sprite_path + "': falling back on dummy.bmp")
            self.segment_sprite = pygame.image.load("images/dummy.bmp")
        finally:
            self.rect = self.segment_sprite.get_rect(center=self.lastLoc)











