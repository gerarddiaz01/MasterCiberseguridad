# Principios SOLID en Python

## **Introducción a SOLID**

**SOLID** es un acrónimo que representa cinco principios fundamentales para el diseño de software orientado a objetos. Estos principios fueron promovidos por Robert C. Martin (tambien conocido como Uncle Bob) y tienen como objetivo mejorar la legibilidad, mantenibilidad y extensibilidad del código.

## **S - Principio de Responsabilidad Única (Single Responsibility Principle - SRP)**

Una clase debe tener una sola razón para cambiar, es decir, debe tener una única responsabilidad o función.

```python
class ReporteVentas:
    def __init__(self, ventas):
        self.ventas = ventas

    def calcular_total(self):
        return sum(self.ventas)

    def guardar_en_archivo(self, nombre_archivo):
        with open(nombre_archivo, 'w') as f:
            f.write(str(self.calcular_total()))
```

**Problema:** La clase `ReporteVentas` tiene dos responsabilidades: calcular el total de ventas y guardar los datos.

**Solución:** Separar responsabilidades en clases distintas.

```python
class ReporteVentas:
    def __init__(self, ventas):
        self.ventas = ventas

    def calcular_total(self):
        return sum(self.ventas)

class GuardadorArchivo:
    def guardar_en_archivo(self, reporte, nombre_archivo):
        with open(nombre_archivo, 'w') as f:
            f.write(str(reporte.calcular_total()))
```

## **O - Principio de Abierto/Cerrado (Open/Closed Principle - OCP)**

Una clase debe estar abierta para su extensión pero cerrada para su modificación.

```python
class Descuento:
    def aplicar(self, precio):
        return precio

class DescuentoPorcentaje(Descuento):
    def __init__(self, porcentaje):
        self.porcentaje = porcentaje

    def aplicar(self, precio):
        return precio * (1 - self.porcentaje)

class DescuentoFijo(Descuento):
    def __init__(self, cantidad):
        self.cantidad = cantidad

    def aplicar(self, precio):
        return precio - self.cantidad
```

**Ventaja:** Se pueden añadir nuevos tipos de descuento sin modificar las clases existentes.

## **L - Principio de Sustitución de Liskov (Liskov Substitution Principle - LSP)**

Los objetos de una clase derivada deben poder sustituir a los de su clase base sin alterar el comportamiento del programa.

```python
class Pato:
    def hacer_sonido(self):
        return "Cuac"

class PatoDeGoma(Pato):
    def hacer_sonido(self):
        return "Squeak"

def hacer_cantar(pato):
    print(pato.hacer_sonido())

hacer_cantar(Pato())        # Cuac
hacer_cantar(PatoDeGoma())  # Squeak
```

## **I - Principio de Segregación de Interfaces (Interface Segregation Principle - ISP)**

Una clase no debe verse forzada a implementar interfaces que no utiliza.

```python
from abc import ABC, abstractmethod

class Ave(ABC):
    @abstractmethod
    def volar(self):
        pass

class AveQueVuela(Ave):
    def volar(self):
        print("Estoy volando")

class Pinguino(Ave):
    def volar(self):
        raise Exception("No puedo volar")
```

**Problema:** `Pinguino` hereda de `Ave` pero no puede volar.

**Solución:** Dividir la interfaz en múltiples interfaces específicas.

```python
class Ave(ABC):
    pass

class AveVoladora(Ave):
    @abstractmethod
    def volar(self):
        pass

class AveNoVoladora(Ave):
    pass

class Pinguino(AveNoVoladora):
    pass
```

## **D - Principio de Inversión de Dependencias (Dependency Inversion Principle - DIP)**

Las clases deben depender de abstracciones y no de clases concretas.

```python
class Motor:
    def encender(self):
        print("Motor encendido")

class Coche:
    def __init__(self):
        self.motor = Motor()

    def arrancar(self):
        self.motor.encender()
```

**Problema:** `Coche` está directamente acoplado a `Motor`.

**Solución:** Usar inyección de dependencias y trabajar con abstracciones.

```python
class Motor(ABC):
    @abstractmethod
    def encender(self):
        pass

class MotorElectrico(Motor):
    def encender(self):
        print("Motor electrico encendido")

class Coche:
    def __init__(self, motor: Motor):
        self.motor = motor

    def arrancar(self):
        self.motor.encender()

motor = MotorElectrico()
coche = Coche(motor)
coche.arrancar()
```
