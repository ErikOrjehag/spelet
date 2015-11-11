import pygame
import os

main_dir = os.path.split(os.path.abspath(__file__))[0]

#
# Load an image from data directory
#
def load_image(file):
    file = os.path.join(main_dir, 'data', file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "&s" %s'%(file, pygame.get_error()))
    return surface

blue = load_image("blue.png")