import pygame
import Main
import bath
import howtoplay
from sys import exit

pygame.init()

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))
backDrop = pygame.image.load("startscreen.png")


def start():
    running = True
    while running:
        gameWindow.blit(backDrop, (0, 0))
        play = bath.create_draw(180, 390, "PLAY")
        if play:  # if play button pressed, run main.py
            running = False
            Main.main()
        instructions = bath.create_draw(445, 390, "INSTRUCTIONS")
        if instructions:  # if instruction button is made, display instructions
            running = False
            howtoplay.instruct()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                Main.delete()  # clear progress bar history
                pygame.quit()
                exit()


start()
