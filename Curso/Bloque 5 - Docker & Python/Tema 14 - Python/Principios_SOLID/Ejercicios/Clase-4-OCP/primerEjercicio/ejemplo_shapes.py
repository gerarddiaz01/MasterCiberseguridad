'''Éste código define una jerarquía de figuras geométricas usando clases abstractas y herencia.
La clase base Shape() obliga a que todas las figuras implementen el método calculate_area().
Cada figura concreta (Circle, Rectangle, Square) implementa su propia lógica para calcular el área.
Esto sigue el Open/Closed Principle: puedes agregar nuevas figuras extendiendo la clase base, sin modificar el código existente.'''

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    def __init__(self, shape_type):
        self.shape_type = shape_type

    @abstractmethod
    def calculate_area(self):
        pass
# Shape() es una clase base abstracta (hereda de ABC)
# Tiene un atributo shape_type para identificar el tipo de figura
# El método calculate_area es abstracto: todas las subclases deben implementarlo

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius ** 2
# Hereda de Shape()
# El constructor recibe el radio y llama al constructor de la clase base con "circle": se ha hecho la herencia y ahora estás inicializando los
    # atributos de la clase padre, que es self.shape_type o "circle" en éste caso.
# Implementa calculate_area para devolver el área del círculo

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height
# Hereda de Shape()
# El constructor recibe el ancho y alto, y llama al constructor base con "rectangle" (se le pasan los atributos de la clase padre)
# Implementa calculate_area para devolver el área del rectángulo

class Square(Shape):
    def __init__(self, side):
        super().__init__("square")
        self.side = side

    def calculate_area(self):
        return self.side ** 2
# Hereda de Shape
# El constructor recibe el lado y llama al constructor base con "square"
# Implementa calculate_area para devolver el área del cuadrado