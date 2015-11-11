import sys
import pygame

from Map import Map

pygame.init()

size = width, height = 720, 540
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

map = Map()
map.load('./map.txt')

print(map.tiles)

clock = pygame.time.Clock()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)
    map.draw(screen)
    pygame.display.flip()
    clock.tick(30)
