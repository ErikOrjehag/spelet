import pygame

from Tile import Tile


class Map:

    def __init__(self):
        self.tiles = {}
        self.tileSize = 16

    def load(self, path):
        """
        Loads a map stored in a file on disc.
        :param path: The path to the file.
        :return: void
        """
        file = open(path, 'r')
        content = file.read().strip()
        file.close()
        for line in content.split("\n"):
            posX, posY = line.split(":")[0].split()
            tile = Tile.from_str(line.split(":")[1].strip())
            self.tiles[(int(posX), int(posY))] = tile

    def save(self, path):
        """
        Saves this map the a file on disc.
        :param path: The path to the file.
        :return: void
        """
        file = open(path, 'w')
        file.truncate()
        for pos, tile in self.tiles.iteritems():
            print(tile)
            file.write("%d %d: " % (pos[0], pos[1]) + tile.to_str() + "\n")
        file.close()

    def draw(self, surface):
        """
        Draws the map onto a surface.
        :param surface:
        :return:
        """
        for pos, type in self.tiles.iteritems():
            color = (255, 0, 0)
            rect = (pos[0] * self.tileSize, pos[1] * self.tileSize, self.tileSize, self.tileSize)
            pygame.draw.rect(surface, color, rect)
