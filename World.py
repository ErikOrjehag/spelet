from Map import Map


class World:
    """
    Contains all game objects and the map.
    """

    def __init__(self):
        self.player = None
        self.players = None
        self.map = Map()

    def update(self):
        print("update")

    def draw(self, surface):
        self.map.draw(surface)
