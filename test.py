import sys, pygame
from Square import *
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

gameobjects.append(bla)



while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or \
                (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            sys.exit()

        #
        # Checking keys
        #
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            bla.coords = bla.coords[0], bla.coords[1] - 5
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            bla.coords = bla.coords[0] + 5, bla.coords[1]
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            bla.coords = bla.coords[0], bla.coords[1] + 5
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            bla.coords = bla.coords[0] - 5, bla.coords[1]

    screen.fill(white)

    for obj in gameobjects:
        obj.draw(screen)


    pygame.display.flip()