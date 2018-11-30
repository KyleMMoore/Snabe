import pygame

class Food():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.food_sprite = pygame.image.load("images/items/food.bmp")
        self.rect = self.food_sprite.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.isEaten = False

    def blitme(self):
        self.screen.blit(self.food_sprite, self.rect)
