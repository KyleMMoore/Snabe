import pygame
from random import randint
from global_toolbox import GlobalSettings


class Wafer():

    def __init__(self, screen, global_vars):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.snabings = GlobalSettings()
        self.gv = global_vars

        # default power-up state
        self.power_type = "NONE"
        # assigns power-up state
        self.set_type()

        # Attempts to load wafer image
        try:
            self.food_sprite = pygame.image.load("images/items/wafer.png")
        except:
            print("Failed to load wafer sprite. Falling back on dummy.bmp")
            self.food_sprite = pygame.image.load("images/dummy.bmp")
        finally:
            self.rect = self.food_sprite.get_rect()

        self.chooseLocation()
        self.gv.entities.append(self)

    def set_type(self):
        switch = {
            0: "SWORD",
            1: "SHIELD",
        }
        roll = randint(1,100)

        if roll <= self.snabings.shield_rate:
            self.power_type = switch.get(1)
        elif roll > self.snabings.shield_rate:
            self.power_type= switch.get(0)

    def get_type(self):
        return self.power_type

    def chooseLocation(self):
        self.rect.centerx = randint(0, self.snabings.screen_width)
        self.rect.centery = randint(self.snabings.play_area_height+10, self.snabings.screen_height)

    def setLocation(self, x, y):
        self.rect.centerx = x
        self.rect.centery = y

    # returns a tuple containing the (x, y) of the rect
    def getLocation(self):
        return ((self.rect.centerx, self.rect.centery))

    def blitme(self):
        self.screen.blit(self.food_sprite, self.rect)

    def destroy(self):
        self.gv.wafer_list.remove(self)
        self.gv.entities.remove(self)
        del self

    def __repr__(self):
        return str(type(self)) + ": " + str(self.getLocation()) + ": " + str(self.gv.entities.index(self))