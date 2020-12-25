# ********************IMPORTANT **********************************
# START GAME WITH STARTUP.PY
# everything does connect to main.py except for the start screen
# ****************************************************************
import pygame
import foodcourt
import bath
import bake
import guess1
import final_game
from sys import exit

pygame.init()
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# reduce amount of files for the skills intuition
guessing_pets = [["hamster.png", ["rat", "hamster", "cat", "cheese"]],
                 ["parrot.png", ["ferret", "parrot", "chicken", "ham"]],
                 ["salamander.png", ["DNE", "salamander", "gecko", "skink"]]]
# dictionary is used to store the most recently completed tasks
updatebar_dict = {}


# clears the progress bar's history
def delete():
    filein = open("progbar.txt", "w")
    filein.close()


# reads in from a file of user's activity and stores most recent activity in updatebar_dict
def progbar():
    updatebar_dict.clear()
    filein = open("progbar.txt", "r")
    skill = filein.readline().strip()
    while skill != "":
        completed = filein.readline().strip()
        if skill not in updatebar_dict:
            updatebar_dict[skill] = int(completed)
        skill = filein.readline().strip()

    return updatebar_dict


# draws bar by going through the dictionary
def drawbar():
    total = 6
    print("========updated=======")
    for skills in updatebar_dict:
        print(skills, "\n", "|", (updatebar_dict[skills] * "#"), ((total - updatebar_dict[skills]) * "-"), "|",
              "progess:", updatebar_dict[skills], "/", total)

    return " "


# create hit boxes for collision detection
def rectmaker(rectX, rectY, width, height):
    rect = pygame.Rect(rectX, rectY, width, height)
    return rect


# update player on screen
def player(screen, image, playerX, playerY):
    screen.blit(image, (playerX, playerY))


def main():
    total = 0
    gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))
    backDrop = pygame.image.load("lobby.png")
    turtle = pygame.image.load("turtle.png")

    # ---------- games+player collision measurements and co-ordinates ---------#
    # player
    playerX = 100
    playerY = 500
    playerW = 40
    playerH = 40
    # food court
    foodcourtX = 250
    foodcourtY = 220
    foodcourtW = 160
    foodcourtH = 30
    # bake, bath
    tutorialX = 460
    tutorialY = 220
    tutorialW = 90
    tutorialH = 30
    # guessing game
    guessX = 580
    guessY = 500
    guessW = 100
    guessH = 160
    # final game
    finalX = 440
    finalY = 335
    finalW = 135
    finalH = 78

    running = True
    while running:
        gameWindow.blit(backDrop, (0, 0))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:  # can go diagonal
            playerY -= 2
        if keys[pygame.K_DOWN]:
            playerY += 2
        if keys[pygame.K_RIGHT]:
            playerX += 2
        if keys[pygame.K_LEFT]:
            playerX -= 2
        # ---------boundaries-------------#
        if playerX + playerW > 580:  # right side boundary
            playerX -= 2
        if playerX < 100:  # left side boundary
            playerX += 2
        if playerY < 220:  # top boundary
            playerY += 2
        if playerY > 500:  # bottom boundary
            playerY -= 2
        player(gameWindow, turtle, playerX, playerY)

        # ------------collision detection ----------#
        # player and food court detection
        playerRect = rectmaker(playerX, playerY, playerW, playerH)
        foodcourtR = rectmaker(foodcourtX, foodcourtY, foodcourtW, foodcourtH)
        if playerRect.colliderect(foodcourtR):  # player hitting food-court hitbox
            foodcourt.foodcourt()
            playerX = 100
            playerY = 500
            progbar()
            drawbar()

        # player and tutorial games detection
        tutorialR = rectmaker(tutorialX, tutorialY, tutorialW, tutorialH)
        if playerRect.colliderect(
                tutorialR) and "tutorials" not in updatebar_dict:  # "pre-requisites" to play the first tutorial
            bath.bath()
            playerX = 100
            playerY = 500
            progbar()
            drawbar()
        elif playerRect.colliderect(tutorialR) and updatebar_dict["tutorials"] == 3:  # "progress bar pre-requisites" to play the second tutorial
            bake.bake()
            playerX = 100
            playerY = 500
            progbar()
            drawbar()

        # player and guessing game detection
        playerRect_mod = rectmaker(playerX + 40, playerY, playerW, playerH)
        guessR = rectmaker(guessX, guessY, guessW, guessH)
        if playerRect_mod.colliderect(guessR) and "intuition" not in updatebar_dict:
            guess1.guessing(guessing_pets[0][0], guessing_pets[0][1], guessing_pets[0][1][1], "2")
            playerX = 100
            playerY = 500
            progbar()
            drawbar()
        elif playerRect_mod.colliderect(guessR) and updatebar_dict["intuition"] == 2:  # "progress bar pre-requisites" to play the second intuition game
            guess1.guessing(guessing_pets[1][0], guessing_pets[1][1], guessing_pets[1][1][1], "4")
            playerX = 100
            playerY = 500
            progbar()
            drawbar()
        elif playerRect_mod.colliderect(guessR) and updatebar_dict["intuition"] == 4:  # "progress bar pre-requisites" to play the third intuition game
            guess1.guessing(guessing_pets[2][0], guessing_pets[2][1], guessing_pets[2][1][1], "6")
            playerX = 100
            playerY = 500
            progbar()
            drawbar()

        # player and final challenge detection
        finalR = rectmaker(finalX, finalY, finalW, finalH)
        if playerRect_mod.colliderect(finalR):
            progbar()
            for update in updatebar_dict:
                total += updatebar_dict[update]
            final_game.finale(total)
            playerX = 100
            playerY = 500

        pygame.display.update()

        for event in pygame.event.get():  # if the user quits the game
            if event.type == pygame.QUIT:
                delete()  # erase the progress bar's log for a new player, restarts game data for completd tasks
                running = False
                pygame.quit()
                exit()
