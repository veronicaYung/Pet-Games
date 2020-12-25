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

gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))
backDrop2 = pygame.image.load("baking.jpg")
display_steps = []
correct_sequence = ["mix", "bake", "icing", "eat!"]


def bake():
    mix_steps = ["mix", "bake", "icing", "eat!"]
    display_steps = bath.mix_order(mix_steps)
    userSteps2 = []
    running = True
    while running:
        gameWindow.blit(backDrop2, (0, 0))

        step_a = bath.create_draw(600, 100, display_steps[0])  # returns instance.draw_button
        if step_a:
            userSteps2.append(display_steps[0])

        step_b = bath.create_draw(600, 200, display_steps[1])
        if step_b:
            userSteps2.append(display_steps[1])

        step_c = bath.create_draw(600, 300, display_steps[2])
        if step_c:
            userSteps2.append(display_steps[2])

        step_d = bath.create_draw(600, 400, display_steps[3])
        if step_d:
            userSteps2.append(display_steps[3])

        if len(userSteps2) == 4:
            if userSteps2 == correct_sequence:
                print("correct!")
                foodcourt.updatebar("6")
                foodcourt.updatebar("tutorials")
                userSteps2.clear()
                display_steps.clear()
                running = False
            else:
                print("try again")
                userSteps2.clear()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                Main.delete()
                pygame.quit()
                exit()
