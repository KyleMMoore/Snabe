import pygame
from snabe import Snabe

class Sword():
    def __init__(self, screen, snabe):
        self.screen = screen
        self.snabe = snabe

        self.sword_sprite = pygame.image.load("Images/items/sword.bmp")
        self.rect = self.sword_sprite.get_rect()

        self.rect.centerx = 0
        self.rect.centery = 0

    def blitme(self):
        self.screen.blit(self.sword_sprite, self.rect)