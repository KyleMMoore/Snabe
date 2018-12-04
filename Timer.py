import pygame
import sys


class Timer():
    def __init__(self, screen, int):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        if int > 99:
            self.time = 99
        elif int <= 0:
            self.time = 1
        else:
            self.time = int\

        # load timer image and set rect
        try:
            self.timer_body = pygame.image.load("images/timer/timerBody.bmp")
        except:
            print("Failed to load timer body sprite. Falling back on dummy.bmp")
            self.timer_body = pygame.image.load("images/dummy.bmp")
        finally:
            self.rect = self.timer_body.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top

        # load image and rect for left digit
        try:
            self.left_digit = pygame.image.load("images/timer/timer_0.bmp")
        except:
            print("Failed to load timer left digit sprite. Falling back on dummy.bmp")
            self.left_digit = pygame.image.load("images/dummy.bmp")
        finally:
            self.left_digit_rect = self.left_digit.get_rect()

        # offset the digit to the left side of timer
        self.left_digit_rect.centerx = self.screen_rect.centerx - 15
        self.left_digit_rect.top = self.screen_rect.top + 32

        # load image and rect for right digit
        try:
            self.right_digit = pygame.image.load("images/timer/timer_0.bmp")
        except:
            print("Failed to load timer right digit sprite. Falling back on dummy.bmp")
            self.right_digit = pygame.image.load("images/dummy.bmp")
        finally:
            self.right_digit_rect = self.right_digit.get_rect()

        # offset the digit to the right side of timer
        self.right_digit_rect.centerx = self.screen_rect.centerx + 15
        self.right_digit_rect.top = self.screen_rect.top + 32

    # updates timer image to given time
    # converts int to image
    def tick(self):
        # if number is < 10
        # left digit is displayed as 0
        # stores left and right digits
        #  after converting to string
        if len(str(self.time)) == 1:
            lt_digit = "0"
            rt_digit = str(self.time)[0]
        else:
            lt_digit = str(self.time)[0]
            rt_digit = str(self.time)[1]

        # determines the correct image to load based on the digit
        try:
            self.left_digit = pygame.image.load(self.switch(int(lt_digit)))
        except:
            print("Failed to update timer left digit sprite. Falling back on dummy.bmp")
            self.left_digit = pygame.image.load("images/dummy.bmp")
        try:
            self.right_digit = pygame.image.load(self.switch(int(rt_digit)))
        except:
            print("Failed to update timer right digit sprite. Falling back on dummy.bmp")
            self.right_digit = pygame.image.load("images/dummy.bmp")

        #decrements time by 1
        if self.time > 0:
            self.time -= 1

    # artificial switch statement
    # takes int as arg
    # arg is the number to be converted to image
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
        # return the corresponding image or return image for 0
        return switchDict.get(arg, lambda: "images/timer/timer_0.bmp")

    # render image on screen
    def blitme(self):
        self.screen.blit(self.timer_body, self.rect)
        self.screen.blit(self.left_digit, self.left_digit_rect)
        self.screen.blit(self.right_digit, self.right_digit_rect)