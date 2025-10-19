# from abc import ABC, abstractmethod

# class Vehiculo(ABC):
#     @abstractmethod
#     def conducir(self):
#         pass

#     @abstractmethod
#     def volar(self):
#         pass

# class Coche(Vehiculo):
#     def conducir(self):
#         print("El coche está en marcha.")
#     def volar(self):
#         print("El coche no puede volar, acción no soportada.")

# class Avion(Vehiculo):
#     def conducir(self):
#         print("El avión rueda por la pista.")
#     def volar(self):
#         print("El avión despega y está volando.")


'''Analiza el código: la interfaz Vehiculo obliga a todos los vehículos a tener la capacidad de volar(), lo cual no tiene sentido para un coche. 
Esto viola el principio ISP. Nuestra tarea es refactorizar este diseño aplicando el Principio de Segregación de Interfaz. Es decir, dividir la 
interfaz en las partes necesarias y ajusta las clases Coche y Avion en consecuencia.'''

from abc import ABC, abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    def conducir(self):
        pass

class VehiculoVolador(ABC):
    @abstractmethod
    def volar(self):
        pass

class Coche(Vehiculo):
    def conducir(self):
        print("El coche está en marcha.")

class Avion(Vehiculo, VehiculoVolador):
    def conducir(self):
        print("El avión rueda por la pista.")
    def volar(self):
        print("El avión despega y está volando.")