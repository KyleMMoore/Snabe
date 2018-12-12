import pygame
from global_toolbox import GlobalSettings

class Body():
    def __init__(self, screen, head, global_vars, segment_number):
        # Useful game elements
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.snabings = GlobalSettings()
        self.gv = global_vars

        # Info and stats
        self.speed = head.speed
        self.head = head
        self.segment_number = segment_number
        self.is_last_segment = self.segment_number == self.head.score

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

        # Keeps track of player's last location
        # Given a real value when drawSegment is called for the first time
        self.lastLoc = (0, 0)
        # Keeps track of player's last direction of movement
        self.lastDirection = ""

        # Chooses the segment sprite and creates a rect
        self.drawSegment()

        # Appropriately connects this segment to the previous
        self.connect()

        # Float values for centers, allows us to do math easily
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # Stores segment in the global list
        self.gv.entities.append(self)

    ######################
    # Core functionality #
    ######################
    def update(self):
        self.move()

        # update the center values that the rect holds with the newly modified float versions
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
        self.lastLoc = (self.rect.centerx, self.rect.centery)

        # Keeps the lastDirection field and sprite up to date
        if not self.head.stunned:
            self.lastDirection = self.get_direction()
            self.drawSegment()
        # Prevents the head from moving slightly away from the body while stunned
        else:
            self.connect()

        # If segment is on a turning point, turn
        if self.lastLoc in self.head.turns:
            self.turn(self.head.turns[self.lastLoc])

    # Draws segment on-screen
    def blitme(self):
        self.screen.blit(self.segment_sprite, self.rect)

    # Chooses appropriate sprite based on direction, turning status, and segment number
    def drawSegment(self):
        sprite_path = "images/"
        if self.head.player_num == 1:
            sprite_path += "green/"
        else:
            sprite_path += "blue/"

        if self.is_last_segment:
            if self.moving_down:
                sprite_path += "SnabeTailDT.png"
            elif self.moving_left:
                sprite_path += "SnabeTailLT.png"
            elif self.moving_right:
                sprite_path += "SnabeTailRT.png"
            else:
                sprite_path += "SnabeTail.png"

        elif self.lastLoc in self.head.turns:
            new_direction = self.head.turns[self.lastLoc]
            if self.moving_up:
                if new_direction == "LEFT":
                    sprite_path += "SnabeTurnRD.png"
                elif new_direction == "RIGHT":
                    sprite_path += "SnabeTurnLD.png"
            elif self.moving_down:
                if new_direction == "LEFT":
                    sprite_path += "SnabeTurnRU.png"
                elif new_direction == "RIGHT":
                    sprite_path += "SnabeTurnLU.png"
            elif self.moving_left:
                if new_direction == "UP":
                    sprite_path += "SnabeTurnLU.png"
                elif new_direction == "DOWN":
                    sprite_path += "SnabeTurnLD.png"
            elif self.moving_right:
                if new_direction == "UP":
                    sprite_path += "SnabeTurnRU.png"
                elif new_direction == "DOWN":
                    sprite_path += "SnabeTurnRD.png"

        else:
            if self.moving_left or self.moving_right:
                sprite_path += "SnabeBodyTurned.png"
            else:
                sprite_path += "SnabeBody.png"

        try:
            self.segment_sprite = pygame.image.load(sprite_path)
        except:
            print("Error loading sprite at '" + sprite_path + "': falling back on dummy.bmp")
            self.segment_sprite = pygame.image.load("images/dummy.bmp")
        finally:
            self.rect = self.segment_sprite.get_rect(center=self.lastLoc)

    # Removes segment from global list, head list, and screen
    def destroy(self):
        self.gv.entities.remove(self)
        self.head.segments.remove(self)
        self.rect.centerx = self.rect.centery = -1
        self.blitme()

    # Allows segment to be printed to console
    # Prints type, last location, and global index number
    def __repr__(self):
        return str(type(self)) + ": " + str(self.lastLoc) + ": " + str(self.gv.entities.index(self))

    #############################
    # Movement/positioning code #
    #############################
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

    # If current location is a turning location, change directions
    # Last segment removes the turning point from the list
    # This keeps the list of turns from getting huge and causing problems
    def turn(self, new_direction):
        self.set_direction(new_direction)
        if self.is_last_segment:
            del self.head.turns[(self.centerx, self.centery)]

    def set_direction(self, new_direction):
        self.moving_up = new_direction == "UP"
        self.moving_down = new_direction == "DOWN"
        self.moving_left = new_direction == "LEFT"
        self.moving_right = new_direction == "RIGHT"

    def get_direction(self):
        if self.moving_up:
            return "UP"
        if self.moving_down:
            return "DOWN"
        if self.moving_left:
            return "LEFT"
        if self.moving_right:
            return "RIGHT"

    # Connects sprite to its previous segment
    # Based on direction, sets one side of self to adjacent side of previous segment
    # Also ensures center stays aligned
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









