import pygame
from Timer import Timer
from global_toolbox import GlobalSettings
class Score(Timer):
    def __init__(self, screen, int, side):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        leftDigit_loc = [0, GlobalSettings().play_area_height + -10]
        rightDigit_loc = [0, GlobalSettings().play_area_height + -10]
        if(side == "LEFT"):
            leftDigit_loc[0] = self.screen_rect.left
            rightDigit_loc[0] = self.screen_rect.left + 30
        elif(side == "RIGHT"):
            leftDigit_loc[0] = self.screen_rect.right - 60
            rightDigit_loc[0] = self.screen_rect.right - 30

        if int > 99:
            self.time = 99
        elif int <= 0:
            self.time = 1
        else:
            self.time = int

        # load image and rect for left digit
        try:
            self.left_digit = pygame.image.load("images/timer/zero.png")
        except:
            print("Failed to load timer left digit sprite. Falling back on dummy.bmp")
            self.left_digit = pygame.image.load("images/dummy.bmp")
        finally:
            self.left_digit_rect = self.left_digit.get_rect()

        #position left digit on screen
        self.left_digit_rect.left = leftDigit_loc[0]
        self.left_digit_rect.bottom = leftDigit_loc[1]

        # load image and rect for right digit
        try:
            self.right_digit = pygame.image.load("images/timer/zero.png")
        except:
            print("Failed to load timer right digit sprite. Falling back on dummy.bmp")
            self.right_digit = pygame.image.load("images/dummy.bmp")
        finally:
            self.right_digit_rect = self.right_digit.get_rect()

        #position right digit on screen
        self.right_digit_rect.left = rightDigit_loc[0]
        self.right_digit_rect.bottom = rightDigit_loc[1]

        self.update(int)

    def update(self, current_score):
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

        self.time = current_score

    def blitme(self):
        self.screen.blit(self.left_digit, self.left_digit_rect)
        self.screen.blit(self.right_digit, self.right_digit_rect)