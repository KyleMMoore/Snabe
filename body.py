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
        self.lastLoc = (0,0)
        self.entities = entities
        self.entities_rects = entities_rects

        # store previous segment for future reference
        if self.segment_number == 0:
            self.previous_segment = head
        else:
            self.previous_segment = head.segments[segment_number - 1]
            self.previous_segment.is_last_segment = False

        # movement flags
        self.moving_up = self.previous_segment.moving_up
        self.moving_down = self.previous_segment.moving_down
        self.moving_left = self.previous_segment.moving_left
        self.moving_right = self.previous_segment.moving_right

        self.drawSegment()

        # Appropriately connects this segment to the previous
        self.connect()

        # float values for centers, allows us to do math easily
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.lastLoc = (self.centerx, self.centery)

        # Stores segment and rect in the global lists
        self.entities.append(self)
        self.entities_rects.append(self.rect)

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
            self.lastLoc = (self.rect.centerx, self.rect.centery)
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
            if self.moving_down:
                sprite_path += "SnabeTailDT.bmp"
            elif self.moving_left:
                sprite_path += "SnabeTailLT.bmp"
            elif self.moving_right:
                sprite_path += "SnabeTailRT.bmp"
            else:
                sprite_path += "SnabeTail.bmp"

        elif self.lastLoc in self.head.turns:
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
            if self.moving_up or self.moving_down or not self.head.is_moving():
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

    def connect(self):
        if self.moving_down:
            self.rect.bottom = self.previous_segment.rect.top
            self.rect.centerx = self.previous_segment.rect.centerx
        elif self.moving_left:
            self.rect.left = self.previous_segment.rect.right
            self.rect.centery = self.previous_segment.rect.centery
        elif self.moving_right:
            self.rect.right = self.previous_segment.rect.left
            self.rect.centery = self.previous_segment.rect.centery
        else:
            self.rect.top = self.previous_segment.rect.bottom
            self.rect.centerx = self.previous_segment.rect.centerx
        self.lastLoc = (self.rect.centerx, self.rect.centery)

    def destroy(self):
        print(self.segment_number)
        pos = self.entities.index(self)
        self.entities_rects.pop(pos)
        self.entities.remove(self)
        self.head.segments.remove(self)
        self.previous_segment.is_last_segment = True
        self.rect.centerx = self.rect.centery = -1










