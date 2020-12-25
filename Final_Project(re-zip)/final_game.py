import pygame
import Main
import random
import leaderboard
from sys import exit

pygame.init()

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))
backDrop = pygame.image.load("final_game.png")
# --------ninja features-----------#
ninja = pygame.image.load("raphael.png")
ninjaX = 400
ninjaY = 500
ninjaW = 75
ninjaH = 75
ninja_speed = 4
# --------rock features --------#
rock = pygame.image.load("rock.png")
rockX = random.randint(0, WIDTH - 80)
rockY = 0
rocklist = [[rockX, rockY]]
rockW = 80
rockH = 80
rock_speed = 5
score = 0
running = True


# stats determine how hard the game will be based on completed skills
def set_level(score, stats):
    global rock_speed
    global ninja_speed
    if stats < 9:
        rock_speed = 10
    elif stats < 13:
        rock_speed = 5
    else:
        rock_speed = 3
    if score > 10:
        if stats < 9:
            rock_speed = score  # rock speed and ninja speed is proportional to score
            ninja_speed = (score / 2) - 2
        elif stats < 13:
            rock_speed = score / 2
            ninja_speed = (score / 2) - 1  # player speed is also adjusted to completed skills
        else:
            rock_speed = score / 3
            ninja_speed = score / 2


# max rocks at the same times is 10
def rocks(rocklist):
    delay = random.random()  # generate random float value form 0-1 ---> delay will drop rocks at different times
    if len(rocklist) < 10 and delay < 0.01:  # only a few of them will fall at the same time
        rockX = random.randint(0, WIDTH - 80)
        rockY = 0
        rocklist.append([rockX, rockY])


# draw the rocks
def draw_rocks(rocklist):
    for rocks in rocklist:
        Main.player(gameWindow, rock, rocks[0], rocks[1])


# update rock position and makes new rocks by removing cleared ones
def update_rock_p(rocklist):
    global score
    for rocks in (rocklist):  # for every rock you have drawn, move it down and remove it once its gone
        if rocks[1] >= 0 and rocks[1] < HEIGHT:  # if the y-coordinate of rocks are between the top and bottom of screen
            rocks[1] += rock_speed

            if rocks[1] >= HEIGHT:  # if the rocks gets off the screen, remove it
                score += 1  # if rock does not hit raphael, add a point
                rocklist.pop(rocklist.index(rocks))
    return score


# detect collision between every rock and the character
def collision(rocklist):
    global running
    for rocks in rocklist:
        rockRect = Main.rectmaker(rocks[0], rocks[1], rockW, rockH)  # create rock hit boxes
        ninjaRect = Main.rectmaker(ninjaX, ninjaY, ninjaW, ninjaH)  # create player's hit box
        if ninjaRect.colliderect(rockRect) and rocks[1] > ninjaY:
            writeScore(str(score))  # write user's score into the score file
            leaderboard.leaderboard()  # go into leaderboard screen
            running = False


# displays text to screen
def display_score(text, width, height):
    myFont = pygame.font.SysFont("monospace", 35)
    label = myFont.render(text, 1, (WHITE))
    gameWindow.blit(label, (width, height))


# writes user's score into the scores file
def writeScore(score):
    filein = open("scores.txt", "a")
    filein.write("\n")
    filein.write(score)
    filein.close()


def finale(total):
    global running
    global ninjaX
    global ninjaY
    global ninjaW
    global ninjaH
    global ninja_speed
    while running:
        gameWindow.blit(backDrop, (0, 0))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            ninjaX += ninja_speed
        elif keys[pygame.K_LEFT]:
            ninjaX -= ninja_speed
        # ---------boundaries-------------#
        if ninjaX + ninjaW > 800:  # right side boundary
            ninjaX -= ninja_speed
        if ninjaX < 0:  # left side boundary
            ninjaX += ninja_speed
        Main.player(gameWindow, ninja, ninjaX, ninjaY)
        # ---------rock drawing and detecting---------#
        set_level(score, total)
        rocks(rocklist)
        draw_rocks(rocklist)
        update_rock_p(rocklist)
        text = "Score:" + str(score)
        display_score(text, WIDTH - 200, HEIGHT - 40)

        collision(rocklist)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                Main.delete()
                pygame.quit()
                exit()
