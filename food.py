import pygame
from random import randint
from settings import Settings
class Food():
    def __init__(self, screen, entities, entities_rects):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        try:
            self.food_sprite = pygame.image.load("images/items/food.bmp")
        except:
            print("Failed to load food sprite: falling back on dummy.bmp")
            self.food_sprite = pygame.image.load("images/dummy.bmp")
        finally:
            self.rect = self.food_sprite.get_rect()

        self.assignLocation()
        self.isEaten = False
        entities.append(self)
        entities_rects.append(self.rect)
    def blitme(self):
        self.screen.blit(self.food_sprite, self.rect)

    def assignLocation(self):
        self.rect.centerx = randint(0, Settings().screen_width)
        self.rect.centery = randint(Settings().screen_height//8, Settings().screen_height)

    def destroy(self):
        pass
