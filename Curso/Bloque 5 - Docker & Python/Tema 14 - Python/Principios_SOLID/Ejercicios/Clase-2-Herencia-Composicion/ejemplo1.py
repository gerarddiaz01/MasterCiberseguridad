# Ejercicio
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonidos(self):
        pass


class Conejo(Animal):
    def hacer_sonidos(self):
        return "Hola soy un conejo"


mi_conejo = Conejo("Zanahoria")
# print(mi_conejo.nombre)
# print(mi_conejo.hacer_sonidos())


# Ejemplo 2 - herencia multiple
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def conducir(self):
        return "Rum rum!!"

    # def chapero(self):
    #     return "Estoy siendo refactoreado"


# class Persona(Vehiculo, Animal):
#     def __init__(self, nombre, marca, modelo):
#         Vehiculo.__init__(self, marca, modelo)
#         Animal.__init__(self, nombre)

#     def presentarse(self):
#         return f"Soy {self.nombre}, conduzco un {self.marca} {self.modelo}"

#     def hacer_sonidos(self):
#         return "Hola soy una persona"


# persona1 = Persona("Juan", "Toyota", "Corolla")
# print(persona1.presentarse())
# print(persona1.conducir())
# print(persona1.hacer_sonidos())


# Clases compuestas
class Persona:
    def __init__(self, nombre, vehiculo, animal):
        self.nombre = nombre
        self.vehiculo = vehiculo
        self.animal = animal

    def presentarse(self):
        return f"Soy { self.nombre}, conduzco un {self.vehiculo.marca} {self.vehiculo.modelo} y mi mascota es: { self.animal.nombre}"


vehiculo1 = Vehiculo("Toyota", "Corolla")
animal1 = Animal("Du")
persona2 = Persona("Raquel", vehiculo1, animal1)
print(persona2.presentarse())
print(persona2.vehiculo.conducir())
