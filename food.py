import pygame
from random import randint

class Food():
    def __init__(self, screen, snabings):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.snabings = snabings
        
        try:
            self.food_sprite = pygame.image.load("images/items/food.bmp")
        except:
            print("Failed to load food sprite: falling back on dummy.bmp")
            self.food_sprite = pygame.image.load("images/dummy.bmp")
        finally:
            self.rect = self.food_sprite.get_rect()

        self.chooseLocation()
        self.snabings.entities.append(self)
        self.snabings.entities_rects.append(self.rect)

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
        self.snabings.food_list.remove(self)
        self.snabings.entities.remove(self)
        self.snabings.entities_rects.remove(self.rect)