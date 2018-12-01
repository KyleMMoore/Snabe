import pygame
from random import randint
from settings import Settings
class Food():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.food_sprite = pygame.image.load("images/items/food.bmp")
        self.rect = self.food_sprite.get_rect()

        self.assignLocation()
        self.isEaten = False

    def blitme(self):
        self.screen.blit(self.food_sprite, self.rect)

    def assignLocation(self):
        self.rect.centerx = randint(0, Settings().screen_width)
        self.rect.centery = randint(Settings().screen_height//8, Settings().screen_height)
