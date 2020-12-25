import pygame
from pygame.locals import *
import random
from sys import exit
import Main

pygame.init()

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
clicked = False
points = 0

gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))
backDrop = pygame.image.load("foodcourt.png")
d = {'fries': "bad", 'worms': "bad", 'burgers': "bad", 'poutine': "bad", 'salad': "good", 'fruit': "good",
     'pasta': "good", 'kale': "good"}
bad_list = ['fries', 'worms', 'burgers', 'poutine']  # must have two lists to ensure there's atleast one good food
good_list = ['salad', 'fruit', 'pasta', 'kale']


def get_foods(alist):
    food_list = alist[:]
    display = []
    for i in range(2):
        rand = random.randint(0, len(food_list) - 1)
        step = food_list.pop(rand)
        display.append(step)
    return display


# ---progressbar--#
def updatebar(line):
    f = open("progbar.txt", "r+")
    content = f.read()
    f.seek(0, 0)  # activity information is being added to the top of the list
    f.write(line.strip('\r\n') + '\n' + content)  # shift to new line and line.strip('\r\n') is the line separator


class button():
    # button colors:
    button_col = (190, 168, 167)
    hover_col = (244, 219, 216)
    click_col = (203, 239, 182)
    text_col = BLACK
    width = 180  # all buttons are the same size
    height = 40

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def draw_button(self):  # Draws the button with text
        global clicked
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # create button
        button_rect = Rect(self.x, self.y, self.width, self.height)  # store rectangle co-ords+measurements
        if button_rect.collidepoint(pos):  # check if mouse is within the button
            if pygame.mouse.get_pressed()[0] == 1:  # detect left click
                clicked = True
                pygame.draw.rect(gameWindow, self.click_col, button_rect)  # change color of button
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:  # if it was clicked but released
                clicked = False  # reset trigger
                action = True
            else:  # if we are just hovering
                pygame.draw.rect(gameWindow, self.hover_col, button_rect)

        else:  # nothing is being pressed or hovering
            pygame.draw.rect(gameWindow, self.button_col, button_rect)
        # add text to buttons
        font = pygame.font.SysFont("Verdana", 14, "bold")
        text = font.render(self.text, 1, self.text_col)
        gameWindow.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

        return action


def foodcourt():
    global points
    badfoods = get_foods(bad_list)
    goodfoods = get_foods(good_list)
    belly = []
    foods = badfoods + goodfoods
    food1 = button(75, 200, foods[0])
    food2 = button(325, 200, foods[1])
    food3 = button(75, 350, foods[2])
    food4 = button(325, 350, foods[3])
    quit = button(550, 500, "Quit")
    running = True
    while running:
        gameWindow.blit(backDrop, (0, 0))
        # ------if buttons are being pressed ----- #
        if food1.draw_button():
            for foods in d:
                if foods == food1.text:
                    belly.append(d[foods])

        if food2.draw_button():
            for foods in d:
                if foods == food2.text:
                    belly.append(d[foods])

        if food3.draw_button():
            for foods in d:
                if foods == food3.text:
                    belly.append(d[foods])

        if food4.draw_button():
            for foods in d:
                if foods == food4.text:
                    belly.append(d[foods])

        if quit.draw_button():
            for foods in belly:
                if foods == "good":
                    points += 1
                else:
                    points -= 1
            running = False

        if points >= 5:  # if the user chooses enough foods from the good foods list, update bar
            updatebar("6")
            updatebar("food")
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                Main.delete()
                pygame.display.update()
                pygame.quit()
                exit()
