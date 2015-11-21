import sys, pygame
from Square import *
from Character import *
import Images
pygame.init()

pygame.display.set_mode()
size = width, height = 600, 400
speed = [2, 2]
black = 0, 0, 0
white = 255, 255, 255

screen = pygame.display.set_mode(size)

gameobjects = []

coords = 10, 10

bla = Square(coords, Images.blue)

player = Character((50, 50), Images.blue)

gameobjects.append(bla)
gameobjects.append(player)



while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or \
                (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            sys.exit()

        #
        # Checking keys
        #
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            player.move((0, -1))
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            player.move((1, 0))
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            player.move((0, 1))
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            player.move((-1, 0))

    screen.fill(white)

    for obj in gameobjects:
        obj.draw(screen)


    pygame.display.flip()