import pygame
import sys


class Timer():
    def __init__(self, screen, time_left):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.time = time_left

        self.timer_body = pygame.image.load("images/timer/timerBody.bmp")
        self.rect = self.timer_body.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top

        self.left_digit = pygame.image.load("images/timer/timer_0.bmp")
        self.left_digit_rect = self.left_digit.get_rect()

        self.left_digit_rect.centerx = self.screen_rect.centerx - 15
        self.left_digit_rect.top = self.screen_rect.top + 32

        self.right_digit = pygame.image.load("images/timer/timer_0.bmp")
        self.right_digit_rect = self.right_digit.get_rect()

        self.right_digit_rect.centerx = self.screen_rect.centerx + 15
        self.right_digit_rect.top = self.screen_rect.top + 32

    def tick(self):
        if len(str(self.time)) == 1:
            lt_digit = "0"
            rt_digit = str(self.time)[0]
        else:
            lt_digit = str(self.time)[0]
            rt_digit = str(self.time)[1]

        self.left_digit = pygame.image.load(self.switch(int(lt_digit)))
        self.right_digit = pygame.image.load(self.switch(int(rt_digit)))
        if self.time > 0:
            self.time -= 1

    def switch(self, arg):
        switchDict = {
            0: "images/timer/timer_0.bmp",
            1: "images/timer/timer_1.bmp",
            2: "images/timer/timer_2.bmp",
            3: "images/timer/timer_3.bmp",
            4: "images/timer/timer_4.bmp",
            5: "images/timer/timer_5.bmp",
            6: "images/timer/timer_6.bmp",
            7: "images/timer/timer_7.bmp",
            8: "images/timer/timer_8.bmp",
            9: "images/timer/timer_9.bmp",
        }
        return switchDict.get(arg, lambda: "images/timer/timer_0.bmp")

    def blitme(self):
        self.screen.blit(self.timer_body, self.rect)
        self.screen.blit(self.left_digit, self.left_digit_rect)
        self.screen.blit(self.right_digit, self.right_digit_rect)