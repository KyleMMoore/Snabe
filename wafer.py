import pygame
from random import randint

class Wafer():

    def __init__(self, screen, snabings, entities, entities_rects):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.entities = entities
        self.entities_rects = entities_rects
        self.snabings = snabings

        self.power_type = "NONE"
        self.set_type()
        try:
            self.food_sprite = pygame.image.load("images/items/wafer.bmp")
        except:
            print("Failed to load wafer sprite. Falling back on dummy.bmp")
            self.food_sprite = pygame.image.load("images/dummy.bmp")
        finally:
            self.rect = self.food_sprite.get_rect()

        self.chooseLocation()
        self.entities.append(self)
        self.entities_rects.append(self.rect)

    def set_type(self):
        switch = {
            0: "SWORD",
            1: "SHIELD",
        }
        self.power_type= switch.get(randint(0,1))

    def get_type(self):
        return self.power_type

    def chooseLocation(self):
        self.rect.centerx = randint(0, self.snabings.screen_width)
        self.rect.centery = randint(self.snabings.screen_height//8, self.snabings.screen_height)

    def setLocation(self, x, y):
        self.rect.centerx = x
        self.rect.centery = y

    # returns a tuple containing the (x, y) of the rect
    def getLocation(self):
        return ((self.rect.centerx, self.rect.centery))

    def blitme(self):
        self.screen.blit(self.food_sprite, self.rect)

    def destroy(self):
        print(self.get_type())
        self.snabings.wafer_list.remove(self)
        self.entities.remove(self)
        self.entities_rects.remove(self.rect)