import pygame
from food import Food

class Wafer(Food):

    def __init__(self, screen, entities, entities_rects):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.entities = entities
        self.entities_rects = entities_rects
        try:
            self.food_sprite = pygame.image.load("images/items/wafer.bmp")
        except:
            print("Failed to load wafer sprite. Falling back on dummy.bmp")
            self.food_sprite = pygame.image.load("images/dummy.bmp")
        finally:
            self.rect = self.food_sprite.get_rect()

        self.assignLocation()
        self.entities.append(self)
        self.entities_rects.append(self.rect)

    def get_type(self):
        pass