import pygame
import foodcourt
from sys import exit
import random
import Main

pygame.init()

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))
backDrop = pygame.image.load("bath.png")
display = []
correct_sequence = ["soap", "lather", "scrub", "rinse"]


# create a random sequence of the choice which will be displayed on the buttons
def mix_order(choices):
    for i in range(len(choices)):
        rand = random.randint(0, len(choices) - 1)
        step = choices.pop(rand)
        display.append(step)
    return display


# create and draw buttons
def create_draw(x, y, display):
    instance = foodcourt.button(x, y, display)
    return instance.draw_button()


def bath():
    choices = ["soap", "lather", "scrub", "rinse"]
    display = mix_order(choices)
    userSteps = []
    running = True
    while running:
        gameWindow.blit(backDrop, (0, 0))
        step_a = create_draw(600, 100, display[0])
        if step_a:  # if button is clicked, add the text to a list, this will determine if you got the correct sequence
            userSteps.append(display[0])
        step_b = create_draw(600, 200, display[1])
        if step_b:
            userSteps.append(display[1])

        step_c = create_draw(600, 300, display[2])
        if step_c:
            userSteps.append(display[2])

        step_d = create_draw(600, 400, display[3])
        if step_d:
            userSteps.append(display[3])

        quit = create_draw(600, 500, "Quit")
        if quit:
            userSteps.clear()
            display.clear()
            running = False

        if len(userSteps) == 4:
            if userSteps == correct_sequence:  # check if the clicked sequence matches the original one
                print("correct!")
                foodcourt.updatebar("3")
                foodcourt.updatebar("tutorials")
                userSteps.clear()
                display.clear()
                running = False
            else:
                userSteps.clear()
                print("try again")
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                Main.delete()
                pygame.quit()
                exit()
