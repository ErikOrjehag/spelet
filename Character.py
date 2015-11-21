import pygame
from Vector2D import *

class Character(object):
    def __init__(self, pos, image):
        self.image = image
        self.pos = Vector2D(pos[0], pos[1])
        self.health = 10
        self.velocity = Vector2D(0, 0)
        self.acceleration = Vector2D(0, 0)

    def update(self):
        #Update velocity
        self.velocity += self.acceleration

        #Update position
        self.pos += self.velocity


        #self.velocity *= 0
        self.acceleration = 0

    def move(self, dir):
        new_dir = Vector2D(dir)
        self.acceleration += new_dir*5

    def draw(self, screen):
        screen.blit(self.image, self.pos)