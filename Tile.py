
class Tile:

    def __init__(self, type):
        self.type = type
        self.health = 1

    def to_str(self):
        return "%d %d" % (self.type, self.health)

    @staticmethod
    def from_str(tile_str):
        return Tile(int(tile_str.split()[0]))