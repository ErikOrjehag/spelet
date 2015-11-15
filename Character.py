import pygame

class Character:
    def __init__(self, pos, image):
        self.image = image
        self.pos = pygame.math.Vector2(pos)
        self.health = 10
        self.velocity = pygame.math.Vector2(0, 0)
        self.acceleration = pygame.math.Vector2(0, 0)

    def update(self):
        self.pos += self.velocity


        #self.velocity *= 0
        self.acceleration = 0

    def move(self, dir):
        self.acceleration += dir*5

    def draw(self, screen):
        screen.blit(self.image, self.pos)