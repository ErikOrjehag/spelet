class Vector2D(object):
    """
    A 2D vector class that adds support
    for mathematical calculations.
    """
    def __init__(self, x = 0, y = 0, vec = (0, 0)):
        if vec[0] or vec[1]:
            self.x = vec[0]
            self.y = vec[1]
        else:
            self.x = x
            self.y = y

    def __get__(self, instance, owner): #HUR!? VA?
        return (self.x, self.y)

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x * other.x, self.y * other.y)
        elif isinstance(other, float):
            return Vector2D(self.x * other, self.y * other)

    def __div__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x / other.x, self.y / other.y)
        elif isinstance(other, float):
            return Vector2D(self.x / other, self.y / other)

    def __abs__(self):
        return Vector2D(abs(self.x), abs(self.y))

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y

    def distance(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)