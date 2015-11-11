import pygame
pygame.init()

class Square:
    def __init__(self, coords, image):
        self.coords = coords
        self.image = image

    def draw(self, screen):
        screen.blit(self.image, self.coords)