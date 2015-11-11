import pygame


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
            posX, posY, type = line.split(" ")
            self.tiles[(int(posX), int(posY))] = int(type)

    def save(self, path):
        """
        Saves this map the a file on disc.
        :param path: The path to the file.
        :return: void
        """
        file = open(path, 'w')
        file.truncate()
        for pos, type in self.tiles.iteritems():
            file.write("%d %d %d\n" % (pos[0], pos[1], type))
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
