import pygame
from random import randint
from settings import Settings
class Food():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.food_sprite = pygame.image.load("images/items/food.bmp")
        self.rect = self.food_sprite.get_rect()

        self.rect.centerx = randint(0, Settings().screen_width)#self.screen_rect.centerx
        self.rect.centery = randint(0, Settings().screen_height)#self.screen_rect.centery
        self.isEaten = False

    def feed(self):
        self.blitme()
    def blitme(self):
        self.screen.blit(self.food_sprite, self.rect)
