import math

class GeometricFigure:
    def __init__(self, name):
        self._nome = name
    def getNomeFig(self):
        return self._nome

class Square(GeometricFigure):
    def __init__(self, name, side):
        super().__init__(name)
        self._lado = side
    def calcArea(self):
        return self._lado ** 2

class Circle(GeometricFigure):
    def __init__(self, name, radius):
        super().__init__(name)
        self._raio = radius
    def calcArea(self):
        return math.pi * self._raio ** 2

class Rectangle(GeometricFigure):
    def __init__(self, name, side1, side2):
        super().__init__(name)
        self._lado1 = side1
        self._lado2 = side2
    def calcArea(self):
        return self._lado1 * self._lado2