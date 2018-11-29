import pygame
from snabe import Snabe

class Body(Snabe):
    def __init__(self, screen, settings, player_num):
        self.screen = screen
        self.settings = settings
        self.player_num = player_num
        self.speed = settings.base_speed
