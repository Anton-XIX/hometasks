import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # @property
    # def x(self):
    #     return self.x
    #
    # @x.setter
    # def x(self, x):
    #     self.x = x
    #
    # @property
    # def y(self):
    #     return self.y
    #
    # @y.setter
    # def y(self, y):
    #     self.y = y


class Circle(Point):
    def __init__(self, x, y, radius):
        self.radius = radius
        self.center = super().__init__(x, y)

    def get_square(self):
        return math.pi * pow(self.radius, 2)

    def get_perimetr(self):
        return 2 * math.pi * self.radius


class Triangle(Point):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.p1 = Point(x1, y1)
        self.p2 = Point(x2, y2)
        self.p3 = Point(x3, y3)

    def find_sides(self):
        side_a = math.sqrt((self.p2.x - self.p1.x) ** 2 + (self.p2.y - self.p1.y) ** 2)
        side_b = math.sqrt((self.p2.x - self.p3.x) ** 2 + (self.p2.y - self.p3.y) ** 2)
        side_c = math.sqrt((self.p3.x - self.p1.x) ** 2 + (self.p3.y - self.p1.y) ** 2)
        return [side_a, side_b, side_c]

    def get_perimetr(self):
        sides = self.find_sides()
        return (sides[0] + sides[1] + sides[2]) / 2

    def get_square(self):
        sides = self.find_sides()
        per = self.get_perimetr()
        return math.sqrt(per * (per - sides[1]) * (per - sides[0]) * (per - sides[2]))


class Square(Point):
    def __init__(self, x1, y1, x2, y2):
        self.p1 = Point(x1, y1)
        self.p2 = Point(x2, y2)

    def find_side(self):
       return math.sqrt((self.p2.x - self.p1.x) ** 2 + (self.p2.y - self.p1.y) ** 2)

    def get_perimetr(self):
        return self.find_side()*4

    def get_square(self):
        return self.find_side() ** 2


