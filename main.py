import sys
import pygame

from Tile import Tile
from World import World

pygame.init()

size = 720, 540
black = 0, 0, 0
white = 255, 255, 255

screen = pygame.display.set_mode(size)

world = World()
world.map.load("./map.txt")

clock = pygame.time.Clock()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(white)
    world.draw(screen)
    pygame.display.flip()
    clock.tick(30)
