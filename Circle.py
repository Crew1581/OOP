from math import pi
class Circle:
    def __init__(self, radius):
        self._radius = radius
        self._diameter = radius * 2
        self._area = pi * radius ** 2

    def get_radius(self):
        return self._radius
    def get_diameter(self):
        return self._diameter
    def get_area(self):
        return self._area

circle = Circle(5)

print(circle.get_radius())
print(circle.get_diameter())
print(round(circle.get_area()))