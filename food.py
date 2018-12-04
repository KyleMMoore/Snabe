import pygame
from random import randint

class Food():
    def __init__(self, screen, snabings, entities, entities_rects):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.entities = entities
        self.entities_rects = entities_rects
        self.snabings = snabings
        try:
            self.food_sprite = pygame.image.load("images/items/food.bmp")
        except:
            print("Failed to load food sprite: falling back on dummy.bmp")
            self.food_sprite = pygame.image.load("images/dummy.bmp")
        finally:
            self.rect = self.food_sprite.get_rect()

        self.assignLocation()
        self.entities.append(self)
        self.entities_rects.append(self.rect)

    def blitme(self):
        self.screen.blit(self.food_sprite, self.rect)

    def assignLocation(self):
        self.rect.centerx = randint(0, self.snabings.screen_width)
        self.rect.centery = randint(self.snabings.screen_height//8, self.snabings.screen_height)

    def destroy(self):
        self.snabings.food_list.remove(self)
        self.entities.remove(self)
        self.entities_rects.remove(self.rect)