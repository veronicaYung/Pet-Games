import pygame
import Main
import bath
from sys import exit

pygame.init()

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
need_sort = []
top_three = []
gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))
backDrop = pygame.image.load("instructions.png")


def instruct():
    running = True

    while running:
        gameWindow.blit(backDrop, (0, 0))
        play = bath.create_draw(600, 500, "PLAY")
        if play:  # if play button is pressed, go into game
            running = False
            Main.main()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                Main.delete()  # clear progress bar history
                pygame.quit()
                exit()


