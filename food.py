import pygame

class Food():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.food_sprite = pygame.image.load("images/items/food.bmp")
        self.rect = self.food_sprite.get_rect()

        self.rect.centerx = 400
        self.rect.centery = 400

    def blitme(self):
        self.screen.blit(self.food_sprite,self.rect)