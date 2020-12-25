import pygame
import Main
import final_game
from sys import exit

pygame.init()
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
need_sort = []
top_three = []
gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))
backDrop = pygame.image.load("leaderboard.png")


def merge(list1, list2):
    result = []
    while len(list1) > 0 or len(list2) > 0:
        if len(list1) == 0:
            result.append(list2.pop(0))
        elif len(list2) == 0:
            result.append(list1.pop(0))
        else:
            if list1[0] < list2[0]:
                result.append(list1.pop(0))
            else:
                result.append(list2.pop(0))
    return result


def mergesort(alist):
    if len(alist) <= 1:
        return alist

    list1 = mergesort(alist[:int(len(alist) / 2)])
    list2 = mergesort(alist[int(len(alist) / 2):])
    return merge(list1, list2)


def readInScores():
    filein = open("scores.txt", "r")
    score = filein.readline().strip()
    while score != "":
        need_sort.append(int(score))
        score = filein.readline().strip()
    filein.close()
    # print(need_sort)


def getThree(sorted_list):
    sorted_list.reverse()


def leaderboard():
    running = True
    readInScores()
    sorted = mergesort(need_sort)
    # print("sorted list",sorted)
    getThree(sorted)

    while running:
        gameWindow.blit(backDrop, (0, 0))
        final_game.display_score(str(sorted[0]), 450, 194)
        final_game.display_score(str(sorted[1]), 450, 254)
        final_game.display_score(str(sorted[2]), 450, 325)
        final_game.display_score(str(final_game.score), 520, 460)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                Main.delete()  # clear progress bar history
                pygame.quit()
                exit()
