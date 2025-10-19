import math

class Circulo:
    total_creados = 0

    def __init__(self, radio):
        self.radio = radio
        Circulo.total_creados += 1

    def area(self):
        return math.pi * (self.radio **2)
    
    def perimetro(self):
        return 2 * math.pi * self.radio
    
    @classmethod
    def total_circulos(cls):
        return cls.total_creados


circulo1 = Circulo(3)
circulo2 = Circulo(5)

print(f"Area circulo 1: {circulo1.area()}")
print(f"Area circulo 2: {circulo2.area()}")

print(f"Perimetro circulo 1: {circulo1.perimetro()}")
print(f"Perimetro circulo 2: {circulo2.perimetro()}")

print(f"Circulos creados: {Circulo.total_circulos()}")