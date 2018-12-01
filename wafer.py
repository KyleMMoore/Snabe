import pygame
from food import Food

class Wafer(Food):

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.food_sprite = pygame.image.load("images/items/wafer.bmp")
        self.rect = self.food_sprite.get_rect()

        self.assignLocation()