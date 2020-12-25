import pygame
import bath
import foodcourt
import Main
from sys import exit

pygame.init()

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
clicked = False
gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))


# guessing will update depending on progress bar
def guessing(backdrop, choices, correct, bar):
    score = 0
    backDrop = pygame.image.load(backdrop)
    display_pet = bath.mix_order(choices)
    running = True
    while running:
        gameWindow.blit(backDrop, (0, 0))
        step_a = bath.create_draw(500, 250, display_pet[0])  # returns instance.draw_button
        if step_a:  # check if the button is pressed and has correct answer
            if display_pet[0] == correct:
                score += 1
            else:
                print("try again!")

        step_b = bath.create_draw(500, 300, display_pet[1])
        if step_b:
            if display_pet[1] == correct:
                score += 1
            else:
                print("try again!")
        step_c = bath.create_draw(500, 350, display_pet[2])
        if step_c:
            if display_pet[2] == correct:
                score += 1
            else:
                print("try again!")
        step_d = bath.create_draw(500, 400, display_pet[3])
        if step_d:
            if display_pet[3] == correct:
                score += 1
            else:
                print("try again!")
        if score == 1:
            display_pet.clear()
            running = False
            choices.clear()
            foodcourt.updatebar(bar)  # updating progress to unlock new guessing image
            foodcourt.updatebar("intuition")

        pygame.display.update()

        for event in pygame.event.get():  # if user presses quit on this game window, not lobby--> close screen
            if event.type == pygame.QUIT:
                running = False
                Main.delete()
                pygame.quit()
                exit()
