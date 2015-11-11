import sys, pygame
from square import *
from images import *
pygame.init()

size = width, height = 600, 400
speed = [2, 2]
black = 0, 0, 0
white = 255, 255, 255

screen = pygame.display.set_mode(size)

gameobjects = []

coords = 10, 10

bla = Square(coords, blue)

gameobjects.append(bla)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    for obj in gameobjects:
        obj.draw(screen)

    screen.fill(white)
    pygame.display.flip()