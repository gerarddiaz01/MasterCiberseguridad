'''Tenemos un código no optimizado y vamos a refactorizarlo para que cumpla con OCP'''
# Código que no cumple con OCP
def calcular(a, b, operacion):
    if operacion == "sumar":
        return a + b
    elif operacion == "restar":
        return a - b
    else:
        print("Operación no soportada")

# Código refactorizado
from abc import ABC, abstractmethod

class Operacion(ABC):
    @abstractmethod
    def calcular(self, a, b):
        pass

class Suma(Operacion):
    def calcular(self, a, b):
        return a + b

class Resta(Operacion):
    def calcular(self, a, b):
        return a - b

class Multiplicacion(Operacion):
    def calcular(self, a, b):
        return a * b

class Division(Operacion):
    def calcular(self, a, b):
        return a / b if b != 0 else None

# Nueva operación: Potenciación (a^b)
class Potenciacion(Operacion):
    def calcular(self, a, b):
        return a ** b
    
def calcular_operacion(a, b, operacion_obj: Operacion):
    resultado = operacion_obj.calcular(a, b)
    print(f"Resultado: {resultado}")

calcular_operacion(10, 2, Suma())
calcular_operacion(10, 2, Resta())
calcular_operacion(10, 2, Multiplicacion())
calcular_operacion(10, 2, Division())
calcular_operacion(10, 2, Potenciacion())

'''
Podemos fácilmente añadir nuevas operaciones, y cada una tendrá una operación distinta. En la lógica genérica importamos como atributo
el tipo de operación que es al crear una instancia y dicha lógica depende según éste tipo de operación, ya que llama al método abstracto que se adapta según
la operación. Fácil de extender sin modificar la main logic, modular y óptimo.
'''